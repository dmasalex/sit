from django.urls import path
from .views import (SchoolboyListView,
                    ClassroomDetailView,
                    SchoolboyDetailView,
                    SchoolboyCreate,
                    TeacherDetail,
                    location,
                    SchoolboyUpdate,
                    SchoolboyDelete,
                    location_save,
                    location_now,
                    user_login,
                    user_logout,
                    print_location,
                    location_update,
                    boy_location_update
                    )
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', SchoolboyListView.as_view(), name='schoolboy'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('classroom/<str:slug>/', ClassroomDetailView.as_view(), name='classroom_detail'),
    path('teacher_detail/<str:slug>/', TeacherDetail.as_view(), name='teacher_detail'),
    path('schoolboy_create/', SchoolboyCreate.as_view(), name='schoolboy_create'),
    path('schoolboy_detail/<str:slug>/', SchoolboyDetailView.as_view(), name='schoolboy_detail'),
    path('schoolboy_update/<str:slug>/', SchoolboyUpdate.as_view(), name='schoolboy_update'),
    path('schoolboy_delete/<str:slug>/', SchoolboyDelete.as_view(), name='schoolboy_delete'),
    path('location/<str:slug>/', location, name='location'),
    path('location_now/<int:pk>/', location_now, name='location_now'),
    path('location_update/<int:pk>/', location_update, name='location_update'),
    path('boy_location_update/<str:slug>/', boy_location_update, name='boy_location_update'),
    path('location_save/<str:slug>/', location_save, name='location_save'),
    path('print_location/<int:pk>/', print_location, name='print_location')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
