enum Status {
  PENDING = 'PENDING',
  MERGE_CONFLICT = 'MERGE_CONFLICT',
  REJECTED = 'REJECTED',
  MERGED = 'MERGED',
}

export interface User {
  id: String;
  username: String;
  account: String;
}

export interface Line {
  id: String;
  lineNum: Number;
  content: String;
}

export interface ChangedFile {
  id: String;
  filename: String;
  changedLines: Line[];
}

export interface GeneralComment {
  id: String;
  content: String;
  author: User;
  reactions: Reaction[];
  reactionCount: Number;
}

export interface InlineComment {
  id: String;
  file: ChangedFile;
  line: Line;
  content: String;
  author: User;
  reactions: Reaction[];
  reactionCount: Number;
}

export interface Reaction {
  id: String;
  type: String;
  user: User;
}

export interface PullRequest {
  id: String;
  description: String;
  sourceCommit: String;
  targetBranch: String;
  status: Status;
  generalComments: GeneralComment[];
  inlineComments: InlineComment[];
}

export interface View {
  pullRequests: PullRequest;
  changedFiles: ChangedFile[];
}