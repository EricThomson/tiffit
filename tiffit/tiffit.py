"""
tiffit.py

Part of tiffit package
https://github.com/EricThomson/tiffit

"""

import tifffile
import os


# %%
def write(original_path, new_path, verbose=True):
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
            print("\nexiting good_tiff()")
            return

    if os.path.isfile(new_path):
        answer = input(f"{new_path} already exists. Overwrite? (y/n):  ")
        if answer != "y":
            print("\nexiting good_tiff()")
            return

    loaded_movie = tifffile.imread(original_path)
    if verbose:
        print(f"generating {new_path}.\nthis can take a while, depending on file size.")
    tifffile.imsave(new_path,
                   loaded_movie,
                   imagej=False,
                   bigtiff=True)
    if verbose:
        print("success!") if os.path.isfile(new_path) else print("failed")

    return new_path


if __name__ == "__main__":
    data_dir = '../data/'
    original_path = data_dir + r'005d58f7-9841-4854-b6d9-3e8075efc0f5_mc.tiff'
    print(original_path)
    new_path = data_dir + 'test_converted.tiff'
    print(new_path)
    write(original_path, new_path)
