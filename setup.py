﻿import io
from os.path import abspath, dirname, join
from setuptools import find_packages, setup


HERE = dirname(abspath(__file__))
LOAD_TEXT = lambda name: io.open(join(HERE, name), encoding='UTF-8').read()
DESCRIPTION = '\n\n'.join(LOAD_TEXT(_) for _ in [
    'README.rst'
])

setup(
  name = 'phenomenal',      
  packages = ['phenomenal'], 
  version = '0.0.4',  
  license='MIT', 
  description = 'Phenomenal By Hery Phenomenal',
  long_description=DESCRIPTION,
  author = 'Hery Phenomenal',                 
  author_email = 'thitphavanh.psv@gmail.com',     
  url = 'https://github.com/thitphavanh/HeryProfile',  
  download_url = 'https://github.com/Thitphavanh/HeryProfile/archive/v0.0.4.zip',  
  keywords = ['Hery', 'Profile', 'Hery Phenomenal'],   
  classifiers=[
    'Development Status :: 3 - Alpha',     
    'Intended Audience :: Education',     
    'Topic :: Utilities',
    'License :: OSI Approved :: MIT License',   
    'Programming Language :: Python :: 3',      
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10',
  ],
)