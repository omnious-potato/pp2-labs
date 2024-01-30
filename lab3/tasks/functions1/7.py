def has_33(nums):
    for x in range(0, len(nums) - 1):
        if(nums[x] == 3 and nums[x+ 1] == 3):
            return True
    return False




#Example usage
tests = [[1, 3, 1, 3],[1, 3, 3, 1],[1, 1, 3, 3, 4],[1, 1, 5, 3, 3],[1, 1, 5, 4, 3]]
for x in tests:
    print(f"Test: {x}, \tresult: {has_33(x)}")

