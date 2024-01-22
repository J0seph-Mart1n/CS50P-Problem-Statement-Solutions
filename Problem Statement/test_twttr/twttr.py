def main():
    sentence = input("Input: ")
    result = shorten(sentence)
    print(result)

def shorten(word):
    a = list(word)
    i = 0
    while i<len(a):
        if i==len(a)-1:
            break
        if a[i]=='a' or a[i]=='A':
            a.pop(i)
            i=0
        elif a[i]=='e' or a[i]=='E':
            a.pop(i)
            i=0
        elif a[i]=='i' or a[i]=='I':
            a.pop(i)
            i=0
        elif a[i]=='o' or a[i]=='O':
            a.pop(i)
            i=0
        elif a[i]=='u' or a[i]=='U':
            a.pop(i)
            i=0
        i = i+1

    output = "".join(a)

    return ("Output:",output)



if __name__ == "__main__":
    main()
