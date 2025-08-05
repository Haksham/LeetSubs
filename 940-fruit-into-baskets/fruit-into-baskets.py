class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        n = len(fruits)
        if n <= 2:
            return n
        a, b = -1, -1
        last_b_count = 0
        curr_len = 0
        max_len = 0
        for fruit in fruits:
            if fruit == a or fruit == b:
                curr_len += 1
            else:
                curr_len = last_b_count + 1
            if fruit == b:
                last_b_count += 1
            else:
                a, b = b, fruit
                last_b_count = 1
            max_len = max(max_len, curr_len)
        return max_len
        