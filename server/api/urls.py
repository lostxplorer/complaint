from django.urls import path,include

urlpatterns = [
    path('category/',include('api.categories.urls')),
    path('complaint/',include('api.complaint.urls'))
]
