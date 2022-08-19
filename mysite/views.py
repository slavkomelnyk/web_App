from django.shortcuts import render
#from django.http import HttpResponse

def index(requst):
    data = {
        'title':'mysite',
        'values' : [ 'car', 'hello', '123' ]
            }
    return render(requst, 'mysite/index.html', data)


def about(requst):
    return render(requst, 'mysite/about.html')

 