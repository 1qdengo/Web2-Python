#!python

import cgi
form = cgi.FieldStorage()
title = form["title"].value
description = form["description"].value

opened_file = open('data/'+title, 'w')  #data폴더에 파일을 작성한다
opened_file.write(description)
opened_file.close()

#redirection
print("Location: index.py?id="+title)
print()