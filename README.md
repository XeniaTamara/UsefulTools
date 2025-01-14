# UsefulTools

## RGB to grayscale conversion

1. Ensure you have an input image.tif you want to process.
2. Create an output file name.
3. Run the script with the following command:
   
``` bash
python rgb_to_gray.py --i path/to/your/image.tif --o path/to/output/grayscale_image.tif
```

## Contrast-enhancement with CLAHE

Applicable for both RGB and grayscale images.
Kernelsize, clip limit and nbins are optional parameters that will use a default in case they are not defined.

1. Ensure you have an input image.tif you want to process.
2. Create an output file name.
3. Run the script with the following command:

``` bash
python clahe.py -i path/to/your/image.tif -o path/to/output/image.tif -ks defined_kernelsize -cl defined_cliplimit -nb defined_nbins
```
