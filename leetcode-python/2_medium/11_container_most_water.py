######### LeetCode Problem N°11 - Container With Most Water (Medium) ################
# You are given an integer array height of length n. 
# There are n vertical lines drawn such that the two 
# endpoints of the ith line are (i, 0) and (i, height[i]).
# Find two lines that together with the x-axis form a container,
# such that the container contains the most water.
#
# Return the maximum amount of water a container can store.
# Notice that you may not slant the container.
#
# Example 1:
# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. 
# In this case, the max area of water (blue section) the container can contain is 49.

# Example 2:
# Input: height = [1,1]
# Output: 1

# Constraints:
# n == height.length
# 2 <= n <= 105
# 0 <= height[i] <= 104

class Solution:
    def maxArea(self, height: list[int]) -> int:
        '''
        area = base*altura
          - base = x2 - x1
          - altura = min(height[x1], height[x2])

        Comienzo probando los extremos -> Calculo el area. Luego:
        Si h1 < h2 -> muevo x1 a la derecha y continuo probando areas 
                      (ya que areas formadas entre x1 y x<x2 serán menores, no las calculo)
        Si h1 > h2 -> muevo x2 a la izquierda y continuo probando areas
                      (Viceversa, areas formadas entre x>x1 y x2 serán menores, no las calculo)
        '''

        # Inicializo variables
        max_area = 0
        x1, x2 = 0, len(height)-1

        while x1 < x2:
            area = (x2-x1) * min(height[x1], height[x2])
            max_area = max(max_area, area)
            
            # areas formadas entre x1 y x<x2 serán menores (las omito)
            if height[x1] <= height[x2]:
                x1 += 1
            # Viceversa, areas formadas entre x>x1 y x2 serán menores (las omito)
            else:
                x2 -= 1

        return max_area



        

