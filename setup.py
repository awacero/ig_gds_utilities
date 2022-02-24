import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
     name='ig_gds_utilities',  
     version='0.1',
     packages=['ig_gds_utilities'] ,
     author="Wilson Acero",
     author_email="acerowilson@gmail.com",
     description="Python library to be used by differente GDS services",
     long_description=long_description,
   long_description_content_type="text/markdown",
     url="https://github.com/awacero/ig_gds_utilities",
     #packages=setuptools.find_packages(),
     install_requires = ['requests>=2.22.0'],
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )
