import requests
from github import Github


def login_github(token_file = "secret_token"):
    with open(token_file, 'r') as f:
        token = f.read()
    # strip the \n
    token = token.strip()
    g = Github(token)
    return g


def get_user_repo(g):
    repo = g.get_user().get_repos()
    return repo


def get_issues(repo_name):
    repo = g.get_repo(repo_name)
    open_issues = repo.get_issues(state='open')
    for issue in open_issues:
        print(issue)



if __name__ == "__main__":
    g = login_github()
    # repos = get_user_repo(g)

    # query moveit as an example
    # url: https://github.com/ros-planning/moveit
    repo_name = "ros-planning/moveit"
    get_issues(repo_name)

