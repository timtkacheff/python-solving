# You are given a string time in the form of  hh:mm,
# where some of the digits in the string are hidden (represented by ?).
#
# The valid times are those inclusively between 00:00 and 23:59.
#
# Return the latest valid time you can get from time by replacing the hidden digits.

class Solution:

    def maximumTime(self, time: str) -> str:
        chars = list(time)

        for i in range(len(chars)):
            if chars[i] == '?':

                if i == 0:
                    if chars[i+1] in "?0123":
                        chars[i] = '2'
                    else:
                        chars[i] = '1'

                elif i == 1:
                    if chars[i - 1] in "01":
                        chars[i] = '9'
                    else:
                        chars[i] = '3'

                elif i == 3:
                    chars[i] = '5'

                elif i == 4:
                    chars[i] = '9'

        return "".join(chars)


sol = Solution()
print(sol.maximumTime("0?:3?"))
print(sol.maximumTime("2?:3?"))
print(sol.maximumTime("1?:?2"))
