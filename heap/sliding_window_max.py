import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maxHeap = [ (-nums[i], i) for i in range(k) ]
        heapq.heapify(maxHeap)

        output = []
        startWindow = 0
        endWindow = k-1
        while endWindow<len(nums):
            while True:
                maxVal, index = maxHeap[0] #peek maxHeap
                if index>=startWindow and index<=endWindow: 
                    break #stops when peek maxHeap is in sliding window
                heapq.heappop(maxHeap) #remove elements out of sliding window
            output.append( -maxVal ) 
            startWindow += 1
            endWindow += 1
            if endWindow<len(nums):
                if nums[endWindow] > -maxVal:
                    maxHeap = [(-nums[endWindow], endWindow)]
                else:
                    heapq.heappush(maxHeap, (-nums[endWindow], endWindow))

        return output