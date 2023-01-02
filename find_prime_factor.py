"""
Author : Pradeep Panchariya
Email : panchariya11@gmail.com
"""

def find_prime_factor(num):
    """ 
    find the prime factor for the given number.
    num : input
    return : list of prime factor numbers
    """
    factors = []
    i = 2
    while num!=1:
        if num%i==0:
            factors.append(i)
            num//=i
        else:
            i+=1
    return factors


print(find_prime_factor(10))
