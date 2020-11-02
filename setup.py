# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 16:47:31 2020

@author: HP
"""

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
  name = 'PythonSimpleDB',         
  packages = ['simpledb'],
  version = '1.0',      
  license='MIT',        
  description = 'A lightweight (NoSQL) document oriented database, simple and easy to integrate into small apps',   
  long_description=long_description,
  long_description_content_type="text/markdown",
  author = 'OLUWALOLOPE HOPE',                   
  author_email = 'blessyn2hope@gmail.com',      
  url = 'https://github.com/ebonyhope/simpleDB/',   
  download_url = 'https://github.com/ebonyhope/simpleDB/archive/v1.0.tar.gz',    
  keywords = ['NOSQL', 'Database', 'document', 'simple', 'easy'],   
  install_requires=[            
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6'
  ],
)