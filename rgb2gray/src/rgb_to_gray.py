
# Libraries
import os 
from tiffile import imread, imsave
from skimage import io
from skimage.color import rgb2gray
from skimage import img_as_ubyte, img_as_float32, img_as_uint
import argparse
import glob


def get_options():
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
    print(f"Input image read: {input_file}")

    # Convert to grayscale
    image_gray = rgb2gray(image_rgb)
    print(f"RGB2grayscale conversion completed.")

    # Convert to original data type
    original_dtype = image_rgb.dtype
    if original_dtype in ['uint8', 'uint16', 'float32']:
        if original_dtype == 'uint8':
            image_gray = img_as_ubyte(image_gray)
        elif original_dtype == 'uint16':
            image_gray = img_as_uint(image_gray)
        else:
            image_gray = img_as_float32(image_gray)
        print(f"Successfully converted back to original data format: {original_dtype}")
    elif original_dtype == 'float64':
        print(f"Original data format preserved: {original_dtype}")
    else:
        print(f"Unsupported data type: {original_dtype}. Grayscale image saved in default data format: {image_gray.dtype}")
        
    # Save the grayscale image
    imsave(output_file, image_gray)
    print(f"Grayscale image saved: {output_file}")

def main():
    """
    Function to call all other functions.
    """
    options = get_options()
    process_images(options.input, options.output)

if __name__ == '__main__':
    main()
