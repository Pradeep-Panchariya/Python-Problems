"""
Author : Pradeep Panchariya
Email : panchariya11@gmail.com
"""

def index_all(lst, search_element):
    """
    find the all indexes for given element
    lst : list of element
    search_element : int
    return : lst
    """ 
   

    index_list = []
    for i in range(len(lst)):
        if lst[i]==search_element:
            index_list.append([i])
        elif type(lst[i])==list:
            for j in index_all(lst[i],search_element):
                index_list.append([i]+j)
    return index_list
    
    
print(index_all([0,[0,2,[5,6,7,2]],4,5,0,8,2],2))