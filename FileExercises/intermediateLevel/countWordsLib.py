def countWords(filePath):
    with open(filePath, "r") as file:
        content=file.read()
        words = content.split()
        return len(words)
