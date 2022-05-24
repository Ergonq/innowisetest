from rest_framework import serializers

from ticket.models import Ticket, TicketComment


class TicketCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = TicketComment
        exclude = ("ticket",)


class TicketCommentUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = TicketComment
        fields = "__all__"
        read_only_fields = ("admin_response",)


class TicketSerializer(serializers.ModelSerializer):
    status_display = serializers.CharField(source="get_status_display", required=False)
    comments = TicketCommentSerializer(many=True, source="ticketcomment_set", required=False)

    class Meta:
        model = Ticket
        fields = "__all__"


class TicketUserSerializer(serializers.ModelSerializer):
    status_display = serializers.CharField(source="get_status_display", required=False)
    comments = TicketCommentSerializer(many=True, source="ticketcomment_set", required=False)

    class Meta:
        model = Ticket
        fields = "__all__"
        read_only_fields = ("admin_response", "status_display", "status", "user")
