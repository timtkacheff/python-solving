# A complex number can be represented as a string on the form "real+imaginaryi" where:
#
#     real is the real part and is an integer in the range [-100, 100].
#     imaginary is the imaginary part and is an integer in the range [-100, 100].
#     i2 == -1.
#
# Given two complex numbers num1 and num2 as strings, return a string of the complex number that represents their multiplications.

class Solution:
    # (a + Bi) * (x + Yi) = aX - bY + (bX + aY)i
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        first = [int(x) for x in num1[:-1].split("+")]
        second = [int(x) for x in num2[:-1].split("+")]
        a, b = first[0], first[1]
        x, y = second[0], second[1]

        return f"{a*x - b*y}+{b*x + a*y}i"


sol = Solution()
print(sol.complexNumberMultiply("1+1i", "1+1i"))
print(sol.complexNumberMultiply("1+-1i", "1+-1i"))
