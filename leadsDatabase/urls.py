from django.urls import path

from . import views

# As this project contains only one app, namespacing the urls is not strictly necessary.
# However, in this way it becomes scalable for whatever we might add later on.
app_name = 'leadsDatabase'

# We have the main url and two suburls with the list and add pages.
urlpatterns = [
    path('', views.index, name='index'),
    path('list', views.list, name='list'),
    path('add', views.add, name='add'),
    path('addResult', views.addResult, name='addResult'),
]