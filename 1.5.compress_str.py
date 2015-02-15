chars = "aasssdgggg"
i = 0
count = 0
result = ""
while i < len(chars):
    chr = chars[i]
    if count == 1:
        result += chr
    if i + 1 < len(chars):
        if chars[i + 1] != chr: 
            result += str(count)
            count = 1
        else:
            count += 1
    else:
        result += str(count)
    i += 1

print(result)