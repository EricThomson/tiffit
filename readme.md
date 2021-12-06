# tiffit
Lightweight command-line interface for multi-page tiff files.
Conversion, concatenation. and metadata extraction.

That's it. Nothing fancy.

Lighgtweight wrapper for the tifffile package:
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
- do basic setup.py for local pip install
- argparser for command line:
  https://www.digitalocean.com/community/tutorials/how-to-use-argparse-to-write-command-line-programs-in-python
  https://www.freecodecamp.org/news/the-python-handbook/#howtoacceptargumentsfromthecommandlineinpython
- command line direct calling using entry points
- metadata function
- concatenation function


## Acknowledgments
- Powered by the [tifffile](https://github.com/cgohlke/tifffile/) package.
- Developed with support from NIH Bioinformatics, NIEHS Neurobehavioral Core, and NIEHS Neurobiology Laboratories.
