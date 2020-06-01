from django.urls import path, include

urlpatterns = [
    path('user/', include(('cornerapps.user.urls', 'user'), namespace='user')),
    path('menu/', include(('cornerapps.menu.urls', 'user'), namespace='menu')),
]
