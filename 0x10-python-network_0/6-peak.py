#!/usr/bin/python3
"""Defines a peak-finding algorithm."""

def find_peak(list_of_integers):
    """Return a peak in a list of unsorted integers."""
    def peak_helper(lo, hi):
        if lo == hi:
            return list_of_integers[lo]
        mid = (lo + hi) // 2
        if (mid == 0 or list_of_integers[mid] >= list_of_integers[mid - 1]) and \
           (mid == len(list_of_integers) - 1 or list_of_integers[mid] >= list_of_integers[mid + 1]):
            return list_of_integers[mid]
        elif mid > 0 and list_of_integers[mid] < list_of_integers[mid - 1]:
            return peak_helper(lo, mid - 1)
        else:
            return peak_helper(mid + 1, hi)

    if not list_of_integers:
        return None
    return peak_helper(0, len(list_of_integers) - 1)
