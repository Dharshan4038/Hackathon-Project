from datetime import datetime 
from googletrans import Translator
import json
import os
import sendgrid
from sendgrid.helpers.mail import *

p=os.path.dirname(__file__)+"\..\..\data.json"
f=open(p,"r")
data_env = json.load(f)

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

    
def send_email(f_email,t_email,subject,cont,):
    sg = sendgrid.SendGridAPIClient(api_key=data_env['sendgrid_key'])
    from_email = Email(f_email)
    to_email = To(t_email)
    content = Content("text/plain", cont)
    mail = Mail(from_email, to_email, subject, content)
    response = sg.client.mail.send.post(request_body=mail.get())
    print(response.status_code)
    print(response.body)
    print(response.headers)
    return response.status_code