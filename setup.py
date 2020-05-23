import setuptools

#with open("README.md", "r") as fh:
    #long_description = fh.read()
setuptools.setup(
     name='mindpoweredinfra-maglev',
     version='0.4.14',
     description="maglev",
     #long_description=long_description,
     #long_description_content_type="text/markdown",
     py_modules=['maglev'],
     classifiers=[
         "Programming Language :: Python :: 3",
         "Operating System :: OS Independent",
     ],
 )
