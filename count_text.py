with open("merge.txt", "r") as f:
    text= f.read()

char_count= len(text)

word_count= len(text.split())

spaces_count= text.count (" ")

lines_count= len(text.splitlines())

print("Final Analysis :")
print("character ", char_count)
print("words", word_count)
print("lines", lines_count)
print("spaces", spaces_count)