#!/usr/bin/env python

try:
    from .pyKSOPT import KSOPT
    __all__ = ['KSOPT']
except:
    __all__ = []
