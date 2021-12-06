# tiffit
Lightweight command-line interface for multi-page tiff files.
Conversion, concatenation. and metadata extraction.

That's it. Nothing fancy.

Built using the tifffile package:
https://github.com/cgohlke/tifffile/

## usage
From command line:

    tiffit write <path_to_original> <path_to_new>


## installation
Currently no installer

    conda create -n tiffit python=3.8
    conda install -c conda-forge matplotlib
    pip install tifftools


## To do
- argparser for command line:
  - https://towardsdatascience.com/a-simple-guide-to-command-line-arguments-with-argparse-6824c30ab1c3
  - make so you can call different functions with argparser
- do basic setup.py for local pip install
- metadata function
- concatenation function
- command line direct calling using entry points

## Acknowledgments
- Powered by the [tifffile](https://github.com/cgohlke/tifffile/) package.
- Developed with support from NIH Bioinformatics, NIEHS Neurobehavioral Core, and NIEHS Neurobiology Laboratories.
