import os
from dotenv import load_dotenv

load_dotenv()
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

print(GITHUB_TOKEN)
 

import requests
import base64

HEADERS = {
    "Authorization": f"Bearer {GITHUB_TOKEN}",
    "Accept": "application/vnd.github+json"
}

def extract_repo_data(owner: str, repo: str) -> dict:
    # 1️⃣ Repo metadata
    repo_url = f"https://api.github.com/repos/{owner}/{repo}"
    repo_data = requests.get(repo_url, headers=HEADERS).json()

    # 2️⃣ README
    readme_url = f"{repo_url}/readme"
    readme_resp = requests.get(readme_url, headers=HEADERS)

    readme_text = ""
    if readme_resp.status_code == 200:
        encoded = readme_resp.json().get("content", "")
        readme_text = base64.b64decode(encoded).decode("utf-8")

    return {
        "repository_name": repo_data.get("name"),
        "stars": repo_data.get("stargazers_count"),
        "forks": repo_data.get("forks_count"),
        "watchers": repo_data.get("subscribers_count"),
        "readme": readme_text
    }


data = extract_repo_data(
    owner="purvasawant-git",
    repo="trial"
)

print(data)
