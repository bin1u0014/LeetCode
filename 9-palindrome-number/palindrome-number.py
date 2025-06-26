class Solution:
    def isPalindrome(self, x: int) -> bool:
        arr = list(str(x))
        leng = len(arr)
        limit = math.ceil(leng/2)
        a = 0
        j = -1
        for i in range(limit):
            if arr[i] != arr[j]:
                return False
            elif arr[i] == arr[j]: 
                a+=1
                j-=1
        

        if a == limit:
            return True

