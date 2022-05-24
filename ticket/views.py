from rest_framework.permissions import IsAuthenticated

from rest_framework.viewsets import ModelViewSet

from ticket.models import Ticket, TicketComment

from ticket.serializers import (
    TicketSerializer,
    TicketCommentSerializer,
    TicketUserSerializer,
    TicketCommentUserSerializer,
)


class TicketView(ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    permission_classes = [
        IsAuthenticated,
    ]

    def get_serializer_class(self):
        if self.request.user.is_staff:
            return TicketSerializer
        return TicketUserSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        if self.request.user.is_staff:
            return Ticket.objects.all()
        return Ticket.objects.filter(user=self.request.user)


class TicketCommentView(ModelViewSet):
    queryset = TicketComment.objects.all()
    serializer_class = TicketCommentSerializer
    permission_classes = [
        IsAuthenticated,
    ]

    def get_serializer_class(self):
        if self.request.user.is_staff:
            return TicketCommentSerializer
        return TicketCommentUserSerializer

    def get_queryset(self):
        if self.request.user.is_staff:
            return TicketComment.objects.all()
        return TicketComment.objects.filter(user=self.request.user)
