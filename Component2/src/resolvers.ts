import {users, reactions, lines, changedFiles, generalComments, inlineComments, pullRequests} from './db.js';
import { AddGeneralCommentInput, AddInlineCommentInput, AddReactionInput, MergePullRequestInput, PullRequestInput, RejectPullRequestInput, RemoveReactionInput, View } from './types.js';

enum Status {
  PENDING = 'PENDING',
  MERGE_CONFLICT = 'MERGE_CONFLICT',
  REJECTED = 'REJECTED',
  MERGED = 'MERGED',
}

export const resolvers = {
  Query: {
    pullRequests: (parent: any, args: {status: Status, pageLimit: number, offset: number}) => {
      let prs = pullRequests
      let prOutput = [];
      if (args.status) {
        prs = pullRequests.filter(pr => pr.status === args.status);
      }
      if (prs) {
        // offset too large
        if (args.offset*args.pageLimit > prs.length) {
          throw new Error('Offset out of bounds.');
        }
        // handle unfilled last page
        else if (args.offset*args.pageLimit + args.pageLimit > prs.length) {
          prOutput = pullRequests.slice(args.offset*args.pageLimit, prs.length);
        }
        else {
          prOutput = prs.slice(args.offset*args.pageLimit, args.offset*args.pageLimit + args.pageLimit);
        }
        
        const views : View[] = [];
        for (let i = 0; i < prs.length; i++) {
          const view : View = {
            pullRequests: prOutput[i],
            changedFiles: changedFiles, //assume changedFiles is shared for all pull requests, for mocking purpose
          };
          views.push(view);
        }
        return views;
      } 
      else {
        throw new Error('No pull requests found.');
      }
    }
  },
  Mutation: {
    addPullRequest: (parent: any, args: {input: PullRequestInput}) => {
      // check if source commit and target branch are empty
      if (args.input.sourceCommit === "" || args.input.targetBranch === "") {
        throw new Error('Source commit or target branch cannot be empty.');
      }
      // check if source commit already had a pull request
      if (pullRequests.find(pr => pr.sourceCommit === args.input.sourceCommit)) {
        throw new Error('Pull request with this source commit already exists.');
      }
      const pr = {
        id: String(pullRequests.length + 1),
        description: args.input.description,
        sourceCommit: args.input.sourceCommit,
        targetBranch: args.input.targetBranch,
        status: Status.PENDING,
        generalComments: [],
        inlineComments: [],
      };
      pullRequests.push(pr);
      return pr;
    },

    addGeneralComment: (parent: any, args: {input: AddGeneralCommentInput}) => {
      const pr = pullRequests.find(pr => pr.id === args.input.prId);
      if (pr) {
        // check if user exists
        if (!users.find(user => user.id === args.input.author)) {
          throw new Error('User not found.');
        }
        else {
          const comment = {
            id: String(10000 + generalComments.length + 1),
            content: args.input.content,
            author: users.find(user => user.id === args.input.author)!,
            reactions: [],
            reactionCount: 0,
          };
          generalComments.push(comment);
          pr.generalComments.push(comment);
          return generalComments;
        }
      }
      else {
        throw new Error('Pull request not found.');
      }
    },

    addInlineComment: (parent: any, args: {input: AddInlineCommentInput}) => {
      const pr = pullRequests.find(pr => pr.id === args.input.prId);
      if (pr) {
        // check if user, file, and line exist
        if (!users.find(user => user.id === args.input.author)) {
          throw new Error('User not found.');
        }
        else if (!changedFiles.find(file => file.id === args.input.fileId)) {
          throw new Error('File not found.');
        } 
        else if (!lines.find(line => line.lineNum === args.input.lineNum)) {
          throw new Error('Line not found.');
        }
        else {
          const comment = {
            id: String(20000 + inlineComments.length + 1),
            file: changedFiles.find(file => file.id === args.input.fileId)!,
            line: lines.find(line => line.lineNum === args.input.lineNum)!,
            content: args.input.content,
            author: users.find(user => user.id === args.input.author)!,
            reactions: [],
            reactionCount: 0,
          };
          inlineComments.push(comment);
          pr.inlineComments.push(comment);
          return inlineComments;
        }
      }
      else {
        throw new Error('Pull request not found.');
      }
    },

    addReaction: (parent: any, args: {input: AddReactionInput}) => {

      const genCom = generalComments.find(comment => comment.id === args.input.commentId)
      const inlCom = inlineComments.find(comment => comment.id === args.input.commentId)
      const user = users.find(user => user.id === args.input.author)

      // check if user exists
      if (!user) {
        throw new Error('User not found.');
      }

      const reaction = {
        id: String(reactions.length + 1),
        type: args.input.type,
        user: user,
      };

      // add to general comments or inline comments
      if (genCom) {
        // check if user has already reacted to this comment
        if (genCom.reactions.find(reaction => reaction.user.id === args.input.author)) {
          throw new Error('User has already reacted to this comment.');
        }
        else {
          genCom.reactions.push(reaction);
          genCom.reactionCount = genCom.reactions.length;
          reactions.push(reaction);
          return genCom.reactions;
        }
      }
      else if (inlCom) {
        // check if user has already reacted to this comment
        if (inlCom.reactions.find(reaction => reaction.user.id === args.input.author)) {
          throw new Error('User has already reacted to this comment.');
        }
        else {
          inlCom.reactions.push(reaction);
          inlCom.reactionCount = inlCom.reactions.length;
          reactions.push(reaction);
          return inlCom.reactions;
        }
      }
      else {
        throw new Error('Comment not found.');
      }
        
    },

    removeReaction: (parent: any, args: {input: RemoveReactionInput}) => {
      const reaction = reactions.find(reaction => reaction.id === args.input.reactionId);
      // check if reaction exists
      if (!reaction) {
        throw new Error('Reaction not found.');
      }
      // check if user is the creator of this reaction
      else if (reaction.user.id !== args.input.user) {
        throw new Error('User does not own this reaction.');
      }
      else {
        reactions.splice(reactions.indexOf(reaction), 1);
        // remove from generalComments or inlineComments
        if (generalComments.find(comment => comment.reactions.find(reaction => reaction.id === args.input.reactionId))) {
          const comment = generalComments.find(comment => comment.reactions.find(reaction => reaction.id === args.input.reactionId))!;
          comment.reactions.splice(comment.reactions.indexOf(reaction), 1);
          comment.reactionCount = comment.reactions.length;
        }
        else {
          const comment = inlineComments.find(comment => comment.reactions.find(reaction => reaction.id === args.input.reactionId))!;
          comment.reactions.splice(comment.reactions.indexOf(reaction), 1);
          comment.reactionCount = comment.reactions.length;
        }
        return reactions;
      }
    },

    mergePullRequest: (parent: any, args: {input: MergePullRequestInput}) => {
      const pr = pullRequests.find(pr => pr.id === args.input.prId);
      if (pr) {
        // check if pr is already merged or rejected
        if (pr.status === Status.MERGED) {
          throw new Error('Pull request already merged.');
        }
        else if (pr.status === Status.REJECTED) {
          throw new Error('Pull request already rejected.');
        }
        //for simplicity, assume pr with sourceCommit field starting with 0 has merge conflict
        else if (pr.sourceCommit.charAt(0) === '0') {
          pr.status = Status.MERGE_CONFLICT;
          throw new Error('Merge conflict detected. Merge failed.');
        }
        else {
          pr.status = Status.MERGED;
          return pr;
        }
      }
      else {
        throw new Error('Pull request not found.');
      }
    },

    rejectPullRequest: (parent: any, args: {input: RejectPullRequestInput}) => {
      const pr = pullRequests.find(pr => pr.id === args.input.prId);
      if (pr) {
        // check if pr is already merged or rejected
        if (pr.status === Status.REJECTED) {
          throw new Error('Pull request already rejected.');
        }
        else if (pr.status === Status.MERGED) {
          throw new Error('Pull request already merged.');
        }
        else {
          pr.status = Status.REJECTED;
          return pr;
        }
      }
      else {
        throw new Error('Pull request not found.');
      }
    }
  },
};
