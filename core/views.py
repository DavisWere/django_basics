from django.shortcuts import render ,redirect
from core .models import CustomUser
from core .forms import CustomUserCreationForm, StudentMakrsForm



def user_profile(request):
    user= CustomUser.objects.all
    return render(request, 'user_profile.html',{'user':user})


# Create your views here.
def create_user(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request,'user_profile/')  # Redirect to user profile page after successful creation
    else:
        form = CustomUserCreationForm()
    return render(request, 'user_profile.html', {'form': form})

def Student_marks(request):
    if request.method == 'POST':
        form = StudentMakrsForm(request.POST,request.Files)
        if  form.is_valid():
            form.save()
            return redirect('student-marks')
        else :
            form = StudentMakrsForm()
        return  render (request,"user_form.html",{"form":form})