from rest_framework import viewsets
from rent_ads.models import SearchHistory
from rent_ads.serializers.search_history import SearchHistorySerializer


class SearchHistoryViewSet(viewsets.ModelViewSet):
    queryset = SearchHistory.objects.all()
    serializer_class = SearchHistorySerializer

    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            serializer.save(user=self.request.user)
        else:
            if not self.request.session.session_key:
                self.request.session.save()

            serializer.save(session_key=self.request.session.session_key)