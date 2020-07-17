#!python

import cgi, os
form = cgi.FieldStorage()
pageId = form["pageId"].value


os.remove('data/'+pageId)#data폴더에서 페이지를 삭제한다

#Redirection
print("Location: index.py")#index페이지로 이동한다
print()