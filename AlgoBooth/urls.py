from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , include('register.urls')),
    path('problem/' , include('problemPage.urls')),
    path('add_problem/' , include('addProblem.urls')),
    path('blog/' , include('blogPage.urls')),
    path('add_blog/' , include('addBlog.urls')),
    path('' , include('dashboard.urls')),
    path('profile_page/' , include('profilePage.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)