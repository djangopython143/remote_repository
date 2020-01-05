from django.shortcuts import render
from .models import Course,FeedbackData,ContactData
from django.http.response import HttpResponse
from .forms import FeedbackForm
def home(request):
    return render(request,'home.html')
def contact(request):
    if request.method=='POST':
        data=ContactData(name=request.POST.get('name'),
                    email=request.POST.get('email_id'),
                    mobile=request.POST.get('mobile'),
                    comments=request.POST.get('message'),
                    date=date1)
        data.save()
        return HttpResponse('We will contact you soon...')
    else:
        return render(request,'contact.html')
def services(request):
    data=Course.objects.all()
    return render(request,'services.html',{'data':data})
from datetime import datetime
date1=datetime.now()
def feedback_view(request):
    if request.method=='POST':
        fform=FeedbackForm(request.POST)
        if fform.is_valid():
            name1=request.POST.get('Name')
            rating1=request.POST.get('Rating')
            feedback1=request.POST.get('Feedback')
            data=FeedbackData(name=name1,rating=rating1,feedback=feedback1,date=date1)

            data.save()
            fform=FeedbackForm()
            Feedbacks = FeedbackData.objects.all()
            return render(request,'feedback.html',{'fform':fform,'Feedbacks':Feedbacks})
        else:
            return HttpResponse('Invalid Form')
    else:
        fform=FeedbackForm()
        Feedbacks=FeedbackData.objects.all()
        return render(request,'feedback.html',{'fform':fform,'Feedbacks':Feedbacks})


def gallery(request):
    return render(request,'gallery.html')
