from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login,  authenticate, logout
from .forms import RegistrationForm, UserLoginForm, UserUpdateForm, UserProfileUpdateForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
import requests
import json
from pydictionary import Dictionary
from datetime import datetime
# this displays flash messages or notifications
from django.contrib import messages
# importing validate_email and EmailNotValidError
from email_validator import validate_email, EmailNotValidError
# importing the openai API
import openai
# import the generated API key from the secret_key file
from .api_key import API_KEY
# loading the API key from the secret_key file
openai.api_key = API_KEY
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin


# Create your views here.


@login_required(login_url='login')
def homePage(request):
    return render(request, 'WebApp/homePage.html')


def landingPage(request):
    return render(request, 'WebApp/landingPage.html')

@login_required(login_url='login')
def about(request):
    return render(request, 'WebApp/about.html')


@login_required(login_url='login')
def services(request):
    return render(request, 'WebApp/services.html')

@login_required(login_url='login')
def userProfile(request):

   
    return render(request, 'WebApp/userProfile.html')


@login_required(login_url='login')
def updateUserProfile(request):
    if request.method == 'POST':
        updateForm = UserUpdateForm(request.POST, instance=request.user)
        profileForm = UserProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if updateForm.is_valid() and profileForm.is_valid():
            updateForm.save()
            profileForm.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect('userProfile')

    else:
        updateForm = UserUpdateForm(instance=request.user)
        profileForm = UserProfileUpdateForm(instance=request.user.profile)

    context = {'updateForm' : updateForm, 'profileForm' : profileForm}

    return render(request, 'WebApp/updateUserProfile.html', context)



@login_required(login_url='login')
def contact(request):
    return render(request, 'WebApp/contact.html')


def registerRequest(request):
    if request.user.is_authenticated:
        return redirect("homePage")
    else:
        if request.method == "POST":
            form = RegistrationForm(request.POST)
            if form.is_valid():
                user = form.save()
                login(request, user)
                return redirect("homePage")
        else:
            form = RegistrationForm()
        context = {'form' : form}
        return render(request, 'WebApp/register.html', context)



def loginRequest(request):
    if request.user.is_authenticated:
        return redirect("homePage")
    else:
        if request.method == "POST":
            form = UserLoginForm(request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get("password")
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect("homePage")
        else:
            form = UserLoginForm()
        context = {'form' : form}
        return render(request, 'WebApp/login.html', context)


def logoutRequest(request):
    logout(request)
    return redirect("landingPage")



# this is the view that will render search page

@login_required(login_url='login')
def onlineDictionary(request):
    # capturing the word from the form via the name search
    word = request.GET.get('search')
    # creating a dictionary object
    dict = Dictionary(word)
    # passing a word to the dictionary object
    meanings = dict.meanings()
    # getting a synonym and antonym  
    synonyms = dict.synonyms()
    antonyms = dict.antonyms()
    # bundling all the variables in the context  
    context = {
            'word': word,
            'meanings': meanings,
            'synonyms': synonyms,
            'antonoyms':antonyms
        }
    return render(request, 'WebApp/onlineDictionary.html', context)


@login_required(login_url='login')
def dictResult(request):
    return render(request, 'WebApp/dictResult.html')



@login_required(login_url='login')
def weatherApplication(request):
    # if there are no errors the code inside try will execute
    try:
    # checking if the method is POST
        if request.method == 'POST':
            API_KEY = '25bc7f1be8e59c523a25c54f6c669365'
            # getting the city name from the form input   
            city_name = request.POST.get('city')
            # the url for current weather, takes city_name and API_KEY   
            url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}&units=metric'
            # converting the request response to json   
            response = requests.get(url).json()
            # getting the current time
            current_time = datetime.now()
            # formatting the time using directives, it will take this format Day, Month Date Year, Current Time 
            formatted_time = current_time.strftime("%A, %B %d %Y, %H:%M:%S %p")
            # bundling the weather information in one dictionary
            city_weather_update = {
                'city': city_name,
                'description': response['weather'][0]['description'],
                'icon': response['weather'][0]['icon'],
                'temperature': 'Temperature: ' + str(response['main']['temp']) + ' °C',
                'country_code': response['sys']['country'],
                'wind': 'Wind: ' + str(response['wind']['speed']) + 'km/h',
                'humidity': 'Humidity: ' + str(response['main']['humidity']) + '%',
                'time': formatted_time
            }
        # if the request method is GET empty the dictionary
        else:
            city_weather_update = {}
        context = {'city_weather_update': city_weather_update}
        return render(request, 'WebApp/weatherApplication.html', context)
    # if there is an error the 404 page will be rendered 
    # the except will catch all the errors 
    except:
        return render(request, 'WebApp/weatherPage404.html')



@login_required(login_url='login')
def emailValidator(request):
    # checking if the method is POST
    if request.method == 'POST':
        # getting the email from the form input
        email = request.POST.get('email-address')
        # this is the context
        context = {
                'email': email
            }
        # the try statement for verify/validating the email
        try:
            # validating the actual email address using the validate_email function
            email_object = validate_email(email)
            # creating the message and storing it
            messages.success(request, f'{email} is a valid Email address!!')
            # rendering the results to the index page
            return render(request, 'WebApp/emailValidator.html', context)
            # the except statement will capture EmailNotValidError error 
        except EmailNotValidError as e:
            # creating the message and storing it
            messages.warning(request, f'{e}')
            # rendering the error to the index page
            return render(request, 'WebApp/emailValidator.html', context)
    # this will render when there is no request POST or after every POST request  
    return render(request, 'WebApp/emailValidator.html')
    

@login_required(login_url='login')
def intelligentAssistant(request):
    # the try statement is for sending request to the API and getting back the response
    # formatting it and rendering it in the template
    try:
        # checking if the request method is POST
        if request.method == 'POST':
            # getting prompt data from the form
            prompt = request.POST.get('prompt')
            # making a request to the API 
            response = openai.Completion.create(model="text-davinci-003", prompt=prompt, temperature=1, max_tokens=1000)
            # formatting the response input
            formatted_response = response['choices'][0]['text']
            # bundling everything in the context
            context = {
                'formatted_response': formatted_response,
                'prompt': prompt
            }
            # this will render the results in the home.html template
            return render(request, 'WebApp/intelligentAssistant.html', context)
        # this runs if the request method is GET
        else:
            # this will render when there is no request POST or after every POST request
            return render(request, 'WebApp/intelligentAssistant.html')
    # the except statement will capture any error
    except:
    # this will redirect to the 404 page after any error is caught
        
        return redirect('error')


# this is the view for handling errors

@login_required(login_url='login')
def intelligentAssistantErrorResponse(request):
    return render(request, 'WebApp/intelligentAssistantErrorResponse.html')


def demo(request):
    return render(request, 'WebApp/demo.html')



@login_required(login_url='login')
class ChangePasswordView(SuccessMessageMixin, PasswordChangeView):
    template_name = 'WebApp/changePassword.html'
    success_message = "Successfully Changed Your Password"
    success_url = reverse_lazy('homePage')



