
import unittest

from CA5 import *

class TestCommits(unittest.TestCase):

    def setUp(self):
		self.data = Commit()

    def test_number_of_commits(self):
        self.assertEqual(422, len(commits))

    def test_first_commit(self):
        self.assertEqual('Thomas', commits[0].author)
        self.assertEqual(1551925, commits[0].revision)
	
	def test_average_commits(commits,authors):
		assertEqual(42,len(commits)[len(authors)])

	def test_maximum(commits_author):
		assertEqual(91,commits_author)
	
	def test_dates_min(dates):
		assertEqual("2015-07-13 09:21:48 +0100 (Mon, 13 Jul 2015)", dates) 
	
	def test_dates_max(dates):
		assertEqual("20-15-11-27 16:57:44 +0000 (Fri, 27 Nov 2015)", dates) 

if __name__ == '__main__':
    unittest.main()
