# tiffit
Lightweight command-line interface for multi-page tiff files.
Conversion, metadata extraction, and concatenation.

That's it. Nothing fancy.

Built using the tifffile package:
https://github.com/cgohlke/tifffile/

## installation and usage
Install with pip and then use from command line.

    pip install tiffit

    # convert file into a well-behaved bigtiff file
    tiffit convert old.tiff new.tiff

    # get metadata about file without loading file into memory
    # tells you number of images, dimensions, and data type
    tiffit metadate filename.tiff

    # concatenate two tiff files into a newfile
    tiffit concat file1.tiff file2.tiff newfile.tiff

## For more advanced functions
tiffit will remain a lightweight command-line tool. For more complexity, see:
- [opencv](https://docs.opencv.org/4.x/d6/d00/tutorial_py_root.html)
- [pillow](https://github.com/python-pillow/Pillow)
- [tiffile](https://github.com/cgohlke/tifffile/)
- [tifftools](https://github.com/DigitalSlideArchive/tifftools)

If there are specific tiff tags you would like to see read out from metadata, please let me know, bearing in mind I am trying to keep this interface fairly universal and simple.

## To do
- implement metadata function
- implement concatenation function

## Acknowledgments
- Powered by the [tifffile](https://github.com/cgohlke/tifffile/) package.
- Developed with support from NIH Bioinformatics, NIEHS Neurobehavioral Core, and NIEHS Neurobiology Laboratories.
