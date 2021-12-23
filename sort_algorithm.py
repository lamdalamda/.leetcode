import numpy as np
class sort_algorithms():
    def __init__(self,nums):
        self.nums=nums
        self.lens=len(nums)
        self.index_upper=len(nums)-1
    def swap(self,nums,index1,index2):
        tmp=nums[index1]
        nums[index1]=nums[index2]
        nums[index2]=tmp
        return nums
        
    def validate_increasing(self):
        for i in range(0,self.lens-1):
            if self.nums[i]>self.nums[i+1]:
                return False
        return True
    def validate_decreasing(self):
        for i in range(0,self.lens-1):
            if self.nums[i]<self.nums[i+1]:
                return False
        return True            

class mergesort(sort_algorithms):

    def mergesort(self,nums):
        if len(nums)==1:
            return nums
        if len(nums)==2:
            if nums[0]<=nums[1]:
                return nums
            return [nums[1],nums[0]]
        resultlist = []
        part1=self.mergesort(nums[0:int(len(nums)/2)])
        part2=self.mergesort(nums[int(len(nums)/2):])
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
    
class insitu_mergesort(sort_algorithms):
    def __init__(self,nums):
        sort_algorithms.__init__(self,nums)

           
            
            
            
    
    
class index_sort(object):
    def index_sort(self,nums):
        hashdict={}
        result=[]
        for i in range(min(nums),max(nums)):
            hashdict[i]=0
        for i in nums:
            hashdict[i]+=1
        for i in range(min(nums),max(nums)):
            result=result+hashdict[i]*i
        return result
    

class quick_sort(sort_algorithms):
    def __init__(self,nums):
        sort_algorithms.__init__(self,nums)

class quick_sort_beginning_pivot(quick_sort):
    #pivot is the beginning element
    def __init__(self,nums):
        quick_sort.__init__(self,nums)
    
    def sorting_routine(self,nums):
        # input: array to be sort, with the 1st element be the pivoting element
        
        #pivot=self.nums[0]
        # pivot index=0
        pivot=nums[0]
        i=1 # index(1,i) are nums < pivot
        
        """
        j=1 # index (i,j) are nums>pivot
        
        # original
        while j<self.lens:
            if nums[j]>self.pivot:
                j=j+1
            else:
                self.swap(nums,i,j)
                i=i+1
                j=j+1
        """
        # more easily
        for j in range(1,self.lens):     
            if nums[j]<pivot:
                self.swap(nums,i,j)
                i=i+1

        self.swap(nums,0,i-1)
        
        return nums,i,j,pivot
    
    def check_sorting_routine(self,nums):
        tmp=self.sorting_routine()
        if len(nums[tmp[1]:])==0:
            return True
        if max(nums[0:tmp[1]])<=tmp[3] and (min(nums[tmp[1]:])>=tmp[3]):
            return True
        else:
            return False
        
    def choose_pivot_randomly(self,nums):
        pivot_index=np.random.randint(0,len(nums)-1)#include upper bond lennunms-1
        
        self.swap(nums,0,pivot_index)
        return nums
        pass
    
    def random_pivot_sort(self):
        pass

    
            
        
        
    
       
class ith_order(sort_algorithms):
    def __init__(self,nums):
        sort_algorithms.__init__(self,nums)
        
    def ith_order_random(self,nums):
        pass
       
    def ith_order_deterministic_select_pivot(self,nums):
        pass
       
            
            
if __name__=="__main__":
    import numpy as np
    for i in range(0,10000):
        random_array=np.random.randint(0,20,15)
        print(random_array)
        a=quick_sort_beginning_pivot(random_array)
        print(a.random_pivot_sort())
        
            
        