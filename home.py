#!/usr/bin/env python3
import cgi
import boto3
import cgitb
import os
import datetime
from boto3.dynamodb.conditions import Key, Attr
cgitb.enable()

form = cgi.FieldStorage()
dynamodb = boto3.resource('dynamodb');
table = dynamodb.Table('messages')

def printItems(items):
    sortedItems = sorted(items, key=lambda post: post['timestamp'])
    for i in sortedItems:
        date = datetime.datetime.fromtimestamp(int(i['timestamp'])).strftime('%Y-%m-%d %H:%M:%S')
        print("<p>", i['userName'], ":", i['messageText'], " -  ", date, "</p>")


def printNewPostForm():
    print('<form action="post.py" method="post">')
    print("Add A New Post:<br>")
    print('<input type="text" name="userName" placeholder="Your Name">')
    print('<input type="text" name="messageText" placeholder="Message">')
    print('<input type="submit" value="Submit">')
    print('</form>')


def printPostsForUserForm():
    print('<form action="home.py" method="get">')
    print("Find Posts for User:<br>")
    print('<input type="text" name="userName" placeholder="User Name">')
    print('<input type="submit" value="Submit">')
    print('</form>')

print("<html>")
print("<header><title>Message Board</title></header>")
print("<body>")
print("<h1>Welcome to the message board!</h1>")
printNewPostForm()
printPostsForUserForm()
if "userName" in form:
    print("<p>Posts for user:", form["userName"].value)
    response = table.query(
        KeyConditionExpression=Key('userName').eq(form["userName"].value)
    )
    printItems(response['Items'])
    print('<a href="home.py">See All Posts</a>')
else:
    response = table.scan()
    printItems(response['Items'])
print("</body>")
print("</html>")

