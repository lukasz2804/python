##prace na plikach i katalogach
#-*- coding: utf-8 -*-

from os import *

print getcwd()

print getcwd()

print listdir('..')

print listdir(r'/home/student/PycharmProjects/untitled')

import fnmatch
print fnmatch.fnmatch('Python','P*n')
print fnmatch.fnmatch('Python','P*n')

print [x for x in listdir(r'/home/student/PycharmProjects/untitled')
if fnmatch.fnmatch(x,'*[61].*')]

import glob

for x in glob.glob(r'/home/student/PycharmProjects/untitled/*[61].*'):
    print x

#rozdzielenie na sciezke i plik
print path.split('/home/student/PycharmProjects/untitled/cw6.py')

for x in glob.glob(r'../*[61].*'):
    print path.split(x)[1]

print path.join('/','home')
print path.join(r'/','home')

print path.isabs(r'../cw6.py')
print path.isabs(r'/home/student/PycharmProjects/untitled/cw6.py')


print path.exists(r'/home/student/PycharmProjects/untitled/cw6.py')

print path.exists(r'/home/student/PycharmProjects/untitled/cw4246.py')

print path.exists('nTest')
print listdir('.')


print path.isfile('nTest')
print path.isfile('cw6.py')


print path.isdir('nTest')
print path.isdir('cw6.py')




print path.ismount('nTest')
print path.ismount('/home')

print path.getsize('cw6.py')
print path.getsize('nTest')

for x in listdir('.'):
    print x, path.getsize(x)

from time import  ctime
print ctime(path.getctime('cw6.py'))

print ctime(path.getmtime('cw6.py'))

#for sciezka, podkatalogi, pliki in walk(r'./'):
    #print 'w katalogu %s znajduje sie %i  bajtow w %i plikach' %(sciezka, sum(path.getsize(path.join(sciezka,nazwa)) for nazwa in pliki,len(pliki))