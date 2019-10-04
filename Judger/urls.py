from django.urls import path
from django.urls import include
app_name = "judger"
urlpatterns = [
    path('test/', include('django.contrib.auth.urls'))
]