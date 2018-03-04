from django.shortcuts import get_object_or_404, render
from .models import Lead

# Defines the index view, i.e. the welcome page.
def index(request):
    return render(request, 'leadsDatabase/index.html')

# Returns the list of all entries in the Lead model ordered by their name.
def list(request):
    leads = Lead.objects.order_by('-name_text')[:]
    context = {
        'leads' : leads,
    }
    return render(request, 'leadsDatabase/list.html', context)

# Returns the template page for the add lead form.
def add(request):
    return render(request, 'leadsDatabase/add.html')

# The function, that actually handles the adding of a lead.
def addResult(request):
    # Gets the data from the POST method.
    leadName = request.POST.__getitem__('leadName')
    leadEmail = request.POST.__getitem__('leadEmail')

    # Used for error handling.
    error = False
    errorMessage = ''

    # Creates a new lead with the retrieved values for its name and email.
    lead = Lead(name_text=leadName, email_text=leadEmail)

    # Checks if the lead exists already and if name and email were given.abs
    # The check for uniqueness is done only with the email adress.
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
        # If everything is valid, the lead is saved into the database.
        lead.save()
    
    # Provides the names to be used inside the template html file addResult.html
    context = {
        'leadName' : leadName,
        'leadEmail' : leadEmail,
        'error' : error,
        'errorMessage' : errorMessage
    }
    return render(request, 'leadsDatabase/addResult.html', context)
