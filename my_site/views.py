from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request,'index.html')
#     # return HttpResponse("Hello World")
# def index(request):
#     return HttpResponse("Home")

def analyze(request):
    # Get the text
    djtext = request.POST.get('text', 'default')
    # Check checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcount = request.POST.get('charcount', 'off')

    #Check which checkbox is on
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose':'Removed Punctuations', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    if(fullcaps=="on" ):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()

        params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
        # Analyze the text
        return render(request, 'analyze.html', params)

    if(extraspaceremover=="on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1]==" "):
                analyzed = analyzed + char

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        # Analyze the text
        return render(request, 'analyze.html', params)

    if (newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char!="\r":
                analyzed = analyzed + char

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        # Analyze the text
        return render(request, 'analyze.html', params)
    
    if(charcount == "on"):
        analyzed = ""
        analyzed = ("No. of charector in given the text " +str(len(djtext)))
        params = {'purpose': 'Countt the charector', 'analyzed_text': analyzed}
        # Analyze the text
        return render(request, 'analyze.html', params)
    
    if(removepunc != "on" and newlineremover!="on" and extraspaceremover!="on" and fullcaps!="on"):
        return HttpResponse("please select any operation and try again")

    # else:
    #     return HttpResponse("Error")
    
    


# def capfirst(request):
#     return HttpResponse("capitalize first")

# def newlineremove(request):
#     return HttpResponse("Write a new line")

# def spaceremove(request):
#     return HttpResponse("space remover")

# def charcount(request):
#     return HttpResponse("charcount ")
    
# #     # return HttpResponse('''<h1>Videos</h1><a href = https://www.youtube.com/watch?v=AepgWsROO4k&list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9&index=7&ab_channel=CodeWithHarry/video >back</a>''')
# def about(request):
#    return render(request,'about.html')
#      # return HttpResponse("About Harry Bahai <a href = '/n'></a>")
# def video(request):
#     return HttpResponse(''' <h1>Harry Bhai Tutorial</h1><a href = https://www.youtube.com/watch?v=AepgWsROO4k&list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9&index=7&ab_channel=CodeWithHarry ></a>''')
# def videos1(requests):
#     return HttpResponse('''<h1>Harry Bhai Tutorial</h1><a href = https://www.youtube.com/watch?v=ES-bdt0KUZg&list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9&index=8&ab_channel=CodeWithHarry >Coursse video 2</a>''')
# def videos2(requests):
#         return HttpResponse('''<h1>Harry Bhai Tutorial</h1><a href = https://youtu.be/zs2Ux1jfDD0 >video</a>''')
# def videos3(requests):
    