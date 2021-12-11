def normalsort(nums):
    if len(nums)==1:
        return nums
    if len(nums)==2:
        if nums[0]<=nums[1]:
            return nums
        return [nums[1],nums[0]]
    resultlist = []
    part1=normalsort(nums[0:int(len(nums)/2)])
    part2=normalsort(nums[int(len(nums)/2):])
    while len(part1)!=0 or len(part2)!=0:
        if len(part1)==0:
            resultlist.extend(part2)
            return resultlist
        if len(part2)==0:
            resultlist.extend(part1)
            return resultlist
        if part1[0]<part2[0]:
            resultlist.append(part1.pop(0))
        else:
            resultlist.append(part2.pop(0))
    return resultlist