# An arithmetic progression is a sequence of n numbers which have a same common difference.
# For example [2, 3, 4, 5] is AP with common difference 1 and [9, 6, 3] is an AP with common difference -3. 
# [2, 5, 6, 8] is not AP since it does not have same common difference between all the terms.

# Given are 4 integers an, a1, n, k where an represent the n- th tern of AP with n denoting the number of terms and a1 is the first term.#Enter your code here
def solveAP(an, a1, n, k):
     #Enter your code here
     d = (an-a1)//(n-1)
     print(d)
     #Enter your code here
     k = a1+(k-1)* d
     print(k)

