'''
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
'''


class Solution(object):
    # def climbStairs(self, n):
    #     """
    #     :type n: int
    #     :rtype: int
    #     """
    #     if n <= 0:
    #         return 0
    #     elif n == 1:
    #         return 1
    #     elif n == 2:
    #         return 2
    #     else:
    #         return self.climbStairs(n-1) + self.climbStairs(n-2)

    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            a, b = 1, 2
            for i in range(3, n+1):
                tmp = a + b
                a, b = b, tmp
            return tmp

test = Solution()

print(test.climbStairs(35))