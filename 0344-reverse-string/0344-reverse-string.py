class Solution(object):
    def reverseString(self, s):
        n=len(s)
        temp=[0]*n
        for i in range(n):
            temp[i]=s[n-i-1]
        for i in range(n):
            s[i]=temp[i]
        print(temp)

        