#!/usr/bin/env python3
"""
Annotate the below function’s parameters
return values with the appropriate types
"""
from typing import Sequence, Iterable, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Annotate the below function’s parameters
    return values with the appropriate types

    """
    return [(i, len(i)) for i in lst]
