#
# @lc app=leetcode id=146 lang=python3
#
# [146] LRU Cache
#

# @lc code=start
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dict={}
        self.leastRecentlyUsed=0
        

    def get(self, key: int) -> int:
        if key in self.dict:
            return self.dict[key]
        return -1


    def put(self, key: int, value: int) -> None:
        
        pass
    
class LRUnode:
    def __init__(self,key=-1,value=-1):
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end

