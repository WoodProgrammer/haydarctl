import glob
import unittest
from src.gh_utils import *
from tests.utils import check_file
class TestGhUtils(unittest.TestCase):

    def test_gh_clone(self):
        gh_obj = GithubUtils()
        gh_obj.clone_repo(repo_addr="WoodProgrammer/infra_hede", clone_to="haydar-workspace")

        status = check_file("haydar-workspace/infra_hede")
        
        self.assertEqual(status, False)