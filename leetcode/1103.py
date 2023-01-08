from typing import List


# We distribute some number of candies, to a row of n = num_people people in the following way:
#
# We then give 1 candy to the first person, 2 candies to the second person, 
# and so on until we give n candies to the last person.
#
# Then, we go back to the start of the row, giving n + 1 candies to the first person,
# n + 2 candies to the second person, and so on until we give 2 * n candies to the last person.
#
# This process repeats (with us giving one more candy each time, 
# and moving to the start of the row after we reach the end) until we run out of candies. 
# The last person will receive all of our remaining candies (not necessarily one more than the previous gift).
#
# Return an array (of length num_people and sum candies) that represents the final distribution of candies.

class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        result = [0] * num_people

        amount_to_add = 1

        while candies > 0:
            for i, _ in enumerate(result): 
                if candies - amount_to_add <= 0:
                    result[i] += candies
                    candies = 0
                    break
                result[i] += amount_to_add
                candies -= amount_to_add
                amount_to_add += 1
                
        return result
