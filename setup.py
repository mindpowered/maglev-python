import setuptools

#with open("README.md", "r") as fh:
    #long_description = fh.read()
setuptools.setup(
     name='mindpowered-maglev',
     version='0.4.33',
     description="maglev",
     #long_description=long_description,
     #long_description_content_type="text/markdown",
     py_modules=['maglev'],
     classifiers=[
         "Programming Language :: Python :: 3",
         "Operating System :: OS Independent",
         'License :: OSI Approved :: Common Public Attribution License Version 1.0 (CPAL-1.0)',
     ],
 )
