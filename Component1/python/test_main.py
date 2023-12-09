from main import app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_get_index():
    """
    Test default mode of get index.
    """
    response = client.get('/repo/repo_1/main/commit')
    assert response.status_code == 200
    except_data = [
        "Commit hash: commit_1, Tags: python, 17625, Submitter: user1, Directory: scr/temp.py"
    ]
    assert except_data == response.json()

def test_get_index_with_commit_hash():
    """
    Test get index with commit hash.
    """
    response = client.get('/repo/repo_1/main/commit?commit_hash=commit_2')
    assert response.status_code == 200
    except_data = [
        "Commit hash: commit_2, Tags: java, 17625, Submitter: user2, Directory: scr/temp.java"
    ]
    assert except_data == response.json()

def test_get_index_negative():
    """
    Test get index with commit hash.
    """
    response = client.get('/repo/repo_1/main/commit?commit_hash=commit_3')
    assert response.status_code == 400
    except_data = {
        "detail": "Commit not found!"
    }
    assert except_data == response.json()

def test_get_branches():
    """
    Test get branches.
    """
    response = client.get('/repo/repo_1/branches')
    assert response.status_code == 200
    except_data = [
        "Branches: branch_1, branch_2"
    ]
    assert except_data == response.json()

def test_get_branches_negative():
    """
    Test get branches.
    """
    response = client.get('/repo/repo_3/branches')
    assert response.status_code == 400
    except_data = {
        "detail": "Repository not found!"
    }
    assert except_data == response.json()

def test_get_tags():
    """
    Test get tags.
    """
    response = client.get('/repo/repo_1/tags')
    assert response.status_code == 200
    except_data = [
        "Tags: python, 17625, java"
    ]
    assert except_data == response.json()

def test_get_tags_negative():
    """
    Test get tags.
    """
    response = client.get('/repo/repo_3/tags')
    assert response.status_code == 400
    except_data = {
        "detail": "Repository not found!"
    }
    assert except_data == response.json()

def test_get_commits():
    """
    Test get commits.
    """
    response = client.get('/repo/repo_1/branch/branch_1/commits')
    assert response.status_code == 200
    except_data = {"Commits": [
        "Commit hash: commit_1, Tags: python, 17625, Submitter: user1, Directory: scr/temp.py",
        "Commit hash: commit_2, Tags: java, 17625, Submitter: user2, Directory: scr/temp.java"
    ]}
    assert except_data == response.json()

def test_get_commits_repo_negative():
    """
    Test get tags.
    """
    response = client.get('/repo/repo_3/branch/branch_1/commits')
    assert response.status_code == 400
    except_data = {
        "detail": "Repository not found!"
    }
    assert except_data == response.json()

def test_get_commits_branch_negative():
    """
    Test get tags.
    """
    response = client.get('/repo/repo_1/branch/branch_3/commits')
    assert response.status_code == 400
    except_data = {
        "detail": "Branch not found!"
    }
    assert except_data == response.json()

def test_get_tree():
    """
    Test get tree.
    """
    response = client.get('/repo/repo_1/branch/branch_1/commits/commit_1')
    assert response.status_code == 200
    except_data = ["Top level tree: " + "Directory: scr/temp.py"]
    assert except_data == response.json()

def test_get_tree_repo_negative():
    """
    Test get tags.
    """
    response = client.get('/repo/repo_3/branch/branch_1/commits/commit_1')
    assert response.status_code == 400
    except_data = {
        "detail": "Repository not found!"
    }
    assert except_data == response.json()

def test_get_tree_branch_negative():
    """
    Test get tags.
    """
    response = client.get('/repo/repo_1/branch/branch_3/commits/commit_1')
    assert response.status_code == 400
    except_data = {
        "detail": "Branch not found!"
    }
    assert except_data == response.json()

def test_get_tree_commit_negative():
    """
    Test get tags.
    """
    response = client.get('/repo/repo_1/branch/branch_1/commits/commit_3')
    assert response.status_code == 400
    except_data = {
        "detail": "Commit not found!"
    }
    assert except_data == response.json()

def test_get_blob():
    """
    Test get blob.
    """
    response = client.get('/repo/repo_1/branch/branch_1/commit/commit_1/blob/scr/temp.py')
    assert response.status_code == 200
    except_data = ["Blob content" + "python"]
    assert except_data == response.json()

def test_get_blob_repo_negative():
    """
    Test get tags.
    """
    response = client.get('/repo/repo_3/branch/branch_1/commit/commit_1/blob/scr/temp.py')
    assert response.status_code == 400
    except_data = {
        "detail": "Repository not found!"
    }
    assert except_data == response.json()

def test_get_blob_branch_negative():
    """
    Test get tags.
    """
    response = client.get('/repo/repo_1/branch/branch_3/commit/commit_1/blob/scr/temp.py')
    assert response.status_code == 400
    except_data = {
        "detail": "Branch not found!"
    }
    assert except_data == response.json()

def test_get_blob_commit_negative():
    """
    Test get tags.
    """
    response = client.get('/repo/repo_1/branch/branch_1/commit/commit_3/blob/scr/temp.py')
    assert response.status_code == 400
    except_data = {
        "detail": "Commit not found!"
    }
    assert except_data == response.json()

def test_get_blob_path_negative():
    """
    Test get tags.
    """
    response = client.get('/repo/repo_1/branch/branch_1/commit/commit_1/blob/scr/temp.java')
    assert response.status_code == 400
    except_data = {
        "detail": "Blob not found!"
    }
    assert except_data == response.json()

def test_get_subtree():
    """
    Test get subtree.
    """
    response = client.get('/repo/repo_1/branch/branch_2/tree/commit/commit_1/scr')
    assert response.status_code == 200
    except_data = ["Subtree content: " + "main.py"]
    assert except_data == response.json()

def test_get_subtree_repo_negative():
    """
    Test get tags.
    """
    response = client.get('/repo/repo_3/branch/branch_2/tree/commit/commit_1/scr')
    assert response.status_code == 400
    except_data = {
        "detail": "Repository not found!"
    }
    assert except_data == response.json()

def test_get_subtree_branch_negative():
    """
    Test get tags.
    """
    response = client.get('/repo/repo_1/branch/branch_3/tree/commit/commit_1/scr')
    assert response.status_code == 400
    except_data = {
        "detail": "Branch not found!"
    }
    assert except_data == response.json()

def test_get_subtree_commit_negative():
    """
    Test get tags.
    """
    response = client.get('/repo/repo_1/branch/branch_2/tree/commit/commit_3/scr')
    assert response.status_code == 400
    except_data = {
        "detail": "Commit not found!"
    }
    assert except_data == response.json()

def test_get_subtree_path_negative():
    """
    Test get tags.
    """
    response = client.get('/repo/repo_1/branch/branch_2/tree/commit/commit_2/scr/temp.py')
    assert response.status_code == 400
    except_data = {
        "detail": "Directory not found!"
    }
    assert except_data == response.json()

def test_list_issue():
    """
    Test list issue.
    """
    response = client.get('/repo/repo_1/issues?status=Open&page_size=2&page_number=1')
    assert response.status_code == 200
    except_data = {"Issues: ": ["Issue ID: issue_1, Submitter ID: user1, Status: Open"]}
    assert except_data == response.json()

def test_list_issue_repo_negative():
    """
    Test get tags.
    """
    response = client.get('/repo/repo_3/issues?status=Open&page_size=2&page_number=1')
    assert response.status_code == 400
    except_data = {
        "detail": "Repository not found!"
    }
    assert except_data == response.json()

def test_list_issue_status_negative():
    """
    Test get tags.
    """
    response = client.get('/repo/repo_1/issues?status=Close&page_size=2&page_number=1')
    assert response.status_code == 400
    except_data = {
        "detail": "Status not found!"
    }
    assert except_data == response.json()

def test_list_issue_page_negative():
    """
    Test get tags.
    """
    response = client.get('/repo/repo_1/issues?status=Open&page_size=3&page_number=2')
    assert response.status_code == 400
    except_data = {
        "detail": "Invalid pagination!"
    }
    assert except_data == response.json()

def test_report_issue():
    """
    Test report issue.
    """
    response = client.post('/repo/repo_1/issues?issue_description=Issue1&issue_date=2022-01-01&submitter_id=user_1&status=Open')
    print(response)
    assert response.status_code == 201
    except_data = ["New Issue: Issue_2"]
    assert except_data == response.json()

def test_report_issue_repo_negative():
    """
    Test get tags.
    """
    response = client.post('/repo/repo_3/issues?issue_description=Issue1&issue_date=2022-01-01&submitter_id=user_1&status=Open')
    assert response.status_code == 400
    except_data = {
        "detail": "Repository not found!"
    }
    assert except_data == response.json()

def test_report_issue_status_negative():
    """
    Test get tags.
    """
    response = client.post('/repo/repo_1/issues?issue_description=Issue1&issue_date=2022-01-01&submitter_id=user_1&status=Close')
    assert response.status_code == 400
    except_data = {
        "detail": "Issue status not found!"
    }
    assert except_data == response.json()

def test_view_issue():
    """
    Test view issue.
    """
    response = client.get('/repo/repo_1/issues/issue_1?page_size=2')
    assert response.status_code == 200
    except_data = ["Issue ID: Issue_2, Submitter ID: user_1, Status: Open, Comment: ['Date: 2023-01-01, Submitter ID: user1, Content: Wrong format.']"]
    assert except_data == response.json()

def test_view_issue_repo_negative():
    """
    Test get tags.
    """
    response = client.get('/repo/repo_3/issues/issue_1?page_size=2')
    assert response.status_code == 400
    except_data = {
        "detail": "Repository not found!"
    }
    assert except_data == response.json()

def test_view_issue_issue_negative():
    """
    Test get tags.
    """
    response = client.get('/repo/repo_1/issues/issue_3?page_size=2')
    assert response.status_code == 400
    except_data = {
        "detail": "Issue not found!"
    }
    assert except_data == response.json()

def test_view_comments():
    """
    Test view comments.
    """
    response = client.get('/repo/repo_1/issues/issue_1/comments?page_size=2&page_number=1')
    assert response.status_code == 200
    except_data = {"Comment": ["Date: 2023-01-01, Submitter ID: user1, Content: Wrong format."]}
    assert except_data == response.json()

def test_view_comments_repo_negative():
    """
    Test get tags.
    """
    response = client.get('/repo/repo_3/issues/issue_1/comments?page_size=2&page_number=1')
    assert response.status_code == 400
    except_data = {
        "detail": "Repository not found!"
    }
    assert except_data == response.json()

def test_view_comments_issue_negative():
    """
    Test get tags.
    """
    response = client.get('/repo/repo_1/issues/issue_3/comments?page_size=2&page_number=1')
    assert response.status_code == 400
    except_data = {
        "detail": "Issue not found!"
    }
    assert except_data == response.json()

def test_submit_comment():
    """
    Test submit comment.
    """
    response = client.post('/repo/repo_1/issues/issue_1/comments?comment_date=2023-01-01&submitter_id=user1&comment_content=Wrong format.')
    assert response.status_code == 201
    #except_data = ["New comment: Date: 2023-01-01, Submitter ID: user1, Content: Wrong format."]
    except_data = [
        "Comment successfully Comment user: user1, Comment date: 2023-01-01, Content: Wrong format."
    ]
    assert except_data == response.json()

def test_submit_comment_repo_negative():
    """
    Test get tags.
    """
    response = client.post('/repo/repo_3/issues/issue_1/comments?comment_date=2023-01-01&submitter_id=user1&comment_content=Wrong format.')
    assert response.status_code == 400
    except_data = {
        "detail": "Repository not found!"
    }
    assert except_data == response.json()

def test_submit_comment_issue_negative():
    """
    Test get tags.
    """
    response = client.post('/repo/repo_1/issues/issue_3/comments?comment_date=2023-01-01&submitter_id=user1&comment_content=Wrong format.')
    assert response.status_code == 400
    except_data = {
        "detail": "Issue not found!"
    }
    assert except_data == response.json()
