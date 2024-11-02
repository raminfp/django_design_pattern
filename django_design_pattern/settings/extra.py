from .base import *

# =============================================================================
# CACHE CONFIGURATION
# =============================================================================
REDIS_HOST = 'localhost'
REDIS_PORT = 6379

# =============================================================================
# STORAGE CONFIGURATION
# =============================================================================
MINIO_ENDPOINT = os.getenv('MINIO_ENDPOINT')
MINIO_ACCESS_KEY = os.getenv('MINIO_ACCESS_KEY')
MINIO_SECRET_KEY = os.getenv('MINIO_SECRET_KEY')
MINIO_SECURE = os.getenv('MINIO_SECURE')



