
from django.contrib import admin
from django.urls import path, include

from todolist.views import LoginView
from todolist.views import TodoItemView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view(), name='login'),
    path('todos/', TodoItemView.as_view(), name='todos'),
    path('__debug__/', include('debug_toolbar.urls'), name='debug_toolbar'),
]
