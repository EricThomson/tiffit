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
        print(f"generating {new_path}.\nthis can take a while, depending on file size.")
    tifffile.imsave(new_path,
                   loaded_movie,
                   imagej=False,
                   bigtiff=True)
    if verbose:
        print("tiffit.convert() success!") if os.path.isfile(new_path) else print("tiffit.convert() failed")

    return new_path


def metadata(filepath):
    print("here is the metadata")


def concatenate(path1, path2):
    print("I just contactenated some shit, bruv")
# %%


if __name__ == "__main__":
    """
    To test converter:
       python tiffit.py --old D:/tiffit/data/mesmerized.tiff --new D:/tiffit/data/converted.tiff
    """
    tiffit_parser = argparse.ArgumentParser(description="tiffit parser")
    tiffit_subparsers = tiffit_parser.add_subparsers('func')

    convert_parser = tiffit_subparsers.add_parser('convert',
                                                  help='tiffit converter')
    convert_parser.add_argument("--old", type=str, required=True)
    convert_parser.add_argument("--new", type=str, required=True)

    metadata_parser = tiffit_subparsers.add_parser('metadata',
                                                   help='tiffit metadata extractor')
    metadata_parser.add_argument("--path", type=str, required=True)

    concat_parser = tiffit_subparsers.add_parser('concat',
                                                 help='tiffit concatenation')
    concat_parser.add_argument("--path1", type=str, required=True)
    concat_parser.add_argument("--path2", type=str, required=True)

    args = tiffit_parser.parse_args()
    print(f"Parser output: {args}")

    if args.func == 'convert':
        print('CONVERT')
    elif args.func == 'metadata':
        print('METADATA')
    elif args.func == 'concat':
        print('CONCAT')
    else:
        print("HUH?")
    # print(f"in tiffit...\nold: {args.old}\nnew: {args.new}")
    # convert(args.old, args.new)
