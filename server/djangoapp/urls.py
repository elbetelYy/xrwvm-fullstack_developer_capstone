from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'djangoapp'

urlpatterns = [
    # LOGIN route
    path(route='login', view=views.login_user, name='login'),

    # LOGOUT route
    path(route='logout', view=views.logout_user, name='logout'),

    # REGISTRATION route
    path(route='register', view=views.registration, name='register'),

    # GET CARS route (NEW)
    path(route='get_cars', view=views.get_cars, name='getcars'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)