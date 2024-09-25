"""
Part of tiffit package
https://github.com/EricThomson/tiffit
"""

import os
import argparse
import tifffile
from tifftools import tiff_concat


def convert(original_path, new_path, verbose=True):
    """
    Convert tiff to format that can be read by everybody.

    When working with tiff files, they sometimes save in weird formats.
    In particular, there are poorly-defined big tiff/imagej formats that
    cannot be read by all platforms.

    This function undoes that, converting to bigtiff=True, imagej=False, 
    which can be read by all the software we use (inscopix/imagej/mesmerize)

    Inputs:
        original_path (string)
        new_path (string)
        verbose (bool) print things

    Output:
        new_path (string) when it successfully saves the new tiff
    """
    if new_path == original_path:
        answer = input("The new file will overwrite the original. Is this correct? (y/n):  ")
        if answer != "y":
            print("\nexiting tiffit.convert()")
            return

    if os.path.isfile(new_path):
        answer = input(f"{new_path} already exists. Overwrite? (y/n):  ")
        if answer != "y":
            print("\nexiting tiffit.convert()")
            return

    loaded_movie = tifffile.imread(original_path)
    if verbose:
        print(f"\tgenerating {new_path}.\n\tthis can take a while, depending on file size.")
    tifffile.imsave(new_path,
                   loaded_movie,
                   imagej=False,
                   bigtiff=True)
    if verbose:
        # if the file already existed it will say success so beware
        if os.path.isfile(new_path):
            print("\ttiffit.convert() success!")
        else:
            print("\ttiffit.convert() failed")

    return new_path


def info(filepath):
    """
    Print basic info about a tiff file, given path to file.

    Uses tifffile package.
    """
    print(f"Info about {filepath}:")
    with tifffile.TiffFile(filepath) as tf:
        num_images = len(tf.pages)
        first_ifd = tf.pages[0]  # image file directory
        is_imagej = tf.is_imagej
        is_bigtiff = tf.is_bigtiff
    im_dtype = first_ifd.dtype
    im_shape = first_ifd.shape
    print(f"\tNumber of images: {num_images}")
    print(f"\tDimensions of first image: {im_shape}")
    print(f"\tByte representation: {im_dtype}")
    print(f"\tImageJ format? {is_imagej}")
    print(f"\tBigTIFF format? {is_bigtiff}")
    return filepath


def concat(path1, path2, new_path, verbose=True):
    """
    Take tiff files in path1 and path2 and concatenate into tiff in new_path.

    Uses tifffile, adapted from: https://github.com/cgohlke/tifffile/issues/40
    """
    if os.path.isfile(new_path):
        answer = input(f"{new_path} already exists. Overwrite? (y/n):  ")
        if answer != "y":
            print("\nexiting tiffit.concat()")
            return

    if verbose:
        print(f"Creating {new_path}")

    tiff_concat([path1, path2], new_path, overwrite=True)

    if verbose:
        # if the file already existed it will say success so beware
        if os.path.isfile(new_path):
            print("\ttiffit.concat() success!")
        else:
            print("\ttiffit.concat() failed")
    return new_path


def main():
    """
    To test convert:
       tiffit convert D:/tiffit/data/mesmerized.tiff D:/tiffit/data/converted.tiff

    To test info:
        tiffit info D:/tiffit/data/converted.tiff

    To test concat:
        tiffit concat D:/tiffit/data/BK09_ImageJ_tif.tif D:/tiffit/data/BK09_ImageJ_tif.tif D:/tiffit/data/new.tiff
    """
    # set up generic parser
    msg1 = "A lightweight package for doing things with tiff stacks. "
    msg2 = "There are three functions: convert, info, and concat. "
    msg3 = "Enter tiffit <function_name> --help for help with an individual function."
    tiffit_parser = argparse.ArgumentParser(description=msg1 + msg2 + msg3)
    tiffit_subparsers = tiffit_parser.add_subparsers(dest='func',
                                                     help="do simple things with tiff files")

    # convert subparser
    convert_desc = "convert a tiff file to a big tiff that will open in your software"
    convert_parser = tiffit_subparsers.add_parser('convert',
                                                  description=convert_desc,
                                                  help='tiff file converter')
    convert_parser.add_argument("original_path", type=str)
    convert_parser.add_argument("new_path", type=str)

    # info subparser
    info_desc = "Prints out basic info about tiff file without loading file into memory."
    info_parser = tiffit_subparsers.add_parser('info',
                                               description=info_desc,
                                               help='info extractor')
    info_parser.add_argument("path", type=str)

    # concat subparser
    concat_desc = "Concatenate the files in the two paths saving them into the third file."
    concat_parser = tiffit_subparsers.add_parser('concat',
                                                 description=concat_desc,
                                                 help='file concatenator')
    concat_parser.add_argument("path1", type=str)
    concat_parser.add_argument("path2", type=str)
    concat_parser.add_argument("new_path", type=str)

    # extract arguments and call appropriate function
    args = tiffit_parser.parse_args()

    if args.func == 'convert':
        convert(args.original_path, args.new_path)
    elif args.func == 'info':
        info(args.path)
    elif args.func == 'concat':
        concat(args.path1, args.path2, args.new_path)


if __name__ == "__main__":
    main()
