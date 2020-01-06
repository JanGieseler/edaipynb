from setuptools import setup, find_packages
from edaipynb import __version__ as current_version

# ========================================================================================================
# ========================================================================================================
# NOTES for updating this file:
# 1) for version update in the edaipynb.__init__
# 2) update the following comment_on_changes
comment_on_changes = 'first commit'
# ========================================================================================================
# ========================================================================================================


setup(name='edaipynb',
      version=current_version,
      packages=find_packages(),
      description='Experimental Data Analysis with iPython Notebooks',
      url='https://github.com/JanGieseler/edaipynb',
      author='Jan Gieseler',
      author_email='jangie@pm.me',
      license='MIT',
      packages=['edaipynb'],
      zip_safe=False,
      keywords = 'data analysis',
      long_description = comment_on_changes,
      classifiers = [
            'Programming Language :: Python :: 3',
            'License :: OSI Approved :: 2-Clause BSD License',
            'Development Status :: 4 - Beta',
            'Environment :: MacOS (Ubuntu)',
      ],
      install_requires = [
      'matplotlib',
      'pandas',
      'numpy',
      'scipy',
      # 'lmfit',
      # 'uncertainties',
      ]
      )