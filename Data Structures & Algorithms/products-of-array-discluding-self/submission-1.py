class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # prefix
        pre = 1
        result = [1] * len(nums)
        for i in range(1, len(nums)):
            pre *= nums[i-1]
            result[i] = pre
        print(result)
        post = 1 # 6 24 48 48
        for i in range(len(nums)-1,-1,-1):
            result[i] *= post
            post *= nums[i]
        return result
            
        # prefix = [1]
        # postfix = []
        # result = []
        # pre = 1
        # for i in range(1,len(nums)):
        #     pre *=  nums[i-1]
        #     prefix.append(pre)
        # print(prefix)
        # post = 1
        # for i in range(len(nums)-1,-1,-1):
        #     postfix.append(post)
        #     post *= nums[i]
        # print(postfix)
        # postfix.reverse()
        # for i in range(len(nums)):
        #     val = prefix[i] * postfix[i]
        #     result.append(val)
        # print(result)
        # return result
