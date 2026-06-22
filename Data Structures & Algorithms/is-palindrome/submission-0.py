class Solution:
    def isPalindrome(self, s: str) -> bool:
        s="".join(c for c in s if c.isalnum())

        print(len(s)//2)

        for i in range (len(s)//2):
            if s[i].lower()!= s[len(s)-1-i].lower():
                print(s[i])
                print(s[len(s)-1])
                return False
        return True

            
        