class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        ans =[0] * n
        for i in range(n):
            rightmax = -1
            for j in range(i+1, n):
                rightmax = max(rightmax, arr[j])
            ans[i] = rightmax
        return ans
            