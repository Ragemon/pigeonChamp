from django.contrib import admin
from django.urls import path, include
import accounts.urls, mailinglist.urls
urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include(accounts.urls, namespace='accounts')),
    path('maillinglist/', include(mailinglist.urls, namespace='mailinglist',))
]
