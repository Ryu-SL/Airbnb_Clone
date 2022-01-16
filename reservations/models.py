from unittest.mock import DEFAULT
from click import core
from django.db import models
from core import models as core_models


class Reservations(core_models.TimeStampedModel):
    """Reservation Model Def"""

    KEY_STATUS_PENDING = "pending"
    KEY_STATUS_CONFIRMED = "confirmed"
    KEY_STATUS_CANCELLED = "cancelled"
    STATUS_CHOICES = (
        (KEY_STATUS_PENDING, "Pending"),
        (KEY_STATUS_CONFIRMED, "Confirmed"),
        (KEY_STATUS_CANCELLED, "Cancelled"),
    )
    status = models.CharField(
        max_length=12, choices=STATUS_CHOICES, default=KEY_STATUS_PENDING
    )
    check_in = models.DateField()
    check_out = models.DateField()
    guest = models.ForeignKey("users.User", on_delete=models.CASCADE)
    room = models.ForeignKey("rooms.Room", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.guest.name}"
