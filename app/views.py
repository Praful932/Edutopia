from django.shortcuts import render, redirect
from app.forms import StudentSignUpForm, StudentFieldForm, MentorSignUpForm, MentorFieldForm, MentorPostForm, LocForm
from django.contrib import messages
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from app.models import User, Domain, Student, Mentor, Post
# commit = False used when before saving it is needed to input any other data or associated any other model
# Create your views here.


def index(request):
    return render(request, "app/index.html")


def loginf(request):
    if request.user.is_authenticated:
        logout(request)
    return render(request, "app/login.html")


def register(request):
    return render(request, "app/register.html")


def omega(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, "app/omega.html", context=context)


def registerStudent(request):
    if request.user.is_authenticated:
        logout(request)

    if request.method == 'POST':
        # Create form instance with POST data
        signupform = StudentSignUpForm(request.POST)
        studentform = StudentFieldForm(request.POST)
        if signupform.is_valid() and studentform.is_valid():
            username = signupform.cleaned_data.get('username')
            new_user = signupform.save(commit=False)
            new_user.is_student = True
            new_user = signupform.save()
            # login the new registered user
            login(request, new_user)
            student = studentform.save(commit=False)
            student.user = new_user
            studentform.save()
            messages.success(
                request, f'Account successfully created for {username}!')
            return redirect('index')
    else:
        signupform = StudentSignUpForm()
        studentform = StudentFieldForm()
    context = {
        'signupform': signupform,
        'studentform': studentform
    }
    return render(request, "app/registerstudent.html", context=context)


def registerMentor(request):
    if request.user.is_authenticated:
        logout(request)

    if request.method == 'GET':
        signupform = MentorSignUpForm()
        mentorform = MentorFieldForm()
        context = {
            'signupform': signupform,
            'mentorform': mentorform
        }
    else:
        signupform = MentorSignUpForm(request.POST)
        mentorform = MentorFieldForm(request.POST)
        if signupform.is_valid() and mentorform.is_valid():
            username = signupform.cleaned_data.get('username')
            new_user = signupform.save(commit=False)
            new_user.is_mentor = True
            new_user = signupform.save()
            login(request, new_user)
            mentor = mentorform.save(commit=False)
            mentor.user = new_user
            mentorform.save()
            messages.success(
                request, f'Account successfully created for {username}!')
            return redirect('index')

    return render(request, "app/registermentor.html", context=context)


def logoutf(request):
    # Check if user is logged in if not redirect to login page
    if request.user.is_authenticated:
        username = request.user.username
        logout(request)
        messages.success(request, f'Successfully Logged out {username}!')
        return redirect('index')
    return redirect('login')


@login_required
def MentorPost(request):
    if request.user.is_student:
        messages.success(
            request, f'Only Mentors are allowed to access this page!')
        return redirect('index')
    if request.method == 'GET':
        mentorpostform = MentorPostForm()
        context = {
            'mentorpostform': mentorpostform
        }
    else:
        mentorpostform = MentorPostForm(request.POST)
        if mentorpostform.is_valid():
            ob = mentorpostform.save(commit=False)
            # get the current logged in users mentor object to associate with post as foreign key
            mentor = Mentor.objects.get(user=request.user)
            ob.owner = mentor
            mentorpostform.save()
            return redirect('omega')
    return render(request, 'app/mentorpost.html', context=context)

# pk should be same as defined in urls.py


def SinglePost(request, pk):
    post = Post.objects.get(id=pk)
    context = {
        'post': post
    }
    return render(request, "app/singlepost.html", context=context)


@login_required
def alpha(request):
    if request.method == 'GET':
        userarray = User.objects.all()
        lat_cleaned = []
        lng_cleaned = []
        for user in userarray:
            if user.is_student and user.lat:
                lat_cleaned.append(float(user.lat))
                lng_cleaned.append(float(user.lng))
        locations = [list(x) for x in zip(lat_cleaned,lng_cleaned)]
    print(locations)
    context={
        'locations' : locations
    }   
    return render(request, 'app/alpha.html',context=context)

# Only Students
# Add Student Location
@login_required
def AlphaAdd(request):
    if request.user.is_mentor:
        messages.success(
            request, f'Only Students are allowed to access this page!')
        return redirect('index')
    if request.method == 'GET':
        locform = LocForm()
    else:
        locform = LocForm(request.POST)
        # Print Errors
        # print(locform.errors)
        if locform.is_valid():
            lat=locform.cleaned_data['lat']
            lng=locform.cleaned_data['lng']
            # Create user object since locform cannot be used as it will create 
            # another blank instance of user so update fields only of current user
            f = User.objects.get(id=request.user.id)
            f.lat = lat
            f.lng = lng
            f.save()
            return redirect('index')
    context = {
            'locform': locform
        }
    return render(request, 'app/alphaadd.html', context=context)
