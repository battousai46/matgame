from django.urls import path

app_name = "users"

from users.views import MatGameTokenObtainPairView



urlpatterns = [
    path('token/', view=MatGameTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path("login/", MatGameTokenObtainPairView.as_view()),
    path("refresh/", MatGameTokenObtainPairView.as_view()),
    path("logout/", MatGameTokenObtainPairView.as_view()),
]