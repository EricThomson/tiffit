# tiffit
command-line interface for multi-page tiff conversion, concatenation. and metadata extraction. That's it. Nothing fancy.

Lighgtweight wrapper for tifftools:
https://github.com/DigitalSlideArchive/tifftools.

    tiffit write x.tiff y.tiff --bigtiff --bigendian
    tiffit concat x.tiff y.tiff -bigtiff --bigendian

## installation
Currently no installer

    conda create -n tiffit python=3.8
    pip install tifftools
    conda install -c conda-forge matplotlib

If you want to use spyder, follow this:    
https://github.com/spyder-ide/spyder/wiki/Working-with-packages-and-environments-in-Spyder
