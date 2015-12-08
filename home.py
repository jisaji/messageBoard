#!/usr/bin/env python3
import cgi
import boto3
import cgitb
import os
import time
from boto3.dynamodb.conditions import Key, Attr
cgitb.enable()

form = cgi.FieldStorage()
dynamodb = boto3.resource('dynamodb');
table = dynamodb.Table('messages')

print("<html>")
print("<header><title>Message Board</title></header>")
print("<body>")
print("<h1>Welcome to the message board!</h1>")
if "userName" not in form or "messageText" not in form:
    print("<h1>Error, please put userName and messageText in form</h1>")
else:
    response = table.put_item(
        Item={
            'userName': form["userName"].value,
            'timestamp': int(time.time()),
            'messageText': form["messageText"].value,
        }
    )
    print("<h1>New Message Successful</h1>")
print("</body>")
print("</html>")
