class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        
        assume = []
        result = [0] * len(A)
        
        for char in A:
            if char == 0:
                assume.append(1)
            else:
                assume.append(-1)
        result[0] = assume[0]
        for i in range(1,len(result)-1):
            result[i]= result[i-1] + assume[i]
        count = result.count(0)
        return count
        
        


numbers = [1,1,-1,-1,1,-1]
number2 = [0,0,1,1,0,1,]

Solution().solve(number2)

    

