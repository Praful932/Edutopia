from django.shortcuts import render, redirect
from app.forms import (StudentSignUpForm, StudentFieldForm, MentorSignUpForm,
 MentorFieldForm, MentorPostForm, LocForm, UserUpdateForm)
from django.contrib import messages
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from app.models import User, Domain, Student, Mentor, Post
from django.views.generic import DetailView,ListView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
import json
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
    domains = Domain.objects.all()
    posts = Post.objects.all()
    context = {
        'posts': posts,
        'domains' : domains
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
            # Can signals be used here?
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

@login_required
def alpha(request):
    if request.method == 'GET':
        studentarray = Student.objects.all()
        # Student Info
        usernames_cleaned = []
        lats_cleaned = []
        lngs_cleaned = []
        domains_cleaned = []
        profs_cleaned = []
        for student in studentarray:
            if student.user.lat:
                usernames_cleaned.append(str(student.user))
                lats_cleaned.append(float(student.user.lat))
                lngs_cleaned.append(float(student.user.lng))
                domains_cleaned.append(str(student.domain))
                profs_cleaned.append(student.proficiency)
        studentdata = [list(x) for x in zip(usernames_cleaned,lats_cleaned,lngs_cleaned,domains_cleaned,profs_cleaned)]
    context = {
        'studentdata': json.dumps(studentdata)
    }
    return render(request, 'app/alpha.html', context=context)

# Add Student/Mentor Location
@login_required
def AlphaAdd(request):
    if request.method == 'GET':
        locform = LocForm()
    else:
        locform = LocForm(request.POST)
        # Print Errors
        # print(locform.errors)
        if locform.is_valid():
            lat = locform.cleaned_data['lat']
            lng = locform.cleaned_data['lng']
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


@login_required
def beta(request):
    if request.method == "GET":
        mentorarray = Mentor.objects.all()
        studentarray = Student.objects.all()
        # Mentor Info
        usernamem_cleaned = []
        latm_cleaned = []
        lngm_cleaned = []
        otherinfom_cleaned = []
        domainsm_cleaned = []
        # Student Info
        usernames_cleaned = []
        lats_cleaned = []
        lngs_cleaned = []
        domains_cleaned = []
        profs_cleaned = []

        for student in studentarray:
            if student.user.lat:
                usernames_cleaned.append(str(student.user))
                lats_cleaned.append(float(student.user.lat))
                lngs_cleaned.append(float(student.user.lng))
                domains_cleaned.append(str(student.domain))
                profs_cleaned.append(student.proficiency)
        studentdata = [list(x) for x in zip(usernames_cleaned,lats_cleaned,lngs_cleaned,domains_cleaned,profs_cleaned)]

        for mentor in mentorarray:
            if mentor.user.lat:
                usernamem_cleaned.append(str(mentor.user))
                latm_cleaned.append(float(mentor.user.lat))
                lngm_cleaned.append(float(mentor.user.lng))
                otherinfom_cleaned.append(mentor.OtherInfo)
                mentordomainlist = []
                # Since mentor can have multiple fields
                for domain in mentor.domains.all():
                    mentordomainlist.append(str(domain))
                domainsm_cleaned.append(mentordomainlist)
        mentordata = [list(x) for x in zip(
            usernamem_cleaned,latm_cleaned, lngm_cleaned, otherinfom_cleaned, domainsm_cleaned)]
        
        context = {
            'mentordata': json.dumps(mentordata),
            'studentdata': json.dumps(studentdata)
        }
    return render(request, 'app/beta.html', context=context)

@login_required
def UpdateProfile(request):
    if request.method == "GET":
        if request.user.is_student:
            userform = UserUpdateForm(instance=request.user)
            fieldform = StudentFieldForm(instance=request.user.student)
        else:
            userform = UserUpdateForm(instance=request.user)
            fieldform = MentorFieldForm(instance=request.user.mentor)
        context={
            'userform' : userform,
            'fieldform' : fieldform
        }
    else:
        if request.user.is_student:
            userform = UserUpdateForm(request.POST, instance=request.user)
            fieldform = StudentFieldForm(request.POST, instance=request.user.student)
        else:
            userform = UserUpdateForm(request.POST, instance=request.user)
            fieldform = MentorFieldForm(request.POST, instance=request.user.mentor)
        if userform.is_valid() and fieldform.is_valid():
            userform.save()
            fieldform.save()    
            return redirect('index')
    return render(request,"app/updateprofile.html",context=context)

# Detail View for Each post
class PostDetailView(DetailView):
    model = Post
    template_name = 'app/singlepost.html'
    context_object_name = 'post'

# List View of Posts for Each Mentor
class PostListView(LoginRequiredMixin,UserPassesTestMixin ,ListView):
    model = Post
    template_name = 'app/authorposts.html'

    # Check if passes tests then render template
    def test_func(self):
        if self.request.user.is_mentor:
            return True
        return False

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_mentor = Mentor.objects.get(user=self.request.user)
        context['posts'] = Post.objects.filter(owner=current_mentor)
        return context

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Post
    fields = ['topic','content','domain']
    template_name = 'app/updatepost.html'

    # Check if current user is author of the post
    def test_func(self):
        post = self.get_object()
        if self.request.user.is_mentor and (post.owner.user == self.request.user):
            return True
        return False

    def form_valid(self, form):
        form.instance.owner.user = self.request.user
        return super().form_valid(form)

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Post
    success_url = reverse_lazy('omega')

    # Check if current user is author of the post
    def test_func(self):
        post = self.get_object()
        if self.request.user.is_mentor and (post.owner.user == self.request.user):
            return True
        return False