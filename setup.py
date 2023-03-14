
from setuptools import setup,find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()


setup(
     name='ig_gds_utilities',  
     version='0.1.6',
     packages=(
     find_packages(exclude=['*config_utilities.py'])),
     data_files=[('./ig_gds_utilities/config_utilities_EXAMPLE.cfg')],
     author="Wilson Acero",
     author_email="acerowilson@gmail.com",
     description="Python library to be used by differente GDS services",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/awacero/ig_gds_utilities",
     
     install_requires = ['requests>=2.22.0'],
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )
