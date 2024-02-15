class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        moves = 0
        while target > 1:
            if maxDoubles == 0:
                moves += (target-1)
                target = 1
            elif target %2 == 0 and maxDoubles > 0:
                moves += 1
                maxDoubles -= 1
                target = target//2
            elif target%2 == 1 and maxDoubles >0:
                moves += 2
                maxDoubles -= 1
                target = ((target-1) // 2) 
        return moves
            
