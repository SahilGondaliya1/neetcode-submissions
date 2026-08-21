class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # what actions are repeating the multiplication : if the number is not targeted it is multiplied iterativly. which cane be optimized 
        # what is common ? -> the mutilplication .
        product = 1
        zero = False
        for integer in nums:
            if integer == 0 and not zero:
                zero = True
            elif integer == 0 and zero:
                product = 0
            else:
                product *= integer

        output = []
        for integer in nums:
            if integer != 0 :        
                if not zero :
                    output.append(int(product/integer))            
                else:
                    output.append(0)
            else:
                output.append(int(product))
            
        return output