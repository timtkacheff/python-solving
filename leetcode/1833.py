from typing import List

# It is a sweltering summer day, and a boy wants to buy some ice cream bars.
#
# At the store, there are n ice cream bars. You are given an array costs of length n,
# where costs[i] is the price of the ith ice cream bar in coins.
# The boy initially has coins [coins] to spend, and he wants to buy as many ice cream bars as possible. 
#
# Return the maximum number of ice cream bars the boy can buy with coins coins.
#
# Note: The boy can buy the ice cream bars in any order.


class Solution:
    #INFO:O(N + M) \\ Space - O(m)
    def maxIceCream(self, costs: List[int], coins: int):  # -> int:
        icecreams = 0
        m = max(costs)

        freqArray = [0] * (m + 1)
        for cost in costs:
            freqArray[cost] += 1

        for cost in range(1, m + 1):
            if not freqArray[cost]:
                continue

            if coins < cost:
                break

            availableAmount = min(freqArray[cost], coins // cost)
            
            coins -= cost * availableAmount
            icecreams += availableAmount

        return icecreams



    # INFO: O(N * logN) \\ Space - O(N)
    #
    # def maxIceCream(self, costs: List[int], coins: int):  # -> int:
    #         coins -= price
    #     for price in sorted(costs):
    #         coins -= price
    #
    #         if coins < 0:
    #             break
    #
    #         amount += 1
    #
    #     return amount


sol = Solution()
print(sol.maxIceCream([1, 3, 2, 4, 1], 7))
print(sol.maxIceCream([10, 6, 8, 7, 7, 8], 5))
print(sol.maxIceCream([1, 6, 3, 1, 2, 5], 20))
