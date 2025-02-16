class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        res = None
        arr = [-1] * (2 * n - 1)
        used = [False] * (n + 1)

        def backtrack(l):
            nonlocal res
            if l == len(arr):
                res = arr[:]
                return True

            if arr[l] != -1:
                return backtrack(l + 1)

            for num in range(n, 0, -1):
                if used[num]:
                    continue

                r = l + num if num > 1 else l
                if r < len(arr) and arr[r] == -1:
                    arr[l], arr[r] = num, num
                    used[num] = True

                    if backtrack(l + 1):
                        return True

                    arr[l], arr[r] = -1, -1
                    used[num] = False

            return False

        backtrack(0)
        return res