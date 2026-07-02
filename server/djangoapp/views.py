from django.http import JsonResponse
from django.contrib.auth import login, authenticate
from django.views.decorators.csrf import csrf_exempt
import logging
import json

from .models import CarMake, CarModel
# from .populate import initiate

logger = logging.getLogger(__name__)


# -----------------------------
# LOGIN
# -----------------------------
@csrf_exempt
def login_user(request):
    data = json.loads(request.body)
    username = data['userName']
    password = data['password']

    user = authenticate(username=username, password=password)

    if user is not None:
        login(request, user)
        return JsonResponse({
            "userName": username,
            "status": "Authenticated"
        })

    return JsonResponse({
        "userName": username,
        "status": "Failed"
    })


# -----------------------------
# LOGOUT (placeholder if needed)
# -----------------------------
@csrf_exempt
def logout_user(request):
    from django.contrib.auth import logout
    logout(request)
    return JsonResponse({"userName": ""})


# -----------------------------
# REGISTRATION (placeholder if needed)
# -----------------------------
@csrf_exempt
def registration(request):
    return JsonResponse({"status": "Not implemented yet"})


# -----------------------------
# GET CARS (NEW FUNCTION)
# -----------------------------
def get_cars(request):

    count = CarMake.objects.all().count()
    print(count)

    # Optional: populate database if empty
    try:
        if count == 0:
            from .populate import initiate
            initiate()
    except:
        pass

    car_models = CarModel.objects.select_related('car_make')

    cars = []

    for car_model in car_models:
        cars.append({
            "CarModel": car_model.name,
            "CarMake": car_model.car_make.name
        })

    return JsonResponse({"CarModels": cars})


# -----------------------------
# PLACEHOLDERS (NEXT STEPS)
# -----------------------------
def get_dealerships(request):
    return JsonResponse({"status": "Not implemented yet"})


def get_dealer_reviews(request, dealer_id):
    return JsonResponse({"status": "Not implemented yet"})


def get_dealer_details(request, dealer_id):
    return JsonResponse({"status": "Not implemented yet"})


@csrf_exempt
def add_review(request):
    return JsonResponse({"status": "Not implemented yet"})