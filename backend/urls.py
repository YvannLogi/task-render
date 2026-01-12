from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import get_user_model


# add a temporary admin for deployment

User = get_user_model()
if not User.objects.filter(username='taskad').exists():
    User.objects.create_superuser('taskas', 'task@admin.com', 'Admin12345')
    print("ADMIN CRÉÉ SUR RENDER !")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('core.urls')),
]
