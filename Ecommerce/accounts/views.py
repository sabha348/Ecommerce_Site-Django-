from django.shortcuts import render, redirect

from store.models import Customer
from .forms import NewUserForm
from django.contrib.auth import authenticate, login, logout
# from .forms import ContactForm
from django.contrib import messages

def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            customer = Customer.objects.create(user = user,name=user.username,email=user.email)
            messages.success(request, "Registration successful." )
            return redirect('store')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
        # messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    # form1 = ContactForm()
    return render (request=request, template_name="accounts/register.html", context={"register_form":form, # "contact_form":form1 
        })

def terms(request):
    return render(request, 'accounts/terms.html')


def login_request(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You are now logged in.")
            return redirect('store')
        else:
            messages.error(request,"Invalid username or password.")
            return render(request, 'accounts/login.html')
            
    return render(request=request, template_name='accounts/login.html')

def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("store")

# def login_view(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(data=request.POST)
#         if form.is_valid():
#             user = form.get_user()
#             login(request, user)
#             return redirect('store')
#     else:
#         form = AuthenticationForm()
#     return render(request, 'accounts/login.html', {'form': form})

# def register_view(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect('store')
#     else:
#         form = UserCreationForm()
#     return render(request, 'accounts/register.html', {'form': form})

