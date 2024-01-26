#!/usr/bin/python3
def search_replace(my_list, search, replace):
    return [valu if valu != search else replace for valu in my_list]
