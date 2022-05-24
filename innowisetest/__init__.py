"""
This ensures that the app is loaded when Django starts so that the future @shared_task decorator will use it:
innowisetest/innowisetest/__init__.py:
"""
from .celery import app as celery_app

__all__ = ["celery_app"]
