#!/usr/bin/env python
import os


class Config():
    """
    Basic config
    """
    # Application config
    TIMEZONE = 'Europe/Berlin'
    BASE_DIR = os.path.dirname(os.path.dirname(__file__))
