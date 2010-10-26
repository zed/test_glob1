import os

from distutils.core import setup

def read_file(relpath):
    return open(os.path.join(os.path.dirname(__file__), relpath)).read()

_readme_lines = read_file("README.txt").splitlines()

CLASSIFIERS = """\
Development Status :: 4 - Beta
Intended Audience :: Developers
License :: OSI Approved :: MIT License
Operating System :: OS Independent
Programming Language :: Python :: 2
Programming Language :: Python :: 3
Topic :: Software Development :: Libraries :: Python Modules
"""

NAME             = 'test_glob1'
VERSION          = '0.0.1'
DESCRIPTION      = _readme_lines[0]
LONG_DESCRIPTION = "\n".join(_readme_lines[2:])
URL              = "http://stackoverflow.com/questions/3964681/find-all-files-in-directory-with-extension-txt-with-python/3971553#3971553"
DOWNLOAD_URL     = None #XXX
LICENSE          = 'MIT'
CLASSIFIERS      = filter(len, CLASSIFIERS.split('\n'))
AUTHOR           = "zed"
AUTHOR_EMAIL     = "arn.zart@gmail.com"
PLATFORMS        = ["Windows", "Linux", "Solaris", "Mac OS-X", "Unix"]

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    url=URL,
    download_url=DOWNLOAD_URL,
    license=LICENSE,
    classifiers=CLASSIFIERS,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    maintainer=AUTHOR,
    maintainer_email=AUTHOR_EMAIL,
    platforms=PLATFORMS,
    py_modules=[],
    provides=[],
)
