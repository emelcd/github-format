import datetime
from pprint import pprint as print
from time import sleep
import requests
from dotenv import load_dotenv

load_dotenv()

GITHUB_USER = "emelcd"


list_to_delete = ["shitty-repo", "shitty-repo-2"]

list_to_update = [
    {
        "repo": "portfolio",
        "name": "old-portfolio-v5",
        "description": "👩‍💻 Portfolio App | WebApp React",
        "is_public": False,
    },
]


def delete_repo(repo_name, file):
    url = f"https://api.github.com/repos/{GITHUB_USER}/{repo_name}"
    headers = {"Authorization": f"Bearer {TOKEN}"}
    r = requests.delete(url, headers=headers)

    if r.status_code == 204:
        file.write(f"{repo_name} deleted\n")
    else:
        file.write(f"{repo_name} not deleted\n")

    print(repo_name)


def update_repo(repo, name, description, is_public, file):
    url = f"https://api.github.com/repos/{GITHUB_USER}/{repo}"
    headers = {
        "Authorization": f"token {TOKEN}",
        "Accept": "application/vnd.github.v3+json",
        "Content-Type": "application/json",
    }
    payload = {
        "name": name,
        "description": description,
        "private": not is_public,
    }
    r = requests.patch(url, headers=headers, json=payload)

    if r.status_code == 200:
        file.write(f"{repo} updated\n")
    else:
        file.write(f"{repo} not updated\n")

    print(repo)


if __name__ == "__main__":
    TOKEN = input("Enter your token: ")
    with open("log.txt", "a") as file:
        file.write(f"{datetime.datetime.now()}\n")
        for repo in list_to_delete:
            delete_repo(repo, file)
            sleep(1)
        for repo in list_to_update:
            update_repo(
                repo["repo"], repo["name"], repo["description"], repo["is_public"], file
            )
            sleep(1)
