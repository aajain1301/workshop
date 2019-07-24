from django.urls import include, path
# from rest_framework import routers
# # from .views import UserListView,UserDetailView
# from .views import UserViewSet
#
# router = routers.DefaultRouter()
# router.register('users', UserViewSet)
#
# urlpatterns = [
#     # path("",UserListView.as_view(),name='list'),
#     # path('<int:pk>',UserDetailView.as_view(),name='detail')
#      path("", include(router.urls)),
#      path('auth',include('rest_framework.urls',namespace='rest_framework'))
# ]

from . import views
from api import sms
urlpatterns = [
    path('', views.UserListView.as_view()),
    path('<int:pk>/', views.UserDetailView.as_view()),
    path('rest-auth/', include('rest_auth.urls')),
    path('sms/',sms.send_sms,name='sms'),
]
