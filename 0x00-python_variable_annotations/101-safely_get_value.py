#!/usr/bin/env python3
"""
add type annotations to the function
Given the parameters and the return values
"""
from typing import Sequence, Union, Any, TypeVar, Mapping

R = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[R, None] = None) -> Union[Any, R]:
    """
    Add type annotations to function
    Given the parameters and the return values
    """
    if key in dct:
        return dct[key]
    else:
        return default
