class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [letter.lower() for letter in s if letter.isalnum()]
        if s == s[::-1]:
            return True
        else:
            return False