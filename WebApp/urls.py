from django.urls import path
from . import views
from WebApp.views import ChangePasswordView


urlpatterns = [
    path("", views.landingPage, name="landingPage"),
    path("about/", views.about, name="about"),
    path("homePage/", views.homePage, name="homePage"),
    path("services/", views.services, name="services"),
    path("contact/", views.contact, name="contact"),
    path("userProfile/", views.userProfile, name="userProfile"),
    path("updateUserProfile/", views.updateUserProfile, name="updateUserProfile"),
    path("register/", views.registerRequest, name="register"),
    path("login/", views.loginRequest, name="login"),
    path("logout/", views.logoutRequest, name="logout"),

    path("weatherApplication/", views.weatherApplication, name="weatherApplication"),

    
    path("onlineDictionary/", views.onlineDictionary, name="onlineDictionary"),

    path("emailValidator/", views.emailValidator, name="emailValidator"),
    path("intelligentAssistant/", views.intelligentAssistant, name="intelligentAssistant"),
    path("intelligentAssistantErrorResponse/", views.intelligentAssistantErrorResponse, name="intelligentAssistantErrorResponse"),

    path('changePassword/', ChangePasswordView.as_view(), name='changePassword'),



    path("demo/", views.demo, name="demo"),
]
