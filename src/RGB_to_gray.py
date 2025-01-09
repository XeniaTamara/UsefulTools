
# Libraries
import os 
import matplotlib.pyplot as plt
from tiffile import imread
from skimage import io
from skimage.io import imsave
from skimage.color import rgb2gray
#from pathlib import Path
import argparse
import glob


def getOptions():
    """
    Function to pull in arguments for input and output paths.
    """
    description = """ Convert RGB images to grayscale and save them. """
    parser = argparse.ArgumentParser(description=description)
    
    # Standard Input
    standar = parser.add_argument_group(title='Input and Output', 
                                        description='Input and output for image processing.')
    standar.add_argument("-i", "--input", dest="input", action='store', 
                         required=True, help="Input directory containing RGB images.")
    standar.add_argument("-o", "--output", dest="output", action='store', 
                         required=True, help="Output directory for grayscale images.")
    
    args = parser.parse_args()

    # Standardize paths
    args.input = os.path.abspath(args.input)
    args.output = os.path.abspath(args.output)

    return args

def process_images(input_dir, output_dir):
    """
    Convert RGB images to grayscale and save them.
    """
    image_paths = glob.glob(os.path.join(input_dir, "*.tif")) # using only data in the tif format
    
    for image_path in image_paths:
        # Read the RGB image
        image_rgb = io.imread(image_path)
        
        # Convert to grayscale
        image_gray = rgb2gray(image_rgb)
        
        # Extract the image name and create output path
        image_name = os.path.basename(image_path).split('.')[0]
        output_path = os.path.join(output_dir, f"{image_name}_gray.tif")
        
        # Save the grayscale image
        io.imsave(output_path, image_gray)
        print(f"Saved grayscale image: {output_path}")


def main():
    """
    Function to call all other functions.
    """
    options = getOptions()
    process_images(options.input, options.output)

if __name__ == '__main__':
    main()
