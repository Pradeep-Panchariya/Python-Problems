"""
Author : Pradeep Panchariya
Email : panchariya11@gmail.com
"""

def sort_words(str):
    """
    sort the words in the given input string
    str : input of string type
    return : sorted output
    """ 
    sorting_str = sorted([w.lower()+w for w in str.split()])
    return ' '.join([w[len(w)//2:] for w in sorting_str])

    
print(sort_words("string of WORDS"))