class Solution:
    def bestClosingTime(self, customers: str) -> int:
        count = customers.count('Y')
        minimum = count
        min_indx = 0
        for indx in range(len(customers)):
            if customers[indx] == 'Y':
                count -= 1
            else:
                count += 1
            if count < minimum:
                minimum = count 
                min_indx = indx+1
        return min_indx