import unittest
import subprocess
import os

class TestCosoleInput(unittest.TestCase):
    def test_path(self):
        output = subprocess.run(['./SimilarPictureFinder.py', '--path', 'a_path/to/folder_with_images'], stdout=subprocess.PIPE)
        output_text = output.stdout.decode('utf-8')
        output_first_line = output_text.split('\n')[0]
        project_folder_path = os.getcwd()
        unittest.TestCase.assertEqual(self, output_first_line, 'Full path is: %s/a_path/to/folder_with_images' % project_folder_path)
