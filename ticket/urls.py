from django.urls import path
from rest_framework import routers

from .views import TicketView, TicketCommentView

router = routers.DefaultRouter()

router.register("tickets", TicketView)
router.register("ticket-comments", TicketCommentView)

urlpatterns = [] + router.urls
