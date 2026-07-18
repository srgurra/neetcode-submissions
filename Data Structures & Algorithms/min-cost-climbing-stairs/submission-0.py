class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        one_step_before = cost[1]
        two_steps_before = cost[0]

        for i in range(2, len(cost)):
            current = cost[i] + min(one_step_before, two_steps_before)

            two_steps_before = one_step_before
            one_step_before = current

        return min(one_step_before, two_steps_before)