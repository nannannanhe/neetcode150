class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total_product = 1
        zero_nums = 0
        for num in nums:
            if num == 0:
                zero_nums += 1
            else:
                total_product *= num
        output = []
        for num in nums:
            if zero_nums > 1:
                output.append(0)
            elif num == 0:
                output.append(total_product)
            elif zero_nums != 0:
                output.append(0)
            else:
                output.append(int(total_product/num))
        
        return output

        