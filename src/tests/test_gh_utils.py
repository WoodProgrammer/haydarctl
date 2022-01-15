import glob
import unittest
from src.gh_utils import *
from src.tests.utils import check_file
class TestGhUtils(unittest.TestCase):

    def test_gh_clone(self):
        gh_obj = GithubUtils()
        gh_obj.clone_repo(repo_addr="WoodProgrammer/infra_hede", clone_to="/tmp")

        status = check_file("/tmp/infra_hede")
        
        self.assertEqual(status, False)