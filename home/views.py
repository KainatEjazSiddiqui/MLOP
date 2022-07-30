from django.shortcuts import render, HttpResponse ,redirect
from datetime import datetime
from home.models import Contact
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login


# Create your views here.
def search(request):
    query=request.GET['query']
    if len(query)>78:
        allPosts=Post.objects.none()
    else:
        allPostsTitle= Post.objects.filter(title__icontains=query)
        allPostsAuthor= Post.objects.filter(author__icontains=query)
        allPostsContent =Post.objects.filter(content__icontains=query)
        allPosts=  allPostsTitle.union(allPostsContent, allPostsAuthor)
    if allPosts.count()==0:
        messages.warning(request, "No search results found. Please refine your query.")
    params={'allPosts': allPosts, 'query': query}
    return render(request, 'home/search.html', params)
def index(request):
   print(request.user)
   
   return render(request, 'index.html')
    # return HttpResponse("this is homepage")
def handleSignUp(request):
    if request.method=="POST":
        # Get the post parameters
        username=request.POST['username']
        email=request.POST['email']
        fname=request.POST['fname']
        lname=request.POST['lname']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']

        # check for errorneous input
        if len(username)<10:
            messages.error(request, " Your user name must be under 10 characters")
            return redirect('home')

        if not username.isalnum():
            messages.error(request, " User name should only contain letters and numbers")
            return redirect('home')
        if (pass1!= pass2):
             messages.error(request, " Passwords do not match")
             return redirect('home')
        
        # Create the user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name= fname
        myuser.last_name= lname
        myuser.save()
        messages.success(request, " Your MLOPsDCAI AC has been successfully created")
        return redirect('home')

    else:
        return HttpResponse("404 - Not found")

   # if request.method=="POST":
        # Get the post parameters
  #      username=request.POST['username']
   #     email=request.POST['email']
    #    fname=request.POST['fname']
     #   lname=request.POST['lname']
      #  pass1=request.POST['pass1']
       # pass2=request.POST['pass2']

        # check for errorneous input
        
        # Create the user
        #myuser = User.objects.create_user(username, email, pass1)
        #myuser.first_name= fname
        #myuser.last_name= lname
        #myuser.save()
        #messages.success(request, " Your MLOPsDCAI AC has been successfully created")
        #return redirect('home')

    #else:
     #   return HttpResponse("404 - Not found")
def handeLogin(request):
    if request.method=="POST":
        # Get the post parameters
        loginusername=request.POST['loginusername']
        loginpassword=request.POST['loginpassword']

        user=authenticate(username= loginusername, password= loginpassword)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect("home")
        else:
            messages.error(request, "Invalid credentials! Please try again")
            return redirect("home")

    return HttpResponse("404- Not found")
   

    return HttpResponse("login")

def loginUser(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)

        # check if user has entered correct credentials
        user = authenticate(username=username, password=password)

        if user is not None:
            # A backend authenticated the credentials
            login(request, user)
            return redirect("/")

        else:
            # No backend authenticated the credentials
            messages.error(request, "Invalid credentials! Please try again")
            return render(request, 'login.html')
    
    return render(request, 'login.html')

def logoutUser(request):
    logout(request)
    return redirect("/")
def about(request):
    return render(request, 'about.html') 

def services(request):
    if request.user.is_anonymous:
        return redirect("/login") 
    return render(request, 'services.html')
 
def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date = datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent!')
    return render(request, 'contact.html')
def  result (request):
    return render(request, 'prepro.html')
def prepro(request):
    return render(request, 'prepro.html') 
def aug(request):
    return render(request, 'aug.html') 
def prog(request):
    return render(request, 'prog.html')    
def impre(request):
    return render(request, 'impre.html')     
def datasetpre(request):       
    return render(request, 'datasetpre.html') 
def datasetAfter(request):       
    return render(request, 'datasetAfter.html')
def augb(request):       
    return render(request, 'augb.html')    
def auga(request):       
    return render(request, 'auga.html')                         