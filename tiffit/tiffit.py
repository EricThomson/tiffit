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


if __name__ == "__main__":
    """
    To test converter:
       python tiffit.py --old D:/tiffit/data/mesmerized.tiff --new D:/tiffit/data/converted.tiff 
    """
    convert_parser = argparse.ArgumentParser(description="converting tiff file")
    convert_parser.add_argument("--old", type=str, required=True)
    convert_parser.add_argument("--new", type=str, required=True)
    args = convert_parser.parse_args()
    print(f"in tiffit...\nold: {args.old}\nnew: {args.new}")
    convert(args.old, args.new)
