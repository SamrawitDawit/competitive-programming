class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        dic = collections.defaultdict(int)
        for i in cpdomains:
            count, domain = i.split(' ')
            subdomains = domain.split('.')
            for j in range(len(subdomains)):
                dic['.'.join(subdomains[j:])] += int(count)
        lst = []
        for key, value in dic.items():
            lst.append(str(value)+" "+ key)
        return lst
