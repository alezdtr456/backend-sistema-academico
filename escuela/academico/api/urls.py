from rest_framework.routers import DefaultRouter
from academico.api.views import (
    CarreraViewSet, AlumnoViewSet, MateriaViewSet, InscripcionViewSet,
)

router = DefaultRouter()
router.register('carreras', CarreraViewSet, basename='carrera')