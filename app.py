from flask import Flask, redirect, url_for, request,render_template
import os
import sys
import json
from watson_developer_cloud import ConversationV1

conversation = ConversationV1(
    username='Your_username',
    password='Your_password',
    version='2017-04-21')
    
conversation_chat = ConversationV1(
     username='Your_username',
    password='Your_password',
    version='2017-04-21')

workspace_id = 'your_workspace_id'
workspace_chat='your_workspace_id' 

app = Flask(__name__)

@app.route('/')
def index():
   return render_template('index.html')
   
@app.route('/temp',methods=['POST'])
def temp():
  message_input=request.form['mes']
  try:
    response = conversation.message(workspace_id=workspace_id, message_input={'text':message_input})
    #Respond "chitchat" if the input cannot find an appropriate response in your first workspace
    if response["output"]["text"][0]=='chitchat':
     		response = conversation_chat.message(workspace_id=workspace_chat, message_input={'text':message_input})
    return response["output"]["text"][0]
  except:
    return "Have you set up your own watson credentials?"
   
   	
if __name__ == '__main__':
    app.run(debug = True)
    # app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)))
