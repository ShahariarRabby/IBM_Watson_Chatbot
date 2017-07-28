
This is a Watson chatbot build with IBM Watson conversation and Flask. 

This chatbot uses two Watson conversation workspaces, one for the main purpose of this chatbot, and the 
other deals with chitchat inputs. 

## Credentials

Change your IBM Watson credentials in the app.py file as below:

```
conversation = ConversationV1(
    username='Your_username',
    password='Your_password',
    version='2017-04-21')

workspace_id = 'your_workspace_id'
```

