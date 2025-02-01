from rest_framework import viewsets
from rest_framework.response import Response
from .models import FAQ
from .serializers import FAQSerializer
from rest_framework.decorators import action

class FAQViewSet(viewsets.ModelViewSet):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer

    @action(detail=True, methods=['get'])
    def get_translated(self, request, pk=None):
        faq = self.get_object()
        lang = request.query_params.get('lang', 'en')  # Default language is English
        translated_data = faq.get_translated_text(lang)
        return Response(translated_data)

