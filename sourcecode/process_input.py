import sys
import os
from argparse import ArgumentParser

def get_folder_path():
    parser = ArgumentParser(description='First test task on images similarity.')
    parser.add_argument('--path', help="Path to the folder with images, this argument is required", required=True)
    args = parser.parse_args()
    # returning the path to image folder, could be either absolute or relative
    print('Full path is: ' + os.path.join(os.getcwd(), args.path))
    return os.path.join(os.getcwd(), args.path)

