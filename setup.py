"""Setup file for the gridinfo application."""

##############################################################################
# Python imports.
from pathlib    import Path
from setuptools import setup, find_packages

##############################################################################
# Import the library itself to pull details out of it.
import gridinfo

##############################################################################
# Work out the location of the README file.
def readme():
    """Return the full path to the README file.

    :returns: The path to the README file.
    :rtype: ~pathlib.Path
    """
    return Path( __file__).parent.resolve() / "README.md"

##############################################################################
# Load the long description for the package.
def long_desc():
    """Load the long description of the package from the README.

    :returns: The long description.
    :rtype: str
    """
    with readme().open( "r", encoding="utf-8" ) as rtfm:
        return rtfm.read()

##############################################################################
# Perform the setup.
setup(

    name                          = "gridinfo",
    version                       = gridinfo.__version__,
    description                   = str( gridinfo.__doc__ ),
    long_description              = long_desc(),
    long_description_content_type = "text/markdown",
    url                           = "https://github.com/davep/gridinfo",
    author                        = gridinfo.__author__,
    author_email                  = gridinfo.__email__,
    maintainer                    = gridinfo.__maintainer__,
    maintainer_email              = gridinfo.__email__,
    packages                      = find_packages(),
    package_data                  = { "gridinfo": [ "py.typed", "gridinfo.css" ] },
    include_package_data          = True,
    install_requires              = [ "textual", "rich-pixels", "httpx" ],
    python_requires               = ">=3.9",
    keywords                      = "terminal textual secondlife mapping metaverse virtual-worlds",
    entry_points                  = {
        "console_scripts": "gridinfo=gridinfo.app:run"
    },
    license                       = (
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)"
    ),
    classifiers                   = [
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Environment :: Console",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: End Users/Desktop",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Utilities",
        "Topic :: Terminals",
        "Typing :: Typed"
    ]

)

### setup.py ends here
