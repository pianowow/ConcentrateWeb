#how to load the files to the database

#in python power shell:

#navigate to the ConcentrateWeb project directory
#confirm manage.py, db.sqllite3, en15.txt, and reduced.txt exist

#python manage.py shell

#from the python interactive shell:

#open python file objects
f = open('en15.txt','r')
r = open('reduced.txt','r')

from django.core.files import File

#open django file objects
myf = File(f)
myr = File(r)

from concentrate.models import db_file

#clear the table
db_file.objects.all().delete()

#insert the file objects in the table (creates new .txt files, next to the ref files)
fdb = db_file(file_name='en15.txt',file=myf)
fdb.save()
rdb = db_file(file_name='reduced.txt',file=myr)
rdb.save()

#insert all the words in each file into the db tables
from concentrate.models import en15,reduced

for word in [word.upper().strip() for word in f]:
   w = en15(word=word)
   w.save()

for word in [word.upper().strip() for word in r]:
   w = reduced(word=word)
   w.save()


#close the file objects
f.close()
r.close()
myf.close()
myr.close()

