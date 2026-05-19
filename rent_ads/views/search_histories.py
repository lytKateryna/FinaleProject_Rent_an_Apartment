from django.db.models import Count
from rest_framework import mixins, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from rent_ads.models import SearchHistory
from rent_ads.serializers.search_history import SearchHistorySerializer


class SearchHistoryViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet
):
    queryset = SearchHistory.objects.all()
    serializer_class = SearchHistorySerializer

    def get_permissions(self):
        if self.action == 'popular':
            return [AllowAny()]
        return [IsAuthenticated()]

    @action(detail=False, methods=["get"])
    def popular(self, request):
        popular_keywords = (
            SearchHistory.objects
            .values('keyword')
            .annotate(count=Count('keyword'))
            .order_by('-count')[:10]
        )
        return Response(popular_keywords)