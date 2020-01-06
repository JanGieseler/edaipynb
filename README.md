# edaipynb
edaipynb is an intro to 'Experimental Data Analysis with iPython Notebooks'

After reading through this file and going through the notebooks you will know
- How to setup a working environment (using Anaconda, PyCharm and Github)
- How to work with python packages, including
    - some basics of the Python language
    - package structure
    - version control with git (using github)
    - distribution of python packages (using pip)
    - accessing your python packages form jupyter notebooks
- How to work with jupyter notebooks, including
    - notebook extensions to extend the capabilities of your notebooks
    - organized and readable notebooks (using markdown, html and LaTex)
    - dynamically load your python packages
    - load and save data (using pandas)
    - plotting scientific figures 
    - interactive plotting for data analysis and exploration

## Before you get started - Setting up
Before we get going you need to install a few programs and setup you working environment
### Anaconda
I recommend to install python via Anaconda, which supports Linux, MacOS and Windows. Go to https://www.anaconda.com/distribution/ and install the latest version (Anaconda 2019.10 | Python 3.7 as of this writing).
This provides with python 3.7 and all the main python packages ![](./images/distro-01-1.png)
### PyCharm




funniest/
    funniest/
        __init__.py
    setup.py




edaipynb is built on python 3.6 and tested on Ubunutu, MacOS and Windows
It was built by Jan Gieseler at ICFO. 
It is distributed under the [Revised BSD License](https://en.wikipedia.org/wiki/BSD_licenses).

## Getting Started
The software was developed and tested with python 3.6 on 64-bit Ubunutu. Prior to installation, install the latest  Anaconda distribution for python version 3.6, as it contains some extra dependencies this project utilizes.
You can find the latest Anaconda distribution [here](https://www.continuum.io/downloads). 

### Installation
There are two main ways to install edaipynb: via pip, the python package manager, or directly from the source via github. The former is easier, while the latter gives more explicit access to the source code.

#### Via pip (Beginner)
The simplest way to install edaipynb is with the command-line utility pip. To install simply issue the command

```>>> pip install git+https://github.com/JanGieseler/edaipynb.git```


#### Via git (Intermediate/Advanced)
If you are interested in hosting the source code more directly, you can clone from our git page:

```>>> git clone https://github.com/JanGieseler/edaipynb.git```


## Funding
duffingtools has been partially funded by the European Union (H2020-MSCA-IF-2014 under REA grant Agreement No. 655369).

![Marie Skłodowska-Curie Action](/docs/images/MC_EU_logo_small.png?raw=true "Marie Skłodowska-Curie Action")

# License
This software is released under a dual license; one of the following options can be chosen:

The [Revised BSD License](https://opensource.org/licenses/BSD-2-Clause) (© 2019, Jan Gieseler [JG]).
Any other license, as long as it is obtained from the creator of this package.

## FAQ
### pip install doesn't work
Make sure you have the latest version of pip and setuptools
```>>> pip install --upgrade setuptools```
```>>> pip install --upgrade pip```

