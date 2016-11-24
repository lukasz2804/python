#ilosc plikow ilosc folderow rozmiar plikow rozmiar folderow przelicz na kb i mb
from os import *


dir = raw_input('podaj sciezke')
prevDir= path.split(dir)[0]

print dir + " podkatalog "+ prevDir

paths, dirs, files = walk(dir).next()
file_count = len(files)
dir_count = len(dirs)
allfiles=0
alldirs =0
print str(file_count) + 'plikow , '+str(dir_count)+' katalogow'
for x in files :
    if(path.isfile(dir+'/'+x)):
        print str(x)+' - '+ str(path.getsize(dir+'/'+x))+'b '  +str(path.getsize(dir+'/'+x)/1024) +'kb '+str(path.getsize(dir+'/'+x)/1048576) + 'mb'
        allfiles = allfiles+ path.getsize(dir+'/'+x)


for x in dirs:
    if(path.isdir(x)):
        alldirs = alldirs + path.getsize(x)

print 'wszystkie pliki waza '+str(allfiles)+'b '  +str(allfiles/1024) +'kb '+str(allfiles/1048576) + 'mb'
print 'wszystkie katalogi waza '+str(alldirs)+'b '  +str(alldirs/1024) +'kb '+str(alldirs/1048576) + 'mb'



print

