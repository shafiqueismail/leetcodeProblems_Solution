class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} # this is for the dictionary (for exmaple: {1: 3, 2: 2, 3: 1})
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        arr = []
        for num, cnt in count.items():
            arr.append([cnt, num])
        arr.sort()

        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res



#Reminders:
# my_dict = {"apple": 3}

# print(my_dict.get("apple", 0))   # Output: 3
# print(my_dict.get("banana", 0))  # Output: 0 ← because "banana" doesn't exist yet
        
        
