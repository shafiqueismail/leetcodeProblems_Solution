class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} # First make a dictionary/hashmap to see the frequency of each number.
        
        for i in nums:
            count[i] = count.get(i, 0) + 1 # Where gonna span through the entire list and store the amount of frequencies for each number. if its a unique number we assume it to be zero and add 1 to frquency. 

        # we need ot turn it into a list beacuse we cant retireve the highest freuqency strait from teh dictoanry but its easier with an array using the sort()
        arr = []
        for num, cnt in count.items(): # this is a classic line to turn a dictionary into an list. using the .items() with a for loop
            arr.append([cnt, num])
        arr.sort() # now it will get sorted the list, it sorts using the first index. For exmaple: arr = [[1, 3], [2, 2], [3, 1]]

        res = []
        while len(res) < k: # will loop until it recahes the kth most frequency as desried. 
            res.append(arr.pop()[1]) # it will pop out the last elemenet sinc eit has the largest frequency is in the back when doing sort. and the [1] will be the key ([0] refers to the frequency)
        return res

#Reminders:
# my_dict = {"apple": 3}

# print(my_dict.get("apple", 0))   # Output: 3
# print(my_dict.get("banana", 0))  # Output: 0 ← because "banana" doesn't exist yet
        
        
