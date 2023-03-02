import requests
from github import Github
import github


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
    closed_issues = repo.get_issues(state='closed')
    for issue in closed_issues:
        # check if it is a PR
        linked_issue_number = None
        try:
            PR = issue.as_pull_request()
            # check if it fixing an issue
            # the logic is to check if the PR body contains the issue number in the format of #<issue_number>
            issue_body_split = issue.body.split()
            # print(issue_body_split)
            for i in range(1,len(issue_body_split)):
                if issue_body_split[i].startswith("#"):
                    # check if the issue number point to a valid issue
                    linked_issue_number = issue_body_split[i][1:]
                    # check if issue number can be converted to int
                    try:
                        linked_issue_number = int(linked_issue_number)
                        linked_issue = repo.get_issue(number=linked_issue_number)
                        # if issue is valid, break the loop
                        break
                    except Exception as e:
                        # print(e)
                        linked_issue_number = None
                        continue
            if linked_issue_number is not None:
                print("PR: ", issue.as_pull_request())
                print("Linked Issue: ", linked_issue)
        
        # Issue is not a PR
        except github.GithubException as e:
            # TODO: pass to the issue handler
            pass

        # Body does not contain valid information. Skip
        except AttributeError as e:
            pass

        except Exception as e:
            print("Encountered exception: ", e)
            pass



if __name__ == "__main__":
    g = login_github()
    # repos = get_user_repo(g)

    # query moveit as an example
    # url: https://github.com/ros-planning/moveit
    repo_name = "ros-planning/moveit"
    get_issues(repo_name)

