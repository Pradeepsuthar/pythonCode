# Create file by :- pradeepBhardwaj
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    # return HttpResponse('''<h1>Home Page</h1> <a href="http://127.0.0.1:8000/about">about Us</a>''')
    params = {"fname":"Pradeep","lname":"Suthar"}
    return render(request, 'index.html',params)

def aboutPage(request):
    return HttpResponse("<a href='/'><- Back </a> About Page")

def analysisText(request):
    # print(request.GET.get("text","default"))
    useText = request.GET.get("text","default")
    removepunc = request.GET.get("removepunc", "off")
    upperCase = request.GET.get("upperCase", "off")
    print(useText)
    print(removepunc)
    # return HttpResponse("<a href='/'><- Back </a> Analysis Text")
    if (removepunc == "on"):
        punctuationList = '''!"#$%&'()*+,-./:;?@[]^_`{|}~'''
        analyzedText = ""
        for char in useText:
            if char not in punctuationList:
                analyzedText+=char
                
        parameters = {"purpose":"Removed Punctuation", "analyzedText": analyzedText}
        return render(request, "analyzeText.html",parameters)

    elif (upperCase == "on"):
        analyzedText = ""
        for char in useText:
            analyzedText = analyzedText + char.upper()

        parameters = {"purpose":"Upper Case", "Upper Case": analyzedText}
        return render(request, "analyzeText.html",parameters)
    else:
        error = {"error":"Please check the checkboxx for remove puncutuations."}
        return render(request, "analyzeText.html",error)

