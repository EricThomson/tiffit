from setuptools import setup, find_packages
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "readme.md").read_text()

setup(name='tiffit',
      version='0.1.0',
      description="Lightweight tiff utilities",
      author="Eric Thomson",
      author_email="thomson.eric@gmail.com",
      licence="MIT",
      url="https://github.com/EricThomson/tiffit",
      packages=find_packages(include=['tiffit', 'tiffit.*'],),
      install_requires=['tifffile', 'tifftools'],
      entry_points={
          'console_scripts': ['tiffit=tiffit.tiffit:main', ]
      },
      long_description=long_description,
      long_description_content_type="text/markdown")
