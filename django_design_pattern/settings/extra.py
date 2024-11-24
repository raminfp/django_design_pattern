import os

from .base import *

# =============================================================================
# CACHE CONFIGURATION
# =============================================================================
REDIS_HOST = os.getenv('REDIS_HOST')
REDIS_PORT = os.getenv('REDIS_PORT')

# =============================================================================
# STORAGE CONFIGURATION
# =============================================================================
MINIO_ENDPOINT = os.getenv('MINIO_ENDPOINT')
MINIO_ACCESS_KEY = os.getenv('MINIO_ACCESS_KEY')
MINIO_SECRET_KEY = os.getenv('MINIO_SECRET_KEY')
MINIO_SECURE = os.getenv('MINIO_SECURE')

# =============================================================================
# TODO
# =============================================================================

