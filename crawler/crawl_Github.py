import requests
from github import Github
import github
import sqlite3
from tqdm import tqdm
import time


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


def save_issue(issue, is_PR:int, fix_issue_id:int):
    # save the issue in a sqlite3 db. 
    # the db should have the following fields:
    # issue_id, is_PR, fix_issue_id, issue_title, issue_body, issue_comments, 

    # 1. create a db "issues.db" if not exist
    db = sqlite3.connect("issues.db")
    # 2. create a table "issues" if not exist
    db.execute('''CREATE TABLE IF NOT EXISTS issues
                (issue_id INTEGER PRIMARY KEY, is_PR INTEGER, fix_issue_id INTEGER, issue_title TEXT, issue_body TEXT, issue_comments TEXT)''')
    # 3. parse the required fields
    try:
        issue_id = int(issue.id)
        issue_title = str(issue.title)
        issue_body = str(issue.body)
        issue_comments = []
        for comment in issue.get_comments():
            issue_comments.append(str(comment.body))
        # 4. insert the issue into the db
        db.execute("INSERT INTO issues VALUES (?, ?, ?, ?, ?, ?)", (issue_id, is_PR, fix_issue_id, issue_title, issue_body, str(issue_comments)))
        db.commit()

    except Exception as e:
        print("Encountered exception when saving the issue: ", e)
        
    finally:
        db.close()

def issue_handler(issue):
    # the general strategy is to 
    pass


def get_issues(repo_name):
    repo = g.get_repo(repo_name)
    closed_issues = repo.get_issues(state='closed')

    for i in range(0, closed_issues.totalCount):
        try:
            issue = closed_issues[i]
            # Add a sleep to avoid rate limit. The rate-limit is 1000 requests per hour, so we sleep for 2s.
            time.sleep(2)
            # check if it is a PR
            linked_issue_number = None

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
                # print("PR: ", issue.as_pull_request())
                # print("Linked Issue: ", linked_issue)
                ## save both the PR and the linked issue
                save_issue(issue, 1, linked_issue_number)
                save_issue(linked_issue, 0, None)

        # Issue is not a PR
        except github.GithubException as e:
            # TODO: pass to the issue handler
            pass

        # Body does not contain valid information. Skip
        except AttributeError as e:
            pass

        # Rate limit exceeded. Sleep for 1 hr and continue
        except github.RateLimitExceededException as e:
            print("Rate limit exceeded. Sleeping for 1 hr...")
            time.sleep(3600)
            continue

        except Exception as e:
            print("Encountered exception: ", e)
            pass



if __name__ == "__main__":
    g = login_github()
    # repos = get_user_repo(g)

    source = "../scripts/robot_resources.txt"
    with open(source, 'r') as f:
        resources = f.readlines()
    
    # enumerate 0-70 from resources
    for i in range(30,70):
        resource = resources[i]
        resource_items = resource.split(" ")
        print("Processing resource: ",i, resource_items[0])
        print("resource_items: ", resource_items)
        if len(resource_items) != 2 and "none\n" not in resource_items: # this is labeled and valid
            repo_name = resource_items[0][19:] # after "https://github.com/"
            # repo_name = "ros-planning/moveit"
            get_issues(repo_name)

