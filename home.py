#!/usr/bin/env python3
import cgi
import boto3
import cgitb
import os
from boto3.dynamodb.conditions import Key, Attr
cgitb.enable()

form = cgi.FieldStorage()
dynamodb = boto3.resource('dynamodb');
table = dynamodb.Table('messages')

print("<html>")
print("<header><title>Message Board</title></header>")
print("<body>")
print("<h1>Welcome to the message board!</h1>")
print('<form action="post.py" method="post">')
print("User Name:<br>")
print('<input type="text" name="userName">')
print('<input type="text" name="messageText">')
print('<input type="submit" value="Submit">')
print('</form>')
if "userName" in form:
    print("<p>Posts for user:", form["userName"].value)
    response = table.query(
        KeyConditionExpression=Key('userName').eq(form["userName"].value)
    )
    for i in response['Items']:
        print("<p>", i['userName'], ":", i['messageText'], "</p>")
else:
    response = table.scan()
    for i in response['Items']:
        print("<p>", i['userName'], ":", i['messageText'], "</p>")
print("</body>")
print("</html>")
