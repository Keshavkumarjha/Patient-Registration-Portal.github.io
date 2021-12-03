from django.urls import path
from crud import views
from django.conf import settings
from django.conf.urls.static import static
from django.views import View


urlpatterns = [
    path('', views.home,name='home'),
    path('showdata/', views.showdata,name='showdata'),
    path('fillform/', views.fillform.as_view(),name='fillform'),
    path('<int:id>/', views.update,name='update'),

    path('deletedata/<int:id>/', views.delete_data,name='deletedata'),
    
]
