# tiffit
Lightweight command-line interface for handling tiff files in BigTIFF format.

Convert, extract information, and concatenate. That's it. Nothing fancy.


## installation and usage
Install with pip and then use from command line.

    pip install tiffit

    # convert file into a well-behaved bigtiff file
    tiffit convert old.tiff new.tiff

    # get info about file without loading into memory
    tiffit info filename.tiff

    # concatenate two tiff files into a single bigtiff file
    tiffit concat file1.tiff file2.tiff newfile.tiff


## Notes / caveats
- If there is other information you would like read out from the info command, please let me know, bearing in mind I am trying to keep this interface fairly universal and simple.
- For a summary of tiff (`thousands of incompatible file formats`) specs, see [this excellent overview](https://www.fileformat.info/format/tiff/egff.htm). It is a bit dated, but is still the most readable and detailed reference I've found.
- If you need a package with more complexity, see:
    - [opencv](https://docs.opencv.org/4.x/d6/d00/tutorial_py_root.html)
    - [pillow](https://github.com/python-pillow/Pillow)
    - [tiffile](https://github.com/cgohlke/tifffile/)
    - [tifftools](https://github.com/DigitalSlideArchive/tifftools)


## To do
- add keyword argument to info so user can check on specific image in stack.
Better yet, don't allow mixing of formats just make this a pure bigtiff library: add autoconversion of concatenated files.
- add verbosity controller for convert and concat.



## Acknowledgments
- Powered by the [tifffile](https://github.com/cgohlke/tifffile/) and [tifftools](https://github.com/DigitalSlideArchive/tifftools) packages.
- Developed with support from NIH Bioinformatics, NIEHS Neurobehavioral Core, NIEHS Neurobiology Laboratories. In particular thanks to Shaohua Wang for help during development.
