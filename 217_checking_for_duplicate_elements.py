class Solution:
    def check_duplicates(slef, nums:List[int]) -> bool:
        solution_set=set()

        for i in nums:
            if i in solution_set:
                return True
            else:
                solution_set.add(i)
        return False