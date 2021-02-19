

from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),        # Default admin pannel.
    path('', views.emp_form, name='emp_insert'), # localhost/p/employee. #get and post request for insert operation.
    path('<int:id>/', views.emp_form, name='emp_update'), # get and post request for update operation.
    path('delete/<int:id>/',views.emp_delete, name='emp_delete'), # To delete the existing employee record.
    path('list/', views.emp_list, name='emp_list'), #GET request for retrieve and display all records.
]
