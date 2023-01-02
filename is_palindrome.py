"""
Author : Pradeep Panchariya
Email : panchariya11@gmail.com
"""

def is_palindrome(str):
    """
    Check whether given string is palindrome or not
    str : input of string type
    return : True or False
    """

    #Method -1 
   # return str==str[::-1]

    # Method -2 
    str = str.lower()
    import re
    pattern = r"[a-z]+"
    r = re.findall(pattern, str)
    str = ''.join(r)
    end = len(str)-1
    begining = 0
    while begining<end:
        if str[begining]!=str[end]:
            return False
        else:
            begining+=1
            end-=1
    return True



print(is_palindrome("Go hang a salami, I'm  a lasagna hog."))