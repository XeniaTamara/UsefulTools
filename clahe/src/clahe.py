# Libraries
import os 
from tiffile import imread
from skimage.exposure import equalize_adapthist
from skimage import io
from skimage.io import imsave
from skimage import img_as_ubyte, img_as_float32, img_as_uint
import argparse


def get_options():
    """
    Function to pull in arguments for input and output paths.
    """
    description = """ Enhance contrast of images and save them. """
    parser = argparse.ArgumentParser(description=description)
    
    # Standard Input
    standar = parser.add_argument_group(title='Input and Output', 
                                        description='Input and output for image processing.')
    standar.add_argument("-i", "--input", dest="input", action='store', 
                         required=True, help="Input directory containing RGB or grayscale images.")
    standar.add_argument("-o", "--output", dest="output", action='store', 
                         required=True, help="Output directory for contrast-enhanced images.")
    # Optional parameters (default defined in compliance to scikit-image parameter defaults)
    parser.add_argument("-ks", "--kernelsize", type=int, default=None, 
                        help="Kernel size for CLAHE. Default is None.")
    parser.add_argument("-cl", "--cliplimit", type=float, default=0.01, 
                        help='Clip limit for CLAHE, ranging between 0 and 1. Default is 0.01.')
    parser.add_argument("-nb", "--nbins", type=int, default=256, 
                        help='Number of bins for CLAHE. Default is 256.')

    
    args = parser.parse_args()

    # Standardize paths
    args.input = os.path.abspath(args.input)
    args.output = os.path.abspath(args.output)

    return args

def process_images(input_file, output_file, kernel_size, clip_limit, nbins):
    """
    Enhance contrast of images and save them.
    """
    # Read image
    image_original = io.imread(input_file)
    print(f"Input image read: {input_file}")

    # Contrast enhancement with CLAHE
    image_clahe = equalize_adapthist(image_original, kernel_size=kernel_size, clip_limit=clip_limit, nbins=nbins)
    print(f"CLAHE operation completed.")

    # Convert to original data type
    original_dtype = image_original.dtype
    if original_dtype in ['uint8', 'uint16', 'float32']:
        if original_dtype == 'uint8':
            image_clahe = img_as_ubyte(image_clahe)
        elif original_dtype == 'uint16':
            image_clahe = img_as_uint(image_clahe)
        else:
            image_clahe = img_as_float32(image_clahe)
        print(f"Successfully converted back to original data format: {original_dtype}")
    elif original_dtype == 'float64':
        print(f"Original data format preserved: {original_dtype}")
    else:
        print(f"Unsupported data type: {original_dtype}. Grayscale image saved in default data format: {image_clahe.dtype}")
        
    # Save the contrast-enhanced image
    io.imsave(output_file, image_clahe)
    print(f"Contrast-enhanced image saved: {output_file}")

def main():
    """
    Function to call all other functions.
    """
    options = get_options()
    process_images(
        input_file=options.input, 
        output_file=options.output, 
        kernel_size=options.kernelsize, 
        clip_limit=options.cliplimit, 
        nbins=options.nbins
    )


if __name__ == '__main__':
    main()