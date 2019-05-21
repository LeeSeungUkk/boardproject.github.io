
from django.contrib import admin
from django.urls import path

import dongbang.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',dongbang.views.board, name = 'board'),
    path('submit/', dongbang.views.submit, name= "submit"),
]
