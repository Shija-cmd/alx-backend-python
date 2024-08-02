#!/usr/bin/env python3
"""
type-annotated function make_multiplier that takes a float multiplier
returns a function that multiplies a float by multiplier
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Typed-annotated function
    make_multiplier
    """

    def fn(num: float):
        return num * multiplier
    return fn
