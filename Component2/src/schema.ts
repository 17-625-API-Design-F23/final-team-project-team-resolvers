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

  enum Status {
    PENDING,
    MERGE_CONFLICT,
    REJECTED,
    MERGED,
  }

  type Query {
    pullRequests(status: Status, pageLimit: Int, offset: Int): [PullRequest]!
  }

  type Mutation {
    addPullRequest(description: String!, sourceCommit: String!, targetBranch: String!): PullRequest!
    addGeneralComment(prId: ID!, content: String!, author: ID!): GeneralComment!
    addInlineComment(prId: ID!, content: String!, author: ID!, fileId: ID!, lineNum: Int!): InlineComment!
    addReaction(commentId: ID!, type: String!, author: ID!): Reaction!
    removeReaction(reactionId: ID!, user: ID!): Reaction!
    mergePullRequest(prId: ID!): PullRequest!
    rejectPullRequest(prId: ID!): PullRequest!
  }
`
;
