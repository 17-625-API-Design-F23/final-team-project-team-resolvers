export const typeDefs = ` 
  type User {
    id: ID!
    username: String!
    account: String!
  }

  type GeneralComment {
    id: ID!
    content: String!
    author: User!
    reactions: [Reaction]!
    reactionCount: Int!
  }

  type InlineComment {
    id: ID!
    file: ChangedFile!
    line: Line!
    content: String!
    author: User!
    reactions: [Reaction]!
    reactionCount: Int!
  }

  type Reaction {
    id: ID!
    type: String!
    user: User!
  }

  type ChangedFile {
    id: ID!
    filename: String!
    changedLines: [Line!]!
  }

  type Line {
    id: ID!
    lineNum: Int!
    content: String!
  }

  type PullRequest {
    id: ID!
    description: String!
    sourceCommit: String!
    targetBranch: String!
    status: Status!
    generalComments: [GeneralComment]!
    inlineComments: [InlineComment]!
  }

  type View {
    pullRequests: PullRequest!
    changedFiles: [ChangedFile!]!
  }

  enum Status {
    PENDING,
    MERGE_CONFLICT,
    REJECTED,
    MERGED,
  }

  type Query {
    pullRequests(status: Status, pageLimit: Int, offset: Int): [View]!
  }

  type Mutation {
    addPullRequest(input: addPullRequestInput!): PullRequest!
    addGeneralComment(input: addGeneralCommentInput!): [GeneralComment!]!
    addInlineComment(input: addInlineCommentInput!): [InlineComment!]!
    addReaction(input: addReactionInput!): [Reaction!]!
    removeReaction(input: removeReactionInput!): [Reaction!]!
    mergePullRequest(input: mergePullRequestInput!): PullRequest!
    rejectPullRequest(input: rejectPullRequestInput!): PullRequest!
  }

  input addPullRequestInput {
    description: String!
    sourceCommit: String!
    targetBranch: String!
  }

  input addGeneralCommentInput {
    prId: ID!
    content: String!
    author: ID!
  }

  input addInlineCommentInput {
    prId: ID!
    content: String!
    author: ID!
    fileId: ID!
    lineNum: Int!
  }

  input addReactionInput {
    commentId: ID!
    type: String!
    author: ID!
  }

  input removeReactionInput {
    reactionId: ID!
    user: ID!
  }

  input mergePullRequestInput {
    prId: ID!
  }

  input rejectPullRequestInput {
    prId: ID!
  }
`
;
