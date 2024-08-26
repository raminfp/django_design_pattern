# from injector import inject
from django_design_pattern.settings import client
from minio.error import S3Error
# from minio import Minio as MinioClient
# import os


class MinIOSDK:

    # @inject
    # def __init__(self, minio_client: MinioClient):
    #     self.client = minio_client
    #     self.bucket_name = os.getenv("BUCKET_NAME")

    # def new_find_object(self, object_name):
    #     try:
    #         stat = self.client.stat_object(self.bucket_name, object_name)
    #         return stat
    #     except S3Error:
    #         return None

    def find_object(self, bucket_name, object_name):
        try:
            stat = client.stat_object(bucket_name, object_name)
            return stat
        except S3Error:
            return None

    def search_objects(self, bucket_name, prefix=None, recursive=False):
        objects = client.list_objects(bucket_name, prefix=prefix, recursive=recursive)
        return list(objects)

    def delete_object(self, bucket_name, object_name):
        try:
            client.remove_object(bucket_name, object_name)
            return True
        except S3Error as err:
            return str(err)

    def update_object(self, bucket_name, object_name, file_path):
        try:
            client.fput_object(bucket_name, object_name, file_path)
            return True
        except S3Error as err:
            return str(err)

    def get_all_objects(self, bucket_name, prefix_name, recursive=False):
        objects = []
        for obj in client.list_objects(bucket_name, prefix=prefix_name, recursive=recursive):
            objects.append(obj)
        return objects

    def get_object_contents(self, bucket_name, object_name):
        try:
            object_data = client.get_object(bucket_name, object_name).read()
            return object_data
        except S3Error as err:
            return str(err)
