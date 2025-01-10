
# Libraries
import os 
from tiffile import imread
from skimage import io
from skimage.io import imsave
from skimage.color import rgb2gray
from skimage import img_as_ubyte
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

def process_images(input_file, output_file):
    """
    Convert RGB images to grayscale and save them.
    """
    # Read image
    image_rgb = io.imread(input_file)
    print(f"RGB image read: {input_file}, data type: {image_rgb.dtype}")
        
    # Convert to grayscale
    image_gray = rgb2gray(image_rgb)
    print(f"RGB2grayscale conversion completed.")

    # Convert to 8-bit
    image_gray_uint8 = img_as_ubyte(image_gray)
    print(f"Bit depth back conversion.")
        
    # Save the grayscale image
    io.imsave(output_file, image_gray_uint8)
    print(f"Grayscale image saved: {output_file}, data type: {image_gray_uint8.dtype}")

def main():
    """
    Function to call all other functions.
    """
    options = getOptions()
    process_images(options.input, options.output)

if __name__ == '__main__':
    main()
