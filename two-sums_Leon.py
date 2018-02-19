import time

"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""

nums = [0, 27, 27, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 2]
target = 2
sol = []
i = 0
x = 0


start_time = time.time()
enum_ary = enumerate(nums)
#for p in range(5000000):
for idx_o, val_o in enum_ary:
    for idx_i, val_i in enum_ary:
        if(idx_i <= idx_o):
            continue
        if(target == (val_o + val_i)):
            sol.append(idx_o)
            sol.append(idx_i)
            print ("Indices for the given input are {} and {} at position {} and {}".format(val_o, val_i, idx_o, idx_i))
            break

print("Code from Leon --- %s seconds ---" % (time.time() - start_time))

start_time = time.time()
sol = []
enum_aryr = enumerate(nums)
#for p in range(5000000):
for i, a in enum_aryr:
    for x, b in enum_aryr:
        if (i >= x):
            continue
        if (i < x) and (target == a + b):
            sol.append(i) 
            sol.append(x)
            print ("Indices for the given input are at position {} and {}".format(i,x))
            break
            

#    if len(sol) == 2:
#        print ("Indices for the given input are at position {} and {}".format(sol[0], sol[1]))
#    else: 
#        print ("No indices found.")

print("Code from Roman --- %s seconds ---" % (time.time() - start_time))



