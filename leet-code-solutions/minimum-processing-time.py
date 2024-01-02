class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        tasks.sort()
        processorTime.sort()
        processors_max = []
        higherTask = len(tasks)-1
        for i in range(len(processorTime)):
            processors_max.append(processorTime[i]+tasks[higherTask])
            higherTask -= 4
        return max(processors_max)