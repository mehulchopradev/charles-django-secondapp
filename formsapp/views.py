from django.http import HttpResponse
from django.shortcuts import render
from formsapp.forms import ContactForm, RegisterForm, BookForm
from django.views import View
from django.views.generic import FormView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from formsapp.models import Book, Author
from datetime import datetime

# Create your views here.

# view functions
# view classes

class ContactUsFormView(FormView):
    template_name = 'formsapp/contactus.html'
    form_class = ContactForm
    success_url = '/formsapp/contactus-success'

    def form_valid(self, form):
        contactdata = form.cleaned_data
        print('Sending email to...')
        print(contactdata)

        return super().form_valid(form)

'''class ContactUsView(View):
    def get(self, request):
        contactform = ContactForm()
        return render(request, 'formsapp/contactus.html', {
            'form': contactform
        })

    def post(self, request):
        contactform = ContactForm(request.POST)
        if contactform.is_valid():
            cdata = contactform.cleaned_data
            print(cdata)
            return HttpResponse('We will get back to u!')
        else:
            return render(request, 'formsapp/contactus.html', {
                'form': contactform
            })
'''

'''def contactus(request):
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
'''

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

class BookFormView(FormView):
    template_name = 'formsapp/create-book.html'
    form_class = BookForm

    def form_valid(self, modelform):
        book = modelform.save()
        if book.id:
            return HttpResponse('Success')
        return HttpResponse('Failure')

class BookListView(ListView):
    # model = Book # Book.objects.all()
    # by default
    # formsapp/book_list_view.html
    # object_list
    queryset = Book.objects.filter(price__gt=800)
    context_object_name = 'book_list'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['datetime'] = datetime.now()

        return context_data

class AuthorCreateView(CreateView):
    model = Author
    fields = '__all__'

class AuthorUpdateView(UpdateView):
    model = Author
    fields = '__all__'

class AuthorDeleteView(DeleteView):
    model = Author
    success_url = '/formsapp/contact-us/'   

def author_create_success(request, author_id):
    return HttpResponse('success' + str(author_id))

'''def createbook(request):
    if request.method == 'POST':
        bookform = BookForm(request.POST)
        if bookform.is_valid():
            book = bookform.save()
            if book.id:
                return HttpResponse('Success')
            else:
                return HttpResponse('Failure')
    else:
        bookform = BookForm()
    return render(request, 'formsapp/create-book.html', {
        'form': bookform
    })
'''
