class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def rob_linear(houses: List[int]) -> int:
            two_houses_back = 0
            one_house_back = 0

            for money in houses:
                current = max(
                    one_house_back,
                    two_houses_back + money
                )

                two_houses_back = one_house_back
                one_house_back = current

            return one_house_back

        exclude_last = rob_linear(nums[:-1])
        exclude_first = rob_linear(nums[1:])

        return max(exclude_last, exclude_first)