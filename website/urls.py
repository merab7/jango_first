from django.urls import path
from . import views

urlpatterns = [
    path('', view=views.home, name='home'),
    # path('login', view=views.login_user, name='login'),
    path('logout/', view=views.logout_user, name='logout'),
    path('register/', view=views.register_user, name='register'),
    path('record/<int:pk>', view=views.costumer_record, name='record'),
    path('delete/<int:pk>', view=views.delete_record, name='delete_record'),
    path('add_record/', view=views.add_record, name='add_record'),
    path('update_record/<int:pk>', view=views.update_record, name='update_record'),

]
