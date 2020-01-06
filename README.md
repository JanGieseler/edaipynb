# edaipynb
edaipynb is an intro to 'Experimental Data Analysis with iPython Notebooks'

## A little motivation
The goal of these notes is to provide a concise guide towards using python and jupyter notebooks for experimental data analysis.
The main target audience is experimental physicist but the ideas here apply more generally.

[Python](https://www.python.org/) is a great tool free of charge that is widely used in academia and industry and therefore a useful skill for any scientist.
In experimental science on of the main challenges is to reconcile code redundancy, change in data structure and format and documentation of the results. ![](./images/motivation.png)

In the following we will use a combination of *python packages* to maintain low level code that can be maintained by and distributed to several collaborators and *jupyter notebooks* for highlevel code, clean representation of the results, and data exploration. 

 
## What you will learn
After reading through this file and going through the notebooks you will know
- How to setup a working environment (using Anaconda, PyCharm and Github)
- How to work with python packages, including
    - some basics of the Python language
    - package structure
    - version control with git (using github)
    - distribution of python packages (using pip)
    - accessing your python packages from jupyter notebooks
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
Any text editor can be used to develop your python code. However, I find it more convinient to use an "integrated development environment" (IDE) such as PyCharm, which provided a range of useful tools. Go to https://www.jetbrains.com/pycharm/ and download the latest version of PyCharm.
### Github
[Version Control](https://git-scm.com/book/en/v2/Getting-Started-About-Version-Control)  is a system that records changes to a file or set of files over time so that you can recall specific versions later. Generally it means that if you screw things up or lose files, you can easily recover. In addition, you get all this for very little overhead.
As always there are many solutions out there. Here we will work with github. To create an account go to https://github.com/. To use github seamlessly with PyCharm go to `PyCharm->Preferences->Version Control->Github`. Then click on the '+' sign to login with your github credentials: ![](./images/PyCharm-Github.png)


### Creating and distributing your own package
Now that we have all the tools installed we can finally begin to create our own python package

Let's start with the [minimnal structure](https://python-packaging.readthedocs.io/en/latest/minimal.html).
 ```
edaipynb/
    edaipynb/
        __init__.py
    setup.py
``` 
Note that the project name appears twice here. The higher level is the project and the lower level contains the actual source code. I also already included `setup.py`, which will be used later to distribute the package. The `__init__.py` file indicates that the folder `edaipynb` is actually a python package and not just a simple folder. At this stage `__init__.py` is just an empty text file.

Let's create this minimal package and link it to github.

- In PyCharm go to `File->New project`, change untitled for the project name (e.g. edaipynb) and select the python interpreter. You can either setup a custom virtual environment or select the standard interpreter. Let's do the latter for now.
- Add a new python package with the same name as your project (this automatically creates the `__init__.py` in the new subfolder).
- Add the `setup.py` file for example by copying and modifying the file from https://github.com/JanGieseler/edaipynb/setup.py.
- add the version number to `edaipynb/__init__.py` by `__version__ = '0.1a0'`
- add a `readme.md` and add some [markdown](https://www.markdownguide.org/cheat-sheet) text 

Your file structure should now looks something like:
 ```
edaipynb/
    edaipynb/
        __init__.py
    setup.py
    readme.md
``` 


Tip: The `edaipynb` follows the above structure, so that you can just use it as a template. 



Now we push the new project to github. Go to `VCS->Import into Version Control->Share Project on Github`

That's it!! Now you can check in a browser that your new project  actually appears in your github projects.










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
![](./images/MC.jpg)

# About
edaipynb is built on python 3.6 and tested on Ubunutu, MacOS and Windows
It was built by Jan Gieseler at ICFO. 
It is distributed under the [Revised BSD License](https://en.wikipedia.org/wiki/BSD_licenses).

# License

This software is released under a dual license; one of the following options can be chosen:

The [Revised BSD License](https://opensource.org/licenses/BSD-2-Clause) (© 2019, Jan Gieseler [JG]).
Any other license, as long as it is obtained from the creator of this package.

## FAQ
### pip install doesn't work
Make sure you have the latest version of pip and setuptools
```>>> pip install --upgrade setuptools```
```>>> pip install --upgrade pip```

