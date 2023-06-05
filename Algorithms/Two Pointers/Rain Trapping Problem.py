class Solution:
    def trap(self, height) -> int:
        leftMax = [0]*len(height)
        rightMax = [0]*len(height)
        
        #finding the heighest point till that index
        for i in range(1,len(leftMax)):
            leftMax[i] = max(leftMax[i-1],height[i-1])
        
        #finding the heighest point till that index in reverse order
        for i in range(len(rightMax)-2,-1,-1):
            rightMax[i] = max(rightMax[i+1],height[i+1])
        
        result = 0
        
        #calc the water capacity at each index by taking the min of both max height from left and right side
        for i in range(len(height)):
            capacity = min(leftMax[i],rightMax[i])-height[i]
            if capacity>0:
                result+=capacity
                
        return result

if __name__ == '__main__':   
    calculate_water = Solution()
    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    print(calculate_water.trap(height))