class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for i in range(len(nums)):
            key = nums[i]
            if key not in count:
                count[key] = 0
            count[key] += 1
        print(count)
        # Count: Using the nums[i] as the key and how many time that same umbe roccurs as the value 
        # Left to do: display only the k most frequent in the count hashmap
        dictToList = [ (i, count[i]) for i in count]
        dictToList.sort(key=lambda x: x[1], reverse=True)
        print(dictToList)
        result = []
        for top in range(k):
            result.append(dictToList[top][0])
        return result
        
