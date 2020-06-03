from django.urls import path
from cornerapps.menu.views import StoreMenu, UpdateMenu, IndexMenu, StoreChooseMenu, ViewMenu

urlpatterns = [
    path('index', IndexMenu.as_view(), name='index'),
    path('store', StoreMenu.as_view(), name='store'),
    path('update/<slug:id>', UpdateMenu.as_view(), name='update'),
    path('choose', StoreChooseMenu.as_view(), name='store.choose'),
    path('<uuid:id>', ViewMenu.as_view(), name='view'),
]
