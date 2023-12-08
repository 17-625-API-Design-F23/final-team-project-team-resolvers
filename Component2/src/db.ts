import {User, Line, ChangedFile, GeneralComment, InlineComment, Reaction, PullRequest} from './types.js';

enum Status {
  PENDING = 'PENDING',
  MERGE_CONFLICT = 'MERGE_CONFLICT',
  REJECTED = 'REJECTED',
  MERGED = 'MERGED',
}

const users: User[] = [
    { id: '1', username: 'user1', account: 'account1' },
    { id: '2', username: 'user2', account: 'account2' },
    { id: '3', username: 'user3', account: 'account3' },
    { id: '4', username: 'user4', account: 'account4' },
    // Add more user mock data
  ];

const reactions: Reaction[] = [
    { id: '1', type: 'thumbsUp', user: users[0] },
    { id: '2', type: 'smiley', user: users[1]},
    // Add more reaction mock data
  ];

const lines: Line[] = [
    {
      id: '1',
      lineNum: 10,
      content: 'Some code here',
    },
    {
      id: '2',
      lineNum: 20,
      content: 'Another line of code',
    },
  ];

const changedFiles: ChangedFile[] = [
    {
      id: '1',
      filename: 'file1.js',
      changedLines: [
        lines[0],
        // Add more changed line mock data for file1.js
      ],
    },
    // Add more changed file mock data
  ];

const generalComments: GeneralComment[] = [
    { id: '1', content: 'This is a general comment', author: users[0], reactions: [reactions['1']], reactionCount: reactions.length },
    // Add more general comment mock data
  ];

const inlineComments: InlineComment[] = [
    {
      id: '1',
      file: changedFiles[0], 
      line: changedFiles[0]['changedLines'][0], 
      content: 'This is an inline comment',
      author: users[0],
      reactions: [reactions['3'], reactions['4']],
      reactionCount: reactions.length,
    },
    // Add more inline comment mock data
  ];

const pullRequests: PullRequest[] = [
    {
      id: '1',
      description: 'Fix some issues',
      sourceCommit: '12H3J4',
      targetBranch: 'main',
      status: Status.PENDING,
      generalComments: [generalComments['1']],
      inlineComments: [inlineComments['1']],
    },
    {
      id: '2',
      description: 'Add new feature',
      sourceCommit: '0B324F',
      targetBranch: 'main',
      status: Status.MERGE_CONFLICT,
      generalComments: [],
      inlineComments: [],
    },
    {
      id: '3',
      description: 'Fix some issues',
      sourceCommit: '5DFG34',
      targetBranch: 'main',
      status: Status.REJECTED,
      generalComments: [],
      inlineComments: [],
    },
    {
      id: '4',
      description: 'Add new feature',
      sourceCommit: '9WR234',
      targetBranch: 'main',
      status: Status.MERGED,
      generalComments: [],
      inlineComments: [],
    },
  ];

export {users, reactions, lines, changedFiles, generalComments, inlineComments, pullRequests};
