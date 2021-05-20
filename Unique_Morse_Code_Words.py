class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        word = {
        "a": ".-",
        "b": "-...",
        "c": "-.-.",
        "d": "-..",
        "e": ".",
        "f": "..-.",
        "g": "--.",
        "h": "....",
        "i": "..",
        "j": ".---",
        "k": "-.-",
        "l": ".-..",
        "m": "--",
        "n": "-.",
        "o": "---",
        "p": ".--.",
        "q": "--.-",
        "r": ".-.",
        "s": "...",
        "t": "-",
        "u": "..-",
        "v": "...-",
        "w": ".--",
        "x": "-..-",
        "y": "-.--",
        "z": "--.."
        }
        ans = []
        mors = []
        for i in words:
            temp = ""
            for j in i:
                temp+=word[j]
            mors.append(temp)
        for x in mors:
            if x not in ans:
                ans.append(x)
        return len(ans)