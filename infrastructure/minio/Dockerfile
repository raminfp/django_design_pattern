FROM minio/minio:latest

WORKDIR /app

# Set the environment variables for Minio
ENV MINIO_ROOT_USER=your_minio_access_key
ENV MINIO_ROOT_PASSWORD=your_minio_secret_key

# Expose the Minio ports
#EXPOSE 9000 9001

# Start the Minio server
CMD ["minio", "server", "/data", "--config-dir", "/root/.minio"]
