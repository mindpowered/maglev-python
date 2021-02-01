import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
     name='mindpowered-maglev',
     version='0.7.20',
     author="Mind Powered Corporation",
     author_email="support@mindpowered.dev",
     license="BSD-3-Clause",
     url="https://mindpowered.dev/",
     description="internal bus",
     long_description=long_description,
     long_description_content_type="text/markdown",
     py_modules=['maglev'],
     classifiers=[
         "Programming Language :: Python :: 3",
         "Operating System :: OS Independent",
         'License :: OSI Approved :: BSD License',
     ],
 )
