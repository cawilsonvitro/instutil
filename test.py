import git
import datetime as dt
import fpdf
from zoneinfo import ZoneInfo
import win32com.client as win32
import os

# path = os.getcwd()
# path = os.path.join(path, "git_weekly_report_gen",reports_dir := "reports")
path = r"C:\Users\C376038\Documents\python_code\packages\git_weekly_report_gen\reports"



def weekly_report(path_to_repo, end, start, updates = []):
    """
    Generates a weekly report of git commits within a specified date range.
    Args:
        path_to_repo (str): Path to the local git repository.
        end (datetime): The end datetime for the report range.
        start (datetime): The start datetime for the report range.
        updates (list, optional): List to append commit messages to. Defaults to an empty list.
    Returns:
        str: A newline-separated string of commit messages within the specified date range.
    Side Effects:
        Prints commit details (hexsha, author, date, message) to the console for each commit in the range.
    """

    repo = git.Repo(path_to_repo)
    repo_name = repo.remotes.origin.url.split('.git')[0].split('/')[-1]
    print(repo_name)
    updates.append(f"{repo_name} Weekly Report\n")
    # end = dt.datetime.now(ZoneInfo('EST'))
    # start = end - dt.timedelta(days=5)
    i = 0
    for commit in repo.iter_commits():
        commit_time = commit.committed_datetime
        if commit_time > start and commit_time < end:
            update = f"\t{i}. {commit.message.strip()}"
            updates.append(update)

            # print(f"Commit: {commit.hexsha}")
            # print(f"Author: {commit.author.name} <{commit.author.email}>")
            # print(f"Date: {commit.committed_datetime}")
            # print(f"Message: {commit.message.stri()}")
            # print("-" * 40)
            
            i += 1
            
        
    updates_as_str = ("\n").join(updates)
    

    return updates_as_str

txt = weekly_report(
    path_to_repo="C:/Users/C376038/Documents/inst_suite/python/inst_code/.git",
    end=dt.datetime.now(ZoneInfo('EST')),
    start=dt.datetime.now(ZoneInfo('EST')) - dt.timedelta(days=7)
)
print(txt)

def create_report_and_email(path, txt, email_list):
    time = str(dt.datetime.now(ZoneInfo('EST')).strftime("%Y-%m-%d"))
    with open(f"{path}/{time} report.txt", "+w") as f:
        print(txt)
        f.write(txt)
    
    outlook = win32.Dispatch('outlook.application')
    mail = outlook.CreateItem(0)
    mail.To = (",").join(email_list)
    mail.Body = txt
    mail.Send()



# create_report_and_email(path, txt)


repos = [
    "C:/Users/C376038/Documents/python_code/packages/instutil_pak",
    "C:/Users/C376038/Documents/inst_suite/python/inst_code"
]

# txt = weekly_report(
#     path_to_repo="C:/Users/C376038/Documents/python_code/packages/instutil_pak",
#     end=dt.datetime.now(ZoneInfo('EST')),
#     start=dt.datetime.now(ZoneInfo('EST')) - dt.timedelta(days=7)
# )
# print(txt)


# for repo in repos:
#     txt = weekly_report(
#         path_to_repo=repo,
#         end=dt.datetime.now(ZoneInfo('EST')),
#         start=dt.datetime.now(ZoneInfo('EST')) - dt.timedelta(days=7)
#     )
#     print(txt)


git.Repo(r"C:/Users/C376038/Documents/python_code/packages/instutil_pak")