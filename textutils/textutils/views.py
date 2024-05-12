from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
    # return HttpResponse('''<h1>Shantanu</h1> <a href=\
    #                     "https://www.jiocinema.com/"> match dekho yaaron</a>''')

def about(request):
    return render(request, "about_us.html") 

def analyze(request):
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    convtoupper = request.POST.get('performcaps', 'off')
    #print(removepunc)

    if removepunc == "on" and convtoupper == "on":
        punctuations = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
        analyzedtext = ""
        for char in djtext:
            if char not in punctuations:
                analyzedtext += char.upper()
        params = {
            "analysedtext": analyzedtext
        }
        return render(request, 'analyze.html', params)

    elif removepunc == "on":
        punctuations = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
        analyzedtext = ""
        for char in djtext:
            if char not in punctuations:
                analyzedtext += char
        params = {
            "analysedtext": analyzedtext
        }
        return render(request, 'analyze.html', params) 
    
    elif convtoupper == 'on':
        analyzedtext = djtext.upper()
        params = {
            "analysedtext": analyzedtext
        }        
        return render(request, 'analyze.html', params)
    
    else:
        return HttpResponse("Please select atleast one operation")
    
def home(request):
    return render(request, "home.html")

def contact(request):
    return render(request, "contact_us.html")