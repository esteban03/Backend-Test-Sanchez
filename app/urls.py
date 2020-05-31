from django.urls import path, include

urlpatterns = [
    path('user/', include(('cornerapps.user.urls', 'user'), namespace='user')),
]
