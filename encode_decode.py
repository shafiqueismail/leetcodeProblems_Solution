class Solution:

    def encode(self, strs: List[str]) -> str:
        # Format: length_of_string + '#' + string
        newString = ""
        for i in strs:
            newString += str(len(i)) + "#" + i
        return newString

    def decode(self, s: str) -> List[str]:
        i = 0
        result = []
        while i < len(s):
            # Get the length of the next string
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            # Extract the actual string
            word = s[j + 1: j + 1 + length]
            result.append(word)
            i = j + 1 + length
        return result
