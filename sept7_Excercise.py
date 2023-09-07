
# merge the lists in increasing order

nums1 = [1,2,3,7]
nums2 = [2,5,8]

num_list = []
num_list_sorted = [0]*7
index = 0

for i in nums1:
    num_list.append(i)

for j in nums2:
    num_list.append(j)

print(num_list)

index = 0
for num in num_list:
    
    for nums in num_list:
        if nums <= num:
            
            num_list_sorted[index] = num
            num_list.remove(nums)
            index += 1
        else:
            continue

print(num_list)
print(num_list_sorted)