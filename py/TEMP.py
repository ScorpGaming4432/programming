def splitOnThree(str):
    return [str[start:start+3] for start in range(0, len(str), 3)]
print(splitOnThree('abcdefghiw'))