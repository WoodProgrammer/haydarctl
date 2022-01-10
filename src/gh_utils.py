import os
import logging
from git import Repo

class GithubUtils(object):
    def __init__(self):
        gh_token = os.environ["GH_TOKEN"]
        self.repo_pull_url = "https://{}:x-oauth-basic@github.com/".format(gh_token)

    def clone_repo(self, repo_addr, clone_to="/tmp/"):
        repo_url = "{}/{}".format(self.repo_pull_url, repo_addr)

        try:
            Repo.clone_from(repo_url, clone_to)
        except Exception as exp:
            logging.error(exp)
