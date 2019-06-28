""" creating webpage for wordcount website """

from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    return render(request, 'home.html')

def aboutpage(request):
    return render(request, 'about.html')

def countpage(request):
    fulltext = request.GET['fulltext']
    words = fulltext.split()
    wrdcntDict = {}
    for word in words:
        wrdcntDict[word] = wrdcntDict.get(word,0) + 1

    sortedwords = sorted(wrdcntDict.items(),key=operator.itemgetter(1),reverse = True)

    return render(request, 'count.html',{'fulltext':fulltext,'count':len(words),'sortedwords':sortedwords})


def leageoflegends(request):
    return HttpResponse('<h1>Welcome to the league of Draaaaaaaaaven!</h1>')
