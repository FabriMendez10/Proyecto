from django.urls import path
from .views import ListaAlumnos, DetalleAlumnos, CrearAlumnos, EditarAlumnos, EliminarAlumnos, Logueo, PaginaRegistro
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[path("",ListaAlumnos.as_view(), name="alumnos"),
             path("alumno/<int:pk>",DetalleAlumnos.as_view(), name="alumno"),
             path('login/', Logueo.as_view(), name="login"),
             path('registro/', PaginaRegistro.as_view(), name='registro'),
             path("logout/", LogoutView.as_view(next_page='login'),name="logout"),
             path("crear-alumnos/",CrearAlumnos.as_view(), name="crear-alumnos"),
             path("editar-alumnos/<int:pk>", EditarAlumnos.as_view(), name="editar-alumnos"),
             path("eliminar-alumnos/<int:pk>", EliminarAlumnos.as_view(), name="eliminar-alumnos")]
urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
