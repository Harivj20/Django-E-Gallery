from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('gallery/',views.gallery,name='gallery'),
    path('photos/<id>/',views.photos,name='photos'),
    path('add/',views.add,name='add'),
    path('new_category/',views.new_category,name='new_category'),
    path('search/',views.searchbar,name='search'),
    path('register/',views.registration,name='register'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('theme/',views.theme,name='theme'),
    path('Themeform/',views.ThemeForm,name='Themeform')
]

urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
urlpatterns +=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)