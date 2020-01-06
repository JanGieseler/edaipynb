# edaipynb
edaipynb is an intro to 'Experimental Data Analysis with iPython Notebooks'

After reading through this file and going through the notebooks you will know
edaipynb is built on python 3.6 and tested on Ubunutu, MacOS and Windows
It was built by Jan Gieseler at ICFO. 
It is distributed under the [Revised BSD License](https://en.wikipedia.org/wiki/BSD_licenses).

## Getting Started
The software was developed and tested with python 3.6 on 64-bit Ubunutu. Prior to installation, install the latest  Anaconda distribution for python version 3.6, as it contains some extra dependencies this project utilizes.
You can find the latest Anaconda distribution [here](https://www.continuum.io/downloads). 

### Installation
There are two main ways to install duffingtools: via pip, the python package manager, or directly from the source via github. The former is easier, while the latter gives more explicit access to the source code.

#### Via pip (Beginner)
The simplest way to install duffingtools is with the command-line utility pip. To install simply issue the command

```>>> pip install git+https://github.com/JanGieseler/duffingtools.git```


#### Via git (Intermediate/Advanced)
If you are interested in hosting the source code more directly, you can clone from our git page:

```>>> git clone https://github.com/JanGieseler/duffingtools.git```


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

