from typing import List


# Given two arrays of integers with equal lengths, return the maximum value of:
#
# |arr1[i] - arr1[j]| + |arr2[i] - arr2[j]| + |i - j|
#
# where the maximum is taken over all 0 <= i, j < arr1.length.

class Solution:
    """
    |arr1[i] - arr1[j]| + |arr2[i] - arr2[j]| + |i - j|

    abs(A) + abs(B) = max(A + B, A-B, -A+B, -A-B) =>

    (arr1[i] - arr1[j]) + (arr2[i] - arr2[j]) + i - j
    (arr1[i] - arr1[j]) - (arr2[i] - arr2[j]) + i - j
    - (arr1[i] - arr1[j]) + (arr2[i] - arr2[j]) + i - j
    - (arr1[i] - arr1[j]) - (arr2[i] - arr2[j]) + i - j ===>

    arr1[i] + arr2[i] + i - arr1[j] - arr2[j] - j
        -----------------------------------------
        ==> (arr1[i] + arr2[i] + i) - (arr1[j] + arr2[j] + j)

    arr1[i] - arr2[i] + i - arr1[j] + arr2[j] - j
        -----------------------------------------
        ==> (arr1[i] - arr2[i] + i) - (arr1[j] - arr2[j] + j)

    -arr1[i] + arr2[i] + i + arr1[j] - arr2[j] - j
        -----------------------------------------
        ==> (-arr1[i] + arr2[i] + i) - (-arr1[j] + arr2[j] + j)

    -arr1[i] - arr2[i] + i + arr1[j] + arr2[j] - j 
        -----------------------------------------
        ==> (-arr1[i] - arr2[i] + i) - (-arr1[j] - arr2[j] + j)
 

    """
    
    def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:
        result = 0
        for signX in {-1, 1}:
            for signY in {-1, 1}:
                mx = -(10 ** 20)
                mn = (10 ** 20)

                for i, (x, y) in enumerate(zip(arr1, arr2)):
                    mx = max(mx, signX * x - signY * y + i)
                    mn = min(mn, signX * x - signY * y + i)

                result = max(result, mx - mn)

        return result

