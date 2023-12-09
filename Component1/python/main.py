from fastapi import FastAPI, HTTPException
from typing import List, Dict, Optional
from repository import Repository
from branch import Branch
from commit import Commit
from issue import Issue
from comment import Comment


app = FastAPI()

fake_comments = [Comment(user_id="user1", date="2023-01-01", content="Wrong format."),
    Comment(user_id="user2", date="2023-01-02", content="Good job.")]

fake_issues = [Issue(issue_id="issue_1", user_id="user1", status="Open", description="java problem", date="2024-01-01", comments=fake_comments),
    Issue(issue_id="issue_2", user_id="user2", status="Closed", description="Python problem", date="2024-01-02", comments=[])]

fake_commits1 = [Commit(commit_hash="commit_1", tags=["python", "17625"], user_id="user1", dir={"scr/temp.py":["python"]}),
                Commit(commit_hash="commit_2", tags=["java", "17625"], user_id="user2", dir={"scr/temp.java":["java"]})]
fake_commits2 = [Commit(commit_hash="commit_1", tags=["python"], user_id="user1", dir={"scr/temp.py":["python"], "scr":["main.py"]}),
                Commit(commit_hash="commit_2", tags=["java"], user_id="user2", dir={"scr/temp.java":["java"]})]
fake_commits3 = [Commit(commit_hash="commit_1", tags=["cpp", "17625"], user_id="user3", dir={"scr/temp.cpp":["cpp"]})]

branch1 = Branch(branch_id = "branch_1", commits = fake_commits1)
branch2 = Branch(branch_id = "branch_2", commits = fake_commits2)
branch3 = Branch(branch_id = "branch_3", commits = fake_commits3)

fake_repos = [Repository(repo_id = "repo_1", branches = [branch1, branch2], tags = ["python", "17625", "java"], issues= fake_issues),
              Repository(repo_id = "repo_2", branches = [branch3], tags = ["python", "17625", "java"], issues=[])]


@app.get("/repo/{repository_id}/main/commit/{commit_hash}", status_code=200)
@app.get("/repo/{repository_id}/main/commit")
def get_commit(repository_id: str, commit_hash: Optional[str] = None):
    fake_commits = None
    for repo in fake_repos:
        if repo.repo_id == repository_id:
            fake_commits = repo.branches[0].commits
    if fake_commits == None:
        raise HTTPException(status_code=400, detail="Repository not found!")
    if commit_hash == None:
        return {"Commit hash: " + fake_commits[0].commit_hash + ", "
                    + "Tags: " + ", ".join(fake_commits[0].tags) + ", "
                    + "Submitter: " + fake_commits[0].user_id + ", "
                    + "Directory: " + ', '.join(fake_commits[0].dir.keys())}
    else:
        #check if the commit exists
        #if exist, navigate to the commit
        for commit in fake_commits1:
            if commit.commit_hash == commit_hash:
                chosen_commit = commit
                return {"Commit hash: " + chosen_commit.commit_hash + ", "
                        + "Tags: " + ", ".join(chosen_commit.tags) + ", "
                        + "Submitter: " + chosen_commit.user_id + ", "
                        + "Directory: " + ', '.join(chosen_commit.dir.keys())}
        raise HTTPException(status_code=400, detail="Commit not found!")
        
@app.get("/repo/{repository_id}/branches", status_code=200)
def get_branches(repository_id: str):
    for repo in fake_repos:
        if repo.repo_id == repository_id:
            fake_branches= [b.branch_id for b in repo.branches]
            return {"Branches: " + ', '.join(fake_branches)}
    raise HTTPException(status_code=400, detail="Repository not found!")
    
@app.get("/repo/{repository_id}/tags", status_code=200)
def get_tags(repository_id: str):
    for repo in fake_repos:
        if repo.repo_id == repository_id:
            fake_tags= repo.tags
            return {"Tags: " + ', '.join(fake_tags)}
    raise HTTPException(status_code=400, detail="Repository not found!")

@app.get("/repo/{repository_id}/branch/{branch_id}/commits", status_code=200)
def get_commits(repository_id: str, branch_id: str):
    fake_branches = None
    for repo in fake_repos:
        if repo.repo_id == repository_id:
            fake_branches = repo.branches
    if fake_branches == None:
        raise HTTPException(status_code=400, detail="Repository not found!")
    fake_commits = None
    for branch in fake_branches:
        if branch.branch_id == branch_id:
            fake_commits = branch.commits
            commits_info = []
            for commit in fake_commits:
                commits_info.append(f"Commit hash: {commit.commit_hash}, "
                f"Tags: {', '.join(commit.tags)}, "
                f"Submitter: {commit.user_id}, "
                f"Directory: {', '.join(commit.dir.keys())}")
            return {"Commits": commits_info}
    raise HTTPException(status_code=400, detail="Branch not found!")

@app.get("/repo/{repository_id}/branch/{branch_id}/commits/{commit_hash}", status_code=200)
def get_tree(repository_id: str, branch_id: str, commit_hash: str):
    fake_branches = None
    for repo in fake_repos:
        if repo.repo_id == repository_id:
            fake_branches = repo.branches
    if fake_branches == None:
        raise HTTPException(status_code=400, detail="Repository not found!")
    fake_commits = None
    for branch in fake_branches:
        if branch.branch_id == branch_id:
            fake_commits = branch.commits
    if fake_commits == None:
        raise HTTPException(status_code=400, detail="Branch not found!")
    for commit in fake_commits:
        if commit.commit_hash == commit_hash:
            return {"Top level tree: " + "Directory: " + ', '.join(commit.dir.keys())}
    raise HTTPException(status_code=400, detail="Commit not found!")

@app.get("/repo/{repo_id}/branch/{branch_id}/commit/{commit_hash}/blob/{blob_dir:path}", status_code=200)
def get_blob(repo_id: str, branch_id: str, commit_hash: str, blob_dir: str):
    for repo in fake_repos:
        if repo.repo_id == repo_id:
            for branch in repo.branches:
                if branch.branch_id == branch_id:
                    for commit in branch.commits:
                        if commit.commit_hash == commit_hash:
                            if blob_dir in commit.dir.keys():
                                return {"Blob content" + ', '.join(commit.dir[blob_dir])}
                            else:
                                raise HTTPException(status_code=400, detail="Blob not found!")
                    raise HTTPException(status_code=400, detail="Commit not found!")
            raise HTTPException(status_code=400, detail="Branch not found!")
    raise HTTPException(status_code=400, detail="Repository not found!")

@app.get("/repo/{repository_id}/branch/{branch_id}/tree/commit/{commit_id}/{dir:path}", status_code=200)
def get_subtree(repository_id: str, branch_id: str, commit_id: str, dir: str):
    for repo in fake_repos:
        if repo.repo_id == repository_id:
            for branch in repo.branches:
                if branch.branch_id == branch_id:
                    for commit in branch.commits:
                        if commit.commit_hash == commit_id:
                            if dir in commit.dir:
                                return {"Subtree content: " + ', '.join(commit.dir[dir])}
                            else:
                                raise HTTPException(status_code=400, detail="Directory not found!")
                    raise HTTPException(status_code=400, detail="Commit not found!")
            raise HTTPException(status_code=400, detail="Branch not found!")
    raise HTTPException(status_code=400, detail="Repository not found!")

@app.get("/repo/{repository_id}/issues", status_code=200)
def list_issues(repository_id: str, status: str, page_size: int, page_number: int):
    if repository_id not in [repo.repo_id for repo in fake_repos]:
        raise HTTPException(status_code=400, detail="Repository not found!")
    for repo in fake_repos:
        if repo.repo_id == repository_id:
            fake_repo = repo
    fake_issues = fake_repo.issues
    if status not in ["Open", "Closed"]:
        raise HTTPException(status_code=400, detail="Status not found!")
    issues = [issue for issue in fake_issues if issue.status == status]
    show_start = (page_number - 1) * page_size
    show_end = show_start + page_size
    if show_start >= len(issues):
        raise HTTPException(status_code=400, detail="Invalid pagination!")
    if show_end >len(issues):
        show_end = len(issues)
    page_issues = issues[show_start:show_end]
    show_issues = []
    for issue in page_issues:
        show_issues.append(f"Issue ID: {issue.issue_id}, " 
                           + f"Submitter ID: {issue.user_id}, " 
                           + f"Status: {issue.status}")
    return {"Issues: ": show_issues}

@app.post("/repo/{repository_id}/issues", status_code=201)
def report_issue(repository_id: str, issue_description: str, issue_date: str, submitter_id: str, status: Optional[str] = None):
    if repository_id not in [repo.repo_id for repo in fake_repos]:
        raise HTTPException(status_code=400, detail="Repository not found!")
    for repo in fake_repos:
        if repo.repo_id == repository_id:
            fake_repo = repo
    if status == None:
        fake_status = "Open"
    elif status not in ["Open", "Closed"]:
        raise HTTPException(status_code=400, detail="Issue status not found!")
    else:
        fake_status = status
    new_issue = Issue(issue_id="Issue_"+str(len(fake_issues)), user_id=submitter_id, 
                      status=fake_status,description=issue_description, 
                      date=issue_date,comments=[])
    fake_repo.issues.append(new_issue)
    return {"New Issue: " + str(new_issue.issue_id)}

@app.get("/repo/{repository_id}/issues/{issue_id}", status_code=200)
def view_issues(repository_id: str, issue_id: str, page_size: int):
    if repository_id not in [repo.repo_id for repo in fake_repos]:
        raise HTTPException(status_code=400, detail="Repository not found!")
    for repo in fake_repos:
        if repo.repo_id == repository_id:
            fake_repo = repo
    if issue_id not in [issue.issue_id for issue in fake_repo.issues]:
        raise HTTPException(status_code=400, detail="Issue not found!")
    for issue in fake_repo.issues:
        if issue.issue_id == issue_id:
            fake_issue = issue
    fake_comment = fake_issue.comments
    show_start = 0
    show_end = show_start + page_size
    if show_end >=len(fake_comment):
        show_end = len(fake_comment) - 1
    page_comment = fake_comment[show_start:show_end]
    show_comment = []
    for cmt in page_comment:
        show_comment.append(f"Date: {cmt.date}, " + 
                           f"Submitter ID: {cmt.user_id}, " + 
                           f"Content: {cmt.content}")
    return [f"Issue ID: {issue.issue_id}, " 
            + f"Submitter ID: {issue.user_id}, " 
            + f"Status: {issue.status}, " 
            + f"Comment: {show_comment}"]


@app.get("/repo/{repository_id}/issues/{issue_id}/comments", status_code=200)
def view_comments(repository_id: str, issue_id: str, page_size: int, page_number: int):
    if repository_id not in [repo.repo_id for repo in fake_repos]:
        raise HTTPException(status_code=400, detail="Repository not found!")
    for repo in fake_repos:
        if repo.repo_id == repository_id:
            fake_repo = repo
    if issue_id not in [issue.issue_id for issue in fake_repo.issues]:
        raise HTTPException(status_code=400, detail="Issue not found!")
    for issue in fake_repo.issues:
        if issue.issue_id == issue_id:
            fake_issue = issue
    fake_comment = fake_issue.comments
    show_start = (page_number - 1) * page_size
    show_end = show_start + page_size
    if show_start >= len(fake_comment):
        raise HTTPException(status_code=400, detail="Invalid pagination!")
    if show_end >= len(fake_comment):
        show_end = len(fake_comment) - 1
    page_comment = fake_comment[show_start:show_end]
    show_comment = []
    for cmt in page_comment:
        show_comment.append(f"Date: {cmt.date}, " 
                           + f"Submitter ID: {cmt.user_id}, " 
                           + f"Content: {cmt.content}")
    return {"Comment": show_comment}

@app.post("/repo/{repository_id}/issues/{issue_id}/comments", status_code=201)
def submit_comment(repository_id: str, issue_id: str, submitter_id: str, comment_content: str, comment_date: str):
    if repository_id not in [repo.repo_id for repo in fake_repos]:
        raise HTTPException(status_code=400, detail="Repository not found!")
    for repo in fake_repos:
        if repo.repo_id == repository_id:
            fake_repo = repo
    if issue_id not in [issue.issue_id for issue in fake_repo.issues]:
        raise HTTPException(status_code=400, detail="Issue not found!")
    for issue in fake_repo.issues:
        if issue.issue_id == issue_id:
            fake_issue = issue
    new_comment = Comment(user_id=submitter_id, date=comment_date, content=comment_content)
    fake_issue.comments.append(new_comment)
    return {"Comment successfully " 
            + f"Comment user: {new_comment.user_id}, "
            + f"Comment date: {new_comment.date}, "
            + f"Content: {new_comment.content}"}