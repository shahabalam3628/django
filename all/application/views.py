from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponse
from application.models import Company,Organization  # import model 
import pdb;
#from . form import CompanyForm,OrganizationForm,PostForm,Post
from . form import *
from . models import *
from django.views import generic
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.mail import send_mail

from django.http import HttpResponse

from django.core.mail import EmailMessage





# create Form without using model

def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        if form.is_valid():
            send_mail('Dynamic Email Message', message, 'imranalam3628@gmail.com', ['shahabalam78@gmail.com',])
            return HttpResponse('Thanks for contacting us!')
    else:
        form = ContactForm()
    return render(request, 'emails/contact-us.html', {'form': form})


def home(request):
    return render(request,'emails/test1.html')

def sendmail(request):
    send_mail('Python Test1', 'Hi,This is Python First Message.', 'imranalam3628@gmail.com', ['shahabalam78@gmail.com',])
    return HttpResponse('Mail successfully sent')


def index(request):
    user_list = User.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(user_list, 2)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)

    return render(request, 'core/user_list.html', { 'users': users })



def post_list(request):
	queryset_list = Post2.objects.all().order_by("id")
	paginator = Paginator(queryset_list, 3) #posts per page
	page = request.GET.get('page')
	try:
		queryset = paginator.page(page)
	except PageNotAnInteger:
		queryset = paginator.page(1)
	except EmptyPage:
		queryset = paginator.page(paginator.num_pages)

	context = {"object_list" : queryset,}
	return render(request, "list.html", context) #Comment this line and uncomment next line to display another style
    #return render(request, "list2.html", context)




class BookList(generic.ListView):
    model = Book
    #print("shahahab") 
    queryset = Book.objects.all()
    template_name = 'pagination1.html'
    paginate_by = 3


def setSession(request):
    request.session['sname'] = 'irfan'  
    request.session['semail'] = 'irfan.sssit@gmail.com'  
    return HttpResponse("session is set") 


def getSession(request):
    studentname = request.session['sname']  
    studentemail = request.session['semail']  
    return HttpResponse(studentname+" "+studentemail);

    






def registration(request):
    form = RegistrationForm(request.POST or None)
    if form.is_valid():
        form.save()
    text ={'form':form}
    return render(request,'registration.html',text)



def org_home(request):
    form = OrganizationForm(request.POST or None)
    if form.is_valid():
        form.save()
    text ={'form':form }
    #messages.success(request, 'Form submission successful')
    success = True
    return render(request,'organization.html',text)



def person(request):
    form = PersonForm(request.POST or None)
    if form.is_valid():
        form.save()
    text ={'form':form}
    return render(request,'person.html',text)


     
def mypost(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        form.save()
    data=Post.objects.all()
    print(data)
    
    text ={'form':form,'data':data}
    #data=Post.objects.all()
    return render(request,'post.html',text)

def company_home(request):
    form = CompanyForm(request.POST or None)
    if form.is_valid():
        form.save()
    text ={'form':form}
    return render(request,'company.html',text)




def getPost(request):
    if(request.method=='POST'):
        insert = Post(
            title            = request.POST['title'],
            description      = request.POST['description'],    
        )
        print(title)
        insert.save()
    data=Post.objects.all()   #fetch all record from table
    return render(request,'post.html',{'data':data})



def home_list(request):
    return render(request,'work_list.html')


def student(request):
    return render(request,'work_list.html')

