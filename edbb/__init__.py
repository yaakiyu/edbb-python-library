# EDBB Python Package

from .initializer import __version__
from .error_handling import print_error_message
from .register import register, patch_bot

__all__ = [
    '__version__', 'print_error_message', 'register', 'patch_bot'
]
