class Solution:
    def minNumberOfHours(self, initialEnergy: int, initialExperience: int, energy: List[int], experience: List[int]) -> int:
        hours = 0

        s = sum(energy)
        if initialEnergy <= s:
            hours += s - initialEnergy + 1

        cur = initialExperience
        for e in experience:
            if cur <= e:
                need = e - cur + 1
                hours += need
                cur += need
            cur += e

        return hours