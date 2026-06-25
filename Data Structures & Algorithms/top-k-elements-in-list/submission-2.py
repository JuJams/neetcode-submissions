class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # time: O(n) with bucket sort

        # step 1: frequency map
        # nums=[5,5,5,5,8,8,3]
        vals = {}
        result = []
        # vals = {5: 4, 8: 2, 3: 1}
        for num in nums:
            if num not in vals:
                vals[num] = 1
            else:
                vals[num] += 1
        # step 2: make buckets of length  nums + 1
        buckets = [[] for _ in range(len(nums)+1)]
            # buckets = [[], [], [], [], [], [], [], []]
            #    index.   0.  1.  2.  3.  4.  5.  6.  7
        # step 3: drop each number into the index bing the frequency
        for num in vals:
            count = vals[num]
            buckets[count].append(num)
            # buckets = [[], [3], [8], [], [5], [], [], []]
            #    index.   0.  1.  2.  3.  4.  5.  6.  7
        # step 4: loop in reverse check if not empty and and stop when len(result) = k
        for f in range(len(buckets)-1,0,-1):
            for num in buckets[f]:
                result.append(num)
                if len(result) == k:
                    return result
            

       





        # time: O(n) to count, O(n log n) to sort so O(n log n)
        # space: O(n)
        # result = []
        # vals = {}
        # for num in nums:
        #     if num not in vals:
        #         vals[num] = 1
        #     else:
        #         vals[num] += 1
        # sorted_vals = sorted(vals.items(), key = lambda item: item[1], reverse = True)
        # for num, count in sorted_vals[:k]:
        #     result.append(num)
        # return result

        
























        # Optimal soultion would be using a bucket sort after the count frequency map
        # Bucket sort avoids sorting by using the frequency as the indeices of the array
        # Time Complexity: O(n)
        # Space Complexity: O(n)
        # count = {}
        # for i in range(len(nums)):
        #     key = nums[i]
        #     if key not in count:
        #         count[key] = 0
        #     count[key] += 1
        # print (count)
        # bucket = [ [] for _ in range(len(nums)+1)]
        # print(bucket)
        # for num in count:
        #     freq = count[num]
        #     bucket[freq].append(num)
        # print(bucket)
        # result = []
        # for freq in range(len(bucket)-1,-1,-1):
        #     for num in bucket[freq]:
        #         result.append(num)
        #         if len(result) == k:
        #             return result



        # # Time Complexity: O(n log n)
        # # Space Complexity: O(n)
        # count = {}
        # for i in range(len(nums)):
        #     key = nums[i]
        #     if key not in count:
        #         count[key] = 0
        #     count[key] += 1
        # print(count)
        # # Count: Using the nums[i] as the key and how many time that same number occurs as the value 
        # # Left to do: display only the k most frequent in the count hashmap
        # dictToList = [ (i, count[i]) for i in count]
        # dictToList.sort(key=lambda x: x[1], reverse=True)
        # print(dictToList)
        # result = []
        # for top in range(k):
        #     result.append(dictToList[top][0])
        # return result

       

        
