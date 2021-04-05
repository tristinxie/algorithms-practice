"""
There are several cards arranged in a row, and each card has an associated number of points The 
points are given in the integer array cardPoints.

In one step, you can take one card from the beginning or from the end of the row. You have to take 
exactly k cards.

Your score is the sum of the points of the cards you have taken.

Given the integer array cardPoints and the integer k, return the maximum score you can obtain.
"""
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        leftSum = [0]
        rightSum = [0]
        combined = []
        for i in range(k):
            leftSum.append(cardPoints[i]+leftSum[i])
            rightSum.append(cardPoints[len(cardPoints)-i-1]+rightSum[i])
        for j in range(k+1):
            combined.append(leftSum[j] + rightSum[k-j])
            
        return max(combined)