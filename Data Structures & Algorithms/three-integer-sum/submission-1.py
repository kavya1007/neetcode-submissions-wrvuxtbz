class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        

        for i, value in enumerate(nums):
            if value > 0:
                break
            
            if i > 0 and value == nums[i - 1]:
                continue

            s, e= i + 1, len(nums) - 1
            while s < e:
                threeSum = value + nums[s]+ nums[e]
                if threeSum >0:
                    e = e-1
                elif threeSum <0:
                    s = s+1
                else:
                    res.append([value,nums[s],nums[e]])
                    s+=1
                    e-=1
                    while nums[s] == nums[s-1] and s<e:
                        s+=1

        return res