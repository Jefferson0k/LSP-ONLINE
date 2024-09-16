from rest_framework import viewsets, permissions
from .models import Palabras
from .serialaizers import PalabrasSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

class PalabrasViewSet(viewsets.ModelViewSet):
    queryset = Palabras.objects.all()
    permission_classes= [permissions.AllowAny]
    serializer_class = PalabrasSerializer
    
    @action(detail=True,methods=['post'])
    def done(self, request, pk=None):
        Palabras = self.get_object()
        Palabras.done = not Palabras.done
        Palabras.save()
        return Response({
            'status': 'Palabra ya hecha' if Palabras.done else 'Palabra no hecha'
        },status=status.HTTP_200_OK)