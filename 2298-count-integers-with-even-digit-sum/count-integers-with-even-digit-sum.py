class Solution:
    def countEven(self, num):
        count = 0
        for n in range(1, num + 1):
            if sum(int(d) for d in str(n)) % 2 == 0:
                count += 1
        return count