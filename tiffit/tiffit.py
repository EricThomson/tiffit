"""
Part of tiffit package
https://github.com/EricThomson/tiffit
"""

import os
import argparse
import tifffile


def convert(original_path, new_path, verbose=True):
    """
    Convert tiff to format that can be read by everybody.

    When working with tiff files, they sometimes save in weird formats.
    In particular, there are poorly-defined big tiff/imagej formats that
    cannot be read by all platforms.

    This function undoes that, converting to bigtiff=True, imagej=False, which can
    be read by all the software we use (inscopix/imagej/mesmerize)

    Inputs:
        original_path (string)
        new_path (string)
        verbose (bool) print whether it worked (default True)

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


def metadata(filepath):
    print("here is the metadata")


def concatenate(path1, path2):
    print("I just contactenated some shit, bruv")
# %%


def main():
    """
    To test converter:
       python tiffit.py convert D:/tiffit/data/mesmerized.tiff D:/tiffit/data/converted.tiff

    To test metadata:
        python tiffit.py metadata D:/tiffit/data/converted.tiff

    To test concatenate:
        python tiffit.py concat D:/tiffit/data/mesmerized.tiff D:/tiffit/data/converted.tiff D:/tiffit/data/new.tiff
    """
    # set up generic parser
    msg1 = "A bare-bones package for doing things with multi-page tiff files. "
    msg2 = "Enter tiffit <function_name> --help for help with an individual function."
    tiffit_parser = argparse.ArgumentParser(description=msg1 + msg2)
    tiffit_subparsers = tiffit_parser.add_subparsers(dest='func',
                                                     help="convert, metadata, concat subparser")

    # convert subparser
    convert_desc = "convert a tiff file to a big tiff that will open in your software"
    convert_parser = tiffit_subparsers.add_parser('convert',
                                                  description=convert_desc,
                                                  help='tiff file converter')
    convert_parser.add_argument("original_path", type=str)
    convert_parser.add_argument("new_path", type=str)

    # metadata subparser
    metadata_desc = "Prints out metadata, such as number of images, for file without loading file into memory."
    metadata_parser = tiffit_subparsers.add_parser('metadata',
                                                   description=metadata_desc,
                                                   help='metadata extractor')
    metadata_parser.add_argument("path", type=str)

    # concat subparser
    concat_desc = "Concatenate the files in the two paths, creating a third file."
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
    elif args.func == 'metadata':
        print('METADATA')
        print(args.path)
    elif args.func == 'concat':
        print('CONCAT')
        print(args.path1)
        print(args.path2)
        print(args.new_path)


if __name__ == "__main__":
    main()
