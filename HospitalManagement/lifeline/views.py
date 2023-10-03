from django.shortcuts import render , HttpResponse
from datetime import datetime
from lifeline.models import Contact

# Create your views here.
def index(request):

    if request.method =="POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        DName = request.POST.get('DName')
        issue = request.POST.get('issue')
        contact= Contact(name=name,email=email,phone=phone ,DName=DName,issue=issue, date=datetime.today())
        contact.save()
    return render(request, 'index.html')
    # return HttpResponse("this is homepage")
