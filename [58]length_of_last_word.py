def lengthOfLastWord(s: str):
    s = s.split()
    return len(s[-1])


lengthOfLastWord(" fly me to the moon")
