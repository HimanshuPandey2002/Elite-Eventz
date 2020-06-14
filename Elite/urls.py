from django.contrib import admin
from django.urls import path, include
from register import views as r_views
from venues import views as v_views
from events import views as e_views
from photography import views as p_views
from decoration import views as d_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('register/', r_views.register, name='register'),
    path('venue/', v_views.venue, name='venue'),
    path('decoration/', d_views.dec, name='decoration'),
    path('events/', e_views.event, name='events'),
    path('photography/', p_views.photo, name='photography'),
]
