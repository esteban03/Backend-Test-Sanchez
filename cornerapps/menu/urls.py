from django.urls import path
from cornerapps.menu.views import StoreMenu, UpdateMenu, IndexMenu

urlpatterns = [
  path('index', IndexMenu.as_view(), name='index'),
  path('store', StoreMenu.as_view(), name='store'),
  path('update/<slug:id>', UpdateMenu.as_view(), name='update'),
]