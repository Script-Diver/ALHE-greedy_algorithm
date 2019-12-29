from typing import List, Any


def compare_lists(list1: List[Any], list2: List[Any]):
    if (list1 is None) ^ (list2 is None):
        return False
    if list1 is not None:
        if not len(list1) == len(list2):
            return False
        for pub in list1:
            if not pub in list2:
                return False
    return True