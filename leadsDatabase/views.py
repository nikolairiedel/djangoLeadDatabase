from django.shortcuts import get_object_or_404, render

from .models import Lead

def index(request):
    return render(request, 'leadsDatabase/index.html')

def list(request):
    leads = Lead.objects.order_by('-name_text')[:]
    context = {
        'leads' : leads,
    }
    return render(request, 'leadsDatabase/list.html', context)

def add(request):
    return render(request, 'leadsDatabase/add.html')

def addResult(request):
    leadName = request.POST.__getitem__('leadName')
    leadEmail = request.POST.__getitem__('leadEmail')
    error = False
    errorMessage = ''

    lead = Lead(name_text=leadName, email_text=leadEmail)

    if(Lead.objects.filter(email_text=leadEmail).exists() and leadName != "" and leadEmail != ""):
        error = True
        errorMessage = 'Your Email adress is already in our database.'
    elif(leadName == "" and leadEmail != ""):
        error = True
        errorMessage = 'Please provide a name as well.'
    elif(leadEmail == "" and leadName != ""):
        error = True
        errorMessage = 'Please provide an Email adress as well.'
    elif(leadEmail == "" and leadName == ""):
        error = True
        errorMessage = 'Please provide a name and an Email adress.'
    else:
        lead.save()
    
    context = {
        'leadName' : leadName,
        'leadEmail' : leadEmail,
        'error' : error,
        'errorMessage' : errorMessage
    }
    return render(request, 'leadsDatabase/addResult.html', context)
