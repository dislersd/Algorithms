#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution

'''
for each cookie there is a certain number of ways to eat the cookies
3 cookies = (1 + 1 + 1), (1 + 2), (2 + 1), (3)
2 cookies = (1 + 1), (2)
1 cookie = 1
0 cookies = 0
def eat_cookies(n):
    base case
    if n = 0:
        return 1
    
    return n * eat_cookies(n - 1)
'''

def eating_cookies(n, cache=None):
    if n < 0:
        return 1
    return eating_cookies(n - 1) + eating_cookies(n - 2)

print(eating_cookies(2))



if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')