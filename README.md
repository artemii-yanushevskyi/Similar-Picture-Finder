# Similar Image Finder
__A console tool which finds similar images in a given folder and prints similar pairs.__

# Mini Scrum

* Project layout
    * Make `source` folder stucture
    * Create virtual environment `env`
    * Create `SimilarPictureFinder.py` and make it executable\* 
    * Test it using bash script `./SimilarPictureFinder.py testinput`, should output `['./SimilarPictureFinder.py', 'testinput']`
* Command line input processing
    * Write function `dispatch` using Argparse module that has the following functionality
        * throws an error if there is folder path missing
        * returns the folder path if present
    * Tests for function `dispatch`
* Learning to operate with images
    * Image to numpy array
    * Viewing and saving numpy array as an image
* Find same images
    * Write pixel by pixel comparison
    * Test on the dataset `test_same`

\* first line of the file should be `#! env/bin/python` and run `chmod +x SimilarPictureFinder.py`

