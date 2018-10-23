from django.http import HttpResponse
from django.shortcuts import render
from formsapp.forms import ContactForm, RegisterForm

# Create your views here.

def contactus(request):
    if request.method == 'POST':
        contactform = ContactForm(request.POST)
        if contactform.is_valid():
            cdata = contactform.cleaned_data
            print(cdata)
            return HttpResponse('We will get back to u!')
    else:
        contactform = ContactForm()

    return render(request, 'formsapp/contactus.html', {
        'form': contactform
    })

def register(request):
    if request.method == 'POST':
        registerform = RegisterForm(request.POST, request.FILES)
        if registerform.is_valid():
            rdata = registerform.cleaned_data
            print(rdata)
            handle_uploaded_file(request.FILES['profilepic'])
            return HttpResponse('Success in register')
    else:
        registerform = RegisterForm()

    return render(request, 'formsapp/register.html', {
        'form': registerform
    })

def handle_uploaded_file(file_to_upload):
    # print(file_to_upload.name)
    # print(file_to_upload.content_type)
    with open('/tmp/profile_pics/{0}'.format(file_to_upload.name), mode='wb') as fp:
        for chunk in file_to_upload.chunks():
            fp.write(chunk)
