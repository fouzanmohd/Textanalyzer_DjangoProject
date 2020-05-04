
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

def home(request):

    return render(request, 'home.html')

def analyze(request):
    djtext = request.POST.get('text', 'default')
    removepunc= request.POST.get('removepunc', 'off')
    uppercase= request.POST.get('uppercase', 'off')
    lowercase= request.POST.get('lowercase', 'off')
    removelines= request.POST.get('removelines', 'off')
    removeextraspace= request.POST.get('removeextraspace', 'off')
    countwords = request.POST.get('countwords', 'off')
   
    
# Removing punctuations
    if removepunc == 'on':
        punctuations = ''',.\';:"/?][-_'''
        analyzed = ''
        for char in djtext:
            if char not in punctuations:
                analyzed += char
        djtext = analyzed
        mydict = {'Actionplan': 'Removed Punctuation', 'analyzedtext' : analyzed}       


# Changing to Upper case
    if uppercase  == 'on':
        analyzed=''
        for char in djtext:            
            analyzed = analyzed+char.upper()
        djtext = analyzed
        mydict = {'Actionplan': 'Changing to uppercase', 'analyzedtext' : analyzed}        


# Changing to Lower case    
    if lowercase  == 'on':
        analyzed=''
        for char in djtext:            
            analyzed = analyzed+char.lower()
        djtext = analyzed
        mydict = {'Actionplan': 'Changing to lowercase', 'analyzedtext' : analyzed}        


#Removing newlines
    if removelines == 'on':
        analyzed=''
        for char in djtext:            
            if char != "\n" and char!="\r":
                analyzed = analyzed + char
        djtext = analyzed        
        mydict = {'Actionplan': 'Removing newlines', 'analyzedtext' : analyzed}      
           
  
#Removing extra space between words
    if removeextraspace == 'on':
        analyzed=''
        for index,char in enumerate(djtext):
           if not (djtext[index] == ' ' and djtext[index - 1] == ' '):
               analyzed+=char
        djtext = analyzed
        mydict = {'Actionplan': 'Removing extra space', 'analyzedtext' : analyzed}
        
#To count total number of words
    if countwords == 'on':
        word_list = djtext.split()
        analyzed ='Total words: '+ str(len(word_list))
        djtext = analyzed
        mydict = {'Actionplan': 'Total character count ', 'analyzedtext' : analyzed}
    
   

    if(removepunc != 'on' and uppercase != 'on'and lowercase!='on' and removelines != 'on'and removeextraspace !='on' and countwords != 'on'):
        
        return HttpResponse('<h1>Please select a function and try again!</h1>')
        
    
    return render(request, 'analyze.html', mydict)




def about(request):
   return render(request, 'about.html')