class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        ret = "11"
        for i in range(n - 2):
            prev = ret[0]
            cnt = 1
            new_ret = ""
            for num in ret[1:]:
                if num == prev:
                    cnt += 1
                else:
                    new_ret += str(cnt)
                    new_ret += prev
                    cnt = 1
                    prev = num
            new_ret += str(cnt)
            new_ret += prev
            ret = new_ret
        return ret