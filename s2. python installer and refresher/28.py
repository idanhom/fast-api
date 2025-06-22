grade = 89

try:
    if 0 <= grade <= 59:
        print("F")
    elif 60 <= grade <= 69:
        print("D")
    elif 70 <= grade <= 79:
        print("C")
    elif 80 <= grade <= 89:
        print("B")
    elif 90 <= grade <= 100:
        print("A")
except:
    ValueError(print("hej"))