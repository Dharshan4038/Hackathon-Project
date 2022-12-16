from datetime import datetime 
from googletrans import Translator
import json
import os
import sendgrid
from sendgrid.helpers.mail import *
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
import requests
import json

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

#translate english to tamil
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
    txt=" ".join(new_word)
    if txt=="":
        txt="தலைப்பு"
    return txt


def note_validation(title,content):
    tamil_title = translate_to_tamil(title,True)
    tamil_content = translate_to_tamil(content)
    # print(tamil_title,tamil_content)
    data = { 'NoteTitle' : tamil_title,
            'NoteContent': tamil_content,
            'NoteCreated': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
    return data

    
def send_email(t_email,sub,cont):
    message = Mail(
    from_email='webapp.tamilnotes@gmail.com',
    to_emails=t_email,
    subject=sub,
    html_content='<strong>'+cont+'</strong>')
    try:
        sg = SendGridAPIClient(data_env['sendgrid_key'])
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e)

    return response.status_code

def search_note(title):    
    response_API = requests.get('http://127.0.0.1:8000/note/')
    data=response_API.json()
    t_title=translate_to_tamil(title)
    data1=[]
    for i in data: #get responce as list of dict
        if i['NoteTitle'].find(t_title) != -1:
            data1.append(i)
    for n,i in enumerate(data): #get responce as list of dict
        if i['NoteContent'].find(t_title) != -1:
            if data1[n]['NoteId'] != i['NoteId']:
                data1.append(i)
    return data1


# def app(data,list1):
#     for i in list1
#     if(data['NoteId']==list1[i]['NoteId'])