class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        return heapq.nlargest(k, count.keys(), key=count.get)



#Reminders:
# my_dict = {"apple": 3}

# print(my_dict.get("apple", 0))   # Output: 3
# print(my_dict.get("banana", 0))  # Output: 0 ← because "banana" doesn't exist yet
        
