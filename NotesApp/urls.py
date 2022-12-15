from django.urls import re_path
from NotesApp import views

urlpatterns = [
    re_path(r'^note/$',views.noteApi),
    re_path(r'^note/([0-9]+)$',views.noteApi)
]
