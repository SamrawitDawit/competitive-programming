class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        minimum = None
        for letter in letters:
            if letter > target:
                if not minimum:
                    minimum = letter
                if letter < minimum:
                    minimum = letter
        return minimum if minimum else letters[0]