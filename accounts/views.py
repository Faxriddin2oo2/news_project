from django.contrib.auth import logout
from django.shortcuts import redirect
from django.views import View
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm,UserRegistrationForm


def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request,
                                username=data['username'],
                                password=data['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Muvaffaqiyatli login amalga oshirildi!')
                else:
                    return HttpResponse('Sizning profilingiz faol holatda emas')

            else:
                return HttpResponse('Login va parolda xatolik bor!')
    else:
        form = LoginForm()
        context = {
            'form':form
        }

    return render(request,'registration/login.html', {"form":form})

class CustomLogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('/')


def dashboard_view(request):
    user = request.user
    context = {
        'user': user
    }

    return render(request, 'pages/user_profile.html', context)


def user_register(request):
    if request.method == "POST":
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(
                user_form.cleaned_data["password"]
            )
            new_user.save()
            context = {
                "new_user": new_user
            }
            return render(request, 'account/register_done.html', context)
    else:
        user_form = UserRegistrationForm()
        context = {
            "user_form" : user_form
        }
        return render(request, 'account/register.html', context)