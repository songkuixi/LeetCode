from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        map = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }
        res = []
        for d in digits:
            if len(res) == 0:
                res.extend(map[d])
            else:
                r_len = len(res)
                for i in range(r_len):
                    for letter in map[d]:
                        res.append(res[i] + letter)
                res = res[r_len:]
        return res
