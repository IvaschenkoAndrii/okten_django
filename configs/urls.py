from django.urls import include, path

urlpatterns = [
    path('users', include('apps.users.urls')),
    path('cars', include('apps.cars.urls')),
    path('auto_parks', include('apps.auto_park.urls'))
]
