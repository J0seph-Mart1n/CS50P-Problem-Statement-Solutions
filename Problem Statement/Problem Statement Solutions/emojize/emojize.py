import emoji
import sys
sentence = input("Input: ")
if ":earth_asia" in sentence:
    new = sentence.replace(":earth_asia:","🌏")
    print(new)
    sys.exit()
if ":thumbsup:" in sentence:
    new2 = sentence.replace(":thumbsup:","👍")
    print(new2)
    sys.exit()
print("Output:",emoji.emojize(sentence))
