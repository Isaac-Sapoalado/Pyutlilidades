"""
URL configuration for pyutilidades project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from todo.views import Tarefa_View,Detail_Tarefa_View
from citacoes.views import CitacaoView
from forca.views import Palavraview

urlpatterns = [
    path('api/tarefa/', Tarefa_View.as_view()),
    path('api/palavra/', Palavraview.as_view()),
    path('api/tarefa/<int:pk>', Detail_Tarefa_View.as_view()),
    path('api/cita/', CitacaoView.as_view()),
    path('', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
