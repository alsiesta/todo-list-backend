
from django.contrib import admin
from django.urls import path, include

from todolist.views import LoginView, TodoItemView, TodoItemUpdateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view(), name='login'),
    path('todos/', TodoItemView.as_view(), name='todos'),
    path('todos/<int:pk>/', TodoItemUpdateView.as_view(), name='todo-update'),
    path('__debug__/', include('debug_toolbar.urls'), name='debug_toolbar'),
]
