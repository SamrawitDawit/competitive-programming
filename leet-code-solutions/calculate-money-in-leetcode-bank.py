class Solution:
    def totalMoney(self, n: int) -> int:
        day, money, total= 1, 0, 0
        prev_monday_money = 0
        while day <= n:
            if day%7 == 1:
                i = prev_monday_money + 1
                prev_monday_money = i
            else:
                i += 1 
            total += i
            day += 1
        return total
        # previous = 1
        # total = 0
        # while previous + 7 < n:
        #     last = previous + 6
        #     total += (previous + last)/2
        #     previous += 1
        # total += (previous + n)/2
        # return total
