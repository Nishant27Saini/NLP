import spacy
import subprocess
english = spacy.load("en_core_web_sm")
ch = input("enter your choice: ")
doc1 = english(ch)
#wakeup = english(ch)
myaction = []
for i in doc1:
    if i.pos_ == "VERB":
        #print(i.text, i.lemma_)
        myaction.append(i.lemma_)
y = True 
for i in doc1:
    if i.dep_ == "neg":
        y = False
#if wakeup[0].text == "hey" and wakeup[1].text == "nishant":
if doc1[0].text == "hey" and doc1[1].text == "nishant":
    if "date" in ch and "run" in myaction and y:
        print(subprocess.getoutput("date /t"))
    elif "cal" in ch and "run" in myaction and y:
        print("cal")
    elif "player" in ch and "run" in myaction and y:
        subprocess.getoutput("wmplayer")
    elif "chrome" in ch and "run" in myaction and y:
        subprocess.getoutput("chrome")
    else:
        print("not supported")
else:
    print("donot able to find wakeup word")


