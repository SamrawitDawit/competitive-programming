class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        dic = {word:i for i,word in enumerate(list1)}
        index_sum = float("inf")
        for i in range(len(list2)):
            if list2[i] in dic:
                if i + dic[list2[i]] < index_sum:
                    index_sum = i + dic[list2[i]]
                    answer = []
                    answer.append(list2[i])
                    print(answer)
                elif i + dic[list2[i]] == index_sum:
                    answer.append(list2[i])
        return answer
                    

 
