from rest_framework import routers
from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token
from users.views import UserViewSet, LoginView, LogoutView, ListUserView, CreateUserView, CreateTokenView, ClienteViewSet, ClienteApiView

router  = routers.DefaultRouter()
router.register('user', UserViewSet)
router.register('clientes', ClienteViewSet)

urlpatterns = [
    path('list/', ListUserView.as_view()),
    path('create/', views.CreateUserView.as_view(), name='create_user'),
    path('create/<int:pk>/', CreateUserView.as_view(), name='user-delete'),
    path('api-token-auth/', CreateTokenView.as_view(), name='api_token_auth'),
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('cliente/',ClienteApiView.as_view())
    
]