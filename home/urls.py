from django.urls import path

from home.views import *

urlpatterns = [
    path('', home, name='home'),

    path('skills/', skills, name='skills'),
    path('skills/<int:post_id>/', show_my_post, name='my_post'),

    path('login/', login, name='login'),
    path('signup/', signup, name='signup'),

]
