class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        directory_dic = collections.defaultdict(list)
        for i in paths:
            j = i.split(" ")
            for k in j[1:]:
                directory_dic[k.split("(")[1]].append(j[0]+"/"+k.split("(")[0])
        answer = []
        for i in directory_dic.values():
            if len(i) > 1:
                answer.append(i)
        del directory_dic
        return answer
                

            