"""
Figuring out multipage tiff basics

Using tifffile package
"""
import tifffile  # to use imread and imwrite
from tifffile import TiffFile
import os
import matplotlib.pyplot as plt
import anaties as ana

# %%
import tifftools

# %%
"""
seems 0 (idps) is inscopix (idp inscopix data project the s stands for wtf) --
    this is NOT imagej but inscopix, this is what I use.
seems 1 is bioformat saved using imagej
seems 2 is I have no fucking idea what.

Not sure what the problem is exactly. Basically mesmerize won't open in inscopix.
It *is* trying to save as imagej and bigtiff at the same time, which is a no-no they are literally
incompatible file types. Just pick one I guess?
"""
working_dir = r'D:/tiffit/'
data_dir = working_dir + r'data/'
if not os.path.isdir(data_dir):
    os.makedirs(data_dir)

# %%
data_files = os.listdir(data_dir)
for data_file in data_files:
    print(data_file)

# %%
filename = data_files[0]
file_path = data_dir + filename
print(file_path)
# %%
# Header: 0x4949 <little-endian> <BigTIFF>
# BK09_ImageJ_Bioformat_IDPS.tif
tifftools.tiff_dump(data_dir + data_files[0])

# %%
bamf_path = data_dir + data_files[0]
print(bamf_path)

# %%
new_file = gamf_file = 'good_mc.tiff'
new_path = data_dir + new_file
print(new_path)
# %%
bamf_info = tifftools.read_tiff(bamf_path)
# %% following does not work
tifftools.write_tiff(bamf_info, new_path)


# %%
# Header: 0x4d4d <big-endian> <ClassicTIFF>
# BK09_ImageJ_Bioformat_tif.tif
tifftools.tiff_dump(data_dir + data_files[1])

# %%
# Header: 0x4d4d <big-endian> <ClassicTIFF>
# BK09_ImageJ_tif.tif
tifftools.tiff_dump(data_dir + data_files[2])

# %%
"""
What I need to do is pretty simple:
    try out different permutations of saving bullshit between mesmerize and inscopix.
    1. how to load data into inscopix (data that actually works)
    2. Run some shit in mesmerize (small data) with mc
    3. Try to load in inscopix
    4. Fix it.

    First need to port all this shit over to the beast.
"""

# %%
"""
Below is tifftools stuff

For tiff tags:
    https://github.com/DigitalSlideArchive/tifftools/blob/master/tifftools/constants.py#L522
"""
info = tifftools.read_tiff(file_path)
tags = info['ifds'][0]['tags']
for key in tags.keys():
    print(key)

# %% for image 0 (same for image 1)
256
257
258
259
262
270  # in image 1 but not 0
273
274  # 0 but not 1
277
278
279
282  # 1 but not 0  xresolution
283  # 1 but not 0 yresolution
284  # planarconfig
296  # resolution limit
305  # 1 not 0: software
339


# %% for image 2
254  # : newsubfile type (useless)
256  # imagewidth
257  # imagelength
258  # bits per sample
262  # photometric ? (color space of the data)
270  # image description (this can be really useful)
273  # strip offsets (I will never use this)
# samples per pixel : number of components per pixel (what is a component?)
277
278  # rows per strip
279  # strip byte counts
50838  # imageJ custom bullshit
50839  # imageJ custom bullshit

# %%
tags[256]
tags[262]
tags[tifftools.Tag.

# %%
tags[tifftools.Tag.NewSubFileType.value]  # this is useless
tags[tifftools.Tag.ImageDescription.value]
tags[tifftools.Tag.ImageHeight.value]
tags[tifftools.Tag.ImageWidth.value]

tags[tifftools.Tag.Photometric.value]
tags[262]

tags[50838]

exififd= info['ifds'][0]['tags']
exififd.keys()

# %% ifd = image file directory
"""
Below is tifffile stuff
"""

# %%

# %%
tf= TiffFile(file_path)  # as tf:

# %%
print(f"Byte order: {tf.byteorder}")
num_images= len(tf.pages)
print(f"Num images: {num_images}")
first_ifd= tf.pages[0]
print(first_ifd.shape)
page_tags= first_ifd.tags

print(tf.is_imagej)
print(tf.is_bigtiff)
# %%


# %%
image_data= first_ifd.asarray()
plt.imshow(image_data, cmap='gray')

# %%
import tifffile
# %%
loaded_movie= tifffile.imread(file_path)

# %%
print(new_path)
tifffile.imsave(new_path,
                loaded_movie,
                imagej=False,
                bigtiff=True)
