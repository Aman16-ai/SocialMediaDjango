from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate ,logout
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .models import UserProfile,posts
# Create your views here.
def index(request):
    context = {}
    try:
        allposts = posts.getAllPosts()
        print(allposts)
        for i in allposts:
            print(i.likes.all())
            i.likes_count = len(i.likes.all())
        context['allposts'] = allposts
    except Exception as e:
        print("user not found")
    return render(request,'index.html',context)

def signuppage(request):
    return render(request,"signuppage.html")

def handlesignup(request):
    if(request.method == 'POST'):
        username = request.POST['Username']
        firstname = request.POST['Firstname']
        Lastname = request.POST['Lastname']
        email = request.POST['email']
        age = request.POST['Age']
        profile_image = request.FILES['ProfileImg']
        country = request.POST['Country']
        language = request.POST['Language']
        password = request.POST['pass']
        print(f"Username is {username} Profile is {profile_image}, Firstname is {firstname}, Lastname is {Lastname}, Age is {age},country is {country} and language is {language}")
        
        user = User.objects.create_user(username,email,password)
        user.first_name = firstname
        user.last_name = Lastname
        if(user is not None):
            profile = UserProfile(userauth = user,dob =age,country = country,profile_img = profile_image,language =language)
            profile.save()
            user.save()
    return redirect("/")

def loginpage(request):
    return render(request,"loginpage.html")


def handlelogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['pass']
        print(f"username is {username} and password {password}")
        user = authenticate(request,username = username,password = password)
        if user is not None:
            login(request,user)
            return redirect("/")
        
    return HttpResponse("Credentials invalid")

@login_required(login_url="loginpage")
def myprofileinfo(request):
    userprofile = UserProfile.getUserProfile(request.user)
    allposts = posts.getAllUserPosts(userprofile.id)
    print(userprofile.id)
    print(allposts)
    total_posts = len(allposts)
    print('totalposts',total_posts)
    context = {'profile_info':userprofile ,'totalposts':total_posts,'userposts':allposts}
    return render(request,"profile.html",context)

def logoutuser(request):
    logout(request)
    return redirect("/")

def likePost(request,post_id):
    print(f"Post id is {post_id}")
    post = posts.getPostById(post_id)
    print(post)
    user = UserProfile.getUserProfile(request.user)
    print("user is ",user)
    
    isliked = False
    if user in post.likes.all():
        isliked = True
    if(isliked):
        post.likes.remove(user.id)
    else:
        post.likes.add(user.id)
    post.save()
    return redirect("/")