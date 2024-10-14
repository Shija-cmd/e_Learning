from django.urls import path
from . import views
from django.conf.urls import handler404
# Other url patterns
urlpatterns = [
    path('', views.home, name='index'),
    path('404', views.error, name='404'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('courses', views.courses, name='courses'),
    path('team', views.team, name='team'),
    path('testimonial', views.testimonial, name='testimonial')
]

# Set the custom 404 view
handler404 = 'elearning.views.custom_404_view'