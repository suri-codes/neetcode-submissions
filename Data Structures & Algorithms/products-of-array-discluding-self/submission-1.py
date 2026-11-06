class Solution:

    
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        new = []
        pre = 1
        post = my_mult(nums[1:])

        for idx, num in enumerate(nums):
            #print(f"pre: {pre}, post {post}")
            new.append(pre * post)
            pre *= num
            #length check
            if idx + 1 < len(nums):
                #zero check
                next = nums[idx+1]
                if next == 0:
                    post = my_mult(nums[idx+2:])
                else:
                    post = int(post / nums[idx+1])
            else:
                break

        return new



def my_mult(nums: List[int])->int:
    running = 1
    for num in nums:
        running *= num
    
    return running