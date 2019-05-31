import unittest
import subprocess
import os

class TestSamness(unittest.TestCase):
    def test_sameness(self):
        output = subprocess.run(['./SimilarPictureFinder.py', '--path', 'tests/test_same/'], stdout=subprocess.PIPE)
        output_text = output.stdout.decode('utf-8')
        output_second_line = output_text.split('\n')[1]
        output_third_line = output_text.split('\n')[2]
        unittest.TestCase.assertEqual(self, output_second_line, "image 1 duplicate.png image 1.png")
        unittest.TestCase.assertEqual(self, output_third_line, "image 2 appears like 1 but different.png")
