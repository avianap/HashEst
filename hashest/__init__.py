# -*- coding: utf-8 -*-

"""Top-level package for HashEst."""
from pkg_resources import get_distribution, DistributionNotFound


__author__ = """Aviana Polsky"""
__email__ = 'aviana.polsky@gmail.com'

try:
    __version__ = get_distribution(__name__).version
except DistributionNotFound:
    # package is not installed
    from setuptools_scm import get_version
    import os
    __version__ = get_version(
        os.path.dirname(os.path.dirname(__file__))
    )
