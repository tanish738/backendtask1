from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('book/', views.book, name = 'book'),
    path('update/<str:pk>/',views.updateTask,name="update_task"),
    path('delete/<str:pk>/',views.deleteTask,name="delete_task"),
    path('',views.register_page,name="regiter"),
    path('login/',views.login_page,name="login"),
    path('logout/',views.logout_page,name="logout"),
]

#DataFlair
