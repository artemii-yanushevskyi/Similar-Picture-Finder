# Similar Image Finder

A console application that finds duplicate photos in a given directory.

# Usage

    ./SimilarPictureFinder.py --path path/to/image_dir

# Mini Scrum

* Project layout
    * Make `source` folder stucture
    * Create virtual environment `env`
    * Create `SimilarPictureFinder.py` and make it executable\* 
    * Test it using bash script `./SimilarPictureFinder.py testinput`, should output `['./SimilarPictureFinder.py', 'testinput']`
* Command line input processing
    * Write function `get_folder_path` using Argparse module that has the following functionality
        * throws an error if there is folder path missing
        * returns the folder path if present
    * Test function `get_folder_path`
* Learning to operate with images
    * Image to numpy array
    * Viewing and saving numpy array as an image
* Find same images
    * Write pixel by pixel comparison
    * Test on the dataset `test_same`
* Image Convolutions
    * Blur


\* first line of the file should be `#! env/bin/python` and run `chmod +x SimilarPictureFinder.py`

# Deployment

Create virtual environment

    python3.7 -m virtualenv env
    source env/bin/activate
    # check
    python --version
    # should be 3.7
    # restore requirements
    pip install -r requirements.txt

Test the package

    python -m unittest discover tests
    
    
# To Do

* Finding modified photos. Apply the following, one after another 
    * Resized - easy
    * Blurred - use the Steepest Descent method on the Blur Value. Discovering if it is possible to “approximate” one image to another.
    * Noise - try to blur both images and apply previous step.
* Similar (from the same scene)
    * Apply some metrics based on number of features matched
    * Gradient descent on scale, vertical and horizontal rotation, x and y shift, and angle rotation. Perhaps some other parameters.
