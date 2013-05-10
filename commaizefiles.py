import linecache
import string
import pyperclip

d = {  }
try:
   with open('all_counties.csv') as infile:
      for line in infile:
         d.update( { line[0:line.index(',')]:line[line.index(',')+1:].rstrip() } )
      pyperclip.copy( d )
except IOError:
   print 'File not found!'

print 'Finished!'
