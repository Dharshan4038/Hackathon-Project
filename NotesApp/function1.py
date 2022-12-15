from datetime import datetime 
from googletrans import Translator
import json

translator1=Translator()
def cmp(x, y):
    if x == y:
        return 0
    if x > y:
        return 1
    return -1

def translate_to_tamil(sentence,title=False):
    tamil_txt = translator1.translate(sentence,src='en',dest='ta')
    if(title):
        a = title_dection(tamil_txt.text)
        return a  
    return tamil_txt.text

def translate_to_english(sentence):
    english_txt = translator1.translate(sentence,src='ta',dest='en')
    return english_txt.text

def title_dection(title):
    word_list = title.split(" ")
    new_word = []
    for i in word_list:
        if(translator1.detect(i).lang =='ta'):
            new_word.append(i)
        else:
            continue
    return " ".join(new_word)


def note_validation(title,content):
    tamil_title = translate_to_tamil(title,True)
    tamil_content = translate_to_tamil(content)
    # print(tamil_title,tamil_content)
    data = { 'NoteTitle' : tamil_title,
            'NoteContent': tamil_content,
            'NoteCreated': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
    return data

    
