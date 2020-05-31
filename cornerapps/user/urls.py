from django.urls import path
from cornerapps.user.views import (
  authLogin,
  authLogout,
  StoreChef,
  StoreEmployee
)

urlpatterns = [
  path('auth/login', authLogin, name='auth.login'),
  path('auth/logout', authLogout, name='auth.logout'),
  path('store/chef', StoreChef.as_view(), name='store.chef'),
  path('store/employee', StoreEmployee.as_view(), name='store.employee'),
]