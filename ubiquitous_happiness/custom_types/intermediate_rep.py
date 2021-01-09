"""Module holds all the larger types used in the architect module."""
from typing import List, Dict, Optional


class IR():
    """
    Hold all the larger types used for the Intermediate Representation.

    The IR class is used to collect all the larger types defined for the
    architect module.
    """

    type = Dict[str, Optional[List[Optional[str]]]]
