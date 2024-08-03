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
from autorizar.views import CadastroView,LoginView,AlteraView
from blog.views import BlogView,ComentarioView,InteracaoView,AllBlogView,TagBlogView,TagView
from questao.views import Questao_View,Questao_Detail_View

urlpatterns = [
    path('api/tarefa/', Tarefa_View.as_view()),
    path('api/palavra/', Palavraview.as_view()),
    path('api/tarefa/<int:pk>', Detail_Tarefa_View.as_view()),
    path('api/cita/', CitacaoView.as_view()),
    path('api/blog/', AllBlogView.as_view()),
    path('api/tagblog/', TagBlogView.as_view()),
    path('api/tag/', TagView.as_view()),
    path('api/blog/<int:pk>', BlogView.as_view()),
    path('api/blog/coments/<int:pk>', ComentarioView.as_view()),
    path('api/blog/inter/<int:pk>', InteracaoView.as_view()),
    path('api/questao/<str:filtro>', Questao_Detail_View.as_view()),
    path('api/questao/', Questao_View.as_view()),
    path('auth/cadastrar/', CadastroView.as_view(),name='cadastro'),
    path('auth/login/', LoginView.as_view(),name='login'),
    path('auth/edit/', AlteraView.as_view(),name='alterar'),
    path('', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
