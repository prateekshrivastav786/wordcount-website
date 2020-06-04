from django.http import HttpResponse
from django.shortcuts import render
import operator
def homepage(request):
  return render(request, 'home.html')
 
def count(request):
   fulltext = request.GET['fulltext']
   wordlist=fulltext.split()
   worddic = {}
   for i in wordlist:
     if i in worddic:
        #Increase
        worddic[i] += 1
     else:
        # add to the worddic
       worddic[i] =1
   sortedwords=sorted(worddic.items(), key=operator.itemgetter(1), reverse=True)  
   return render(request, 'count.html', {'fulltext':fulltext, 'count':len(wordlist), 'sortedwords':sortedwords})

def about(request):
  return render(request, 'about.html')

def supportcenter(request):
   return render(request, 'support.html')#, {'fulltext1':fulltext1})

def supporthandler(request):
   fulltext1 = request.GET['fulltext']
   return render(request, 'supporthandler.html', {'fulltext1':fulltext1})
