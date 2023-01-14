# Given an integer x, return true if x is a palindrome, and false otherwise.

class Solution:
    def isPalindrome(self, num: int) -> bool:
        if num < 0:
            return False
        temp = num
        rev = 0
        while num > 0:
            digit = num % 10
            rev = rev * 10 + digit
            num = num // 10
        if temp == rev:
            return True

        return False
