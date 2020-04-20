def histogram(f):
    with open(f,"r") as f:
        text = f.read().lower()
        result = dict()
        for i in text:
            if i in result.keys():
                result[i] += 1
            elif i.isalpha():
                result[i] = 1
    return result
print(histogram("document.txt"))
