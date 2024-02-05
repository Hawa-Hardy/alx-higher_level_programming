#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        my_result = fct(*args)
    except Exception as idx:
        sys.stderr.write("Exception: {}\n".format(idx))
        my_result = None
    return (my_result)
