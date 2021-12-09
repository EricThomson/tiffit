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
Make sure you have pip installed otherwise it might install in your base environemnt like a twit.

    conda install pip
    pip install -e .



## To do
- argparser for command line:
  - https://docs.python.org/3/library/argparse.html#the-add-argument-method
  - https://www.psaggu.com/learning-python/2020/08/07/pfd-writing-command-line-tools-part-2.html
  - https://towardsdatascience.com/a-simple-guide-to-command-line-arguments-with-argparse-6824c30ab1c3
- do basic setup.py for local pip install
- metadata function
- concatenation function
- command line direct calling using entry points

## Acknowledgments
- Powered by the [tifffile](https://github.com/cgohlke/tifffile/) package.
- Developed with support from NIH Bioinformatics, NIEHS Neurobehavioral Core, and NIEHS Neurobiology Laboratories.
