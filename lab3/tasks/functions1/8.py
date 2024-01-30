def spy_game(nums):
    counter = 0
    for x in range(0, len(nums)):
        if(nums[x] == 0):
            counter+= 1
        if(nums[x] == 7  and counter >= 2):
            return True
        
    return False


# tests = [[1,2,4,0,0,7,5],[1,0,2,4,0,5,7],[1,7,2,0,4,5,0]]
# for x in tests: 
#     print(spy_game(x))
    