import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
     name='haydarctl',  
     version='0.1',
     author="WoodProgrammer",
     description="Config drift checker",
     long_description=long_description,
     long_description_content_type="text/markdown",
      install_requires=[
          "jinja2",
          "GitPython",
          "pyyaml"
        ],
     url="https://github.com/WoodProgrammer/haydarctl/",
     packages=setuptools.find_packages(),
     entry_points ={
            'console_scripts': [
                'haydarctl = haydarctl.main:main'
            ]
        },
     classifiers=[
         "Programming Language :: Python :: 3",
         "Operating System :: OS Independent",
     ],
 )