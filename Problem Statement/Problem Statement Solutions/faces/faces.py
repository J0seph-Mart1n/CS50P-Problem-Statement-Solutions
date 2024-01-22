def convert():
    sentence = input()
    for _ in range(len(sentence)):
        if ':)' in sentence:
            sentence = sentence.replace(':)','🙂')
        elif ':(' in sentence:
            sentence = sentence.replace(':(','🙁')
    print(sentence)

def main():
    convert()

if __name__ == '__main__':
    main()
