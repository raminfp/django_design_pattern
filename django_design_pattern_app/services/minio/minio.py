from injector import inject
import io
from minio import Minio as MinioClient
import os


class MinioSDK:

    @inject
    def __init__(self, minio_client: MinioClient):
        self.client = minio_client
        self.bucket_name = os.getenv("BUCKET_NAME")

    def new_find_object(self, object_name):
        stat = self.client.stat_object(self.bucket_name, object_name)
        return stat

    def find_object(self, bucket_name, object_name):
        stat = self.client.stat_object(bucket_name, object_name)
        return stat

    def search_objects(self, bucket_name, prefix=None, recursive=False):
        objects = self.client.list_objects(bucket_name, prefix=prefix, recursive=recursive)
        return list(objects)

    def delete_object(self, bucket_name, object_name):
        self.client.remove_object(bucket_name, object_name)
        return True

    def update_object(self, bucket_name, object_name, file_path):
        self.client.fput_object(bucket_name, object_name, file_path)
        return True

    def upload_file(self, bucket_name, object_name, content):
        # Convert the bytes content into a byte stream (file-like object)
        byte_stream = io.BytesIO(content)

        # Upload the content to MinIO
        self.client.put_object(
            bucket_name=bucket_name,
            object_name=object_name,
            data=byte_stream,
            length=len(content)
        )

    def create_bucket(self, bucket_name):
        if not self.client.bucket_exists(bucket_name):
            self.client.make_bucket(bucket_name)
            return True
        else:
            return False

    def delete_all_objects(self, bucket_name):

        # List all objects in the bucket
        objects = self.client.list_objects(bucket_name, recursive=True)
        for obj in objects:
            self.client.remove_object(bucket_name, obj.object_name)

    def delete_bucket(self, bucket_name):

        # First delete all objects in the bucket
        self.delete_all_objects(bucket_name)
        # Then delete the bucket
        self.client.remove_bucket(bucket_name)

    def get_all_objects(self, bucket_name, prefix_name=None, recursive=True):
        objects = []
        domain = os.getenv("DOMAIN")
        for obj in self.client.list_objects(bucket_name, prefix=prefix_name, recursive=recursive):
            object_names = f"{domain}{obj.object_name}"
            objects.append(object_names)
        return objects

    def get_object_contents(self, bucket_name, object_name):
        object_data = self.client.get_object(bucket_name, object_name).read()
        return object_data
