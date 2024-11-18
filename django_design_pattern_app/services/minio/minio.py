from injector import inject
import io
from minio import Minio as MinioClient
import os


class MinioSDK:

    @inject
    def __init__(self, minio_client: MinioClient):
        """
        Constructor for MinioSDK.

        Parameters
        ----------
        minio_client : MinioClient
            MinIO service object
        """
        self.client = minio_client
        self.bucket_name = os.getenv("BUCKET_NAME")

    def new_find_object(self, object_name):
        """
        Find an object in MinIO.

        Given the object name, find the object in the default bucket.

        Parameters
        ----------
        object_name : str
            The name of the object to find

        Returns
        -------
        stat: StatObject
            The object's metadata
        """
        stat = self.client.stat_object(self.bucket_name, object_name)
        return stat


    def search_objects(self, bucket_name, prefix=None, recursive=False):
        """
        Search for objects in MinIO.

        Given the bucket name, prefix and recursive flag, search for objects in MinIO.

        Parameters
        ----------
        bucket_name : str
            The name of the bucket to search in
        prefix : str
            The prefix of the objects to search for
        recursive : bool
            Whether to search recursively or not

        Returns
        -------
        objects : list[Minio.Object]
            A list of objects that match the search criteria
        """
        objects = self.client.list_objects(bucket_name, prefix=prefix, recursive=recursive)
        return list(objects)

    def delete_object(self, bucket_name, object_name):
        """
        Delete an object from the specified bucket.

        Given the bucket name and object name, delete the object from the bucket.

        Parameters
        ----------
        bucket_name : str
            The name of the bucket to delete the object from
        object_name : str
            The name of the object to delete

        Returns
        -------
        bool
            Whether the object was successfully deleted
        """
        self.client.remove_object(bucket_name, object_name)
        return True

    def update_object(self, bucket_name, object_name, file_path):
        """
        Update an object in the specified bucket.

        Given the bucket name, object name and local file path, update the object in the bucket.

        Parameters
        ----------
        bucket_name : str
            The name of the bucket to update the object in
        object_name : str
            The name of the object to update
        file_path : str
            The path to the file to update with

        Returns
        -------
        bool
            Whether the object was successfully updated
        """
        self.client.fput_object(bucket_name, object_name, file_path)
        return True

    def upload_file(self, bucket_name, object_name, content):
        # Convert the bytes content into a byte stream (file-like object)
        """
        Upload the given content to the specified bucket as the given object name.

        Given the bucket name, object name and the content to upload, upload the content to the bucket.

        Parameters
        ----------
        bucket_name : str
            The name of the bucket to upload the object to
        object_name : str
            The name of the object to upload
        content : bytes
            The bytes content to upload

        Returns
        -------
        bool
            Whether the object was successfully uploaded
        """
        byte_stream = io.BytesIO(content)

        # Upload the content to MinIO
        self.client.put_object(
            bucket_name=bucket_name,
            object_name=object_name,
            data=byte_stream,
            length=len(content)
        )

    def create_bucket(self, bucket_name):
        """
        Create a new bucket in MinIO.

        Given the bucket name, create a new bucket in MinIO if it doesn't already exist.

        Parameters
        ----------
        bucket_name : str
            The name of the bucket to create

        Returns
        -------
        bool
            Whether the bucket was successfully created
        """
        if not self.client.bucket_exists(bucket_name):
            self.client.make_bucket(bucket_name)
            return True
        else:
            return False

    def delete_all_objects(self, bucket_name):

        # List all objects in the bucket
        """
        Delete all objects in a given bucket.

        Given the bucket name, delete all objects in the bucket.

        Parameters
        ----------
        bucket_name : str
            The name of the bucket to delete all objects from

        Returns
        -------
        bool
            Whether all objects were successfully deleted
        """
        objects = self.client.list_objects(bucket_name, recursive=True)
        for obj in objects:
            self.client.remove_object(bucket_name, obj.object_name)

    def delete_bucket(self, bucket_name):

        # First delete all objects in the bucket
        """
        Delete the given bucket.

        Given the bucket name, delete all objects in the bucket and then the bucket itself.

        Parameters
        ----------
        bucket_name : str
            The name of the bucket to delete

        Returns
        -------
        bool
            Whether the bucket was successfully deleted
        """
        self.delete_all_objects(bucket_name)
        # Then delete the bucket
        self.client.remove_bucket(bucket_name)

    def get_all_objects(self, bucket_name, prefix_name=None, recursive=True):
        """
        Get a list of all object names in the given bucket.

        Given the bucket name and optional prefix name and recursive flag,
        return a list of all object names in the bucket.

        Parameters
        ----------
        bucket_name : str
            The name of the bucket to list all objects from
        prefix_name : str
            The prefix of the objects to search for
        recursive : bool
            Whether to search for objects recursively or not

        Returns
        -------
        list[str]
            A list of all object names in the bucket
        """
        objects = []
        domain = os.getenv("DOMAIN")
        for obj in self.client.list_objects(bucket_name, prefix=prefix_name, recursive=recursive):
            object_names = f"{domain}{obj.object_name}"
            objects.append(object_names)
        return objects

    def get_object_contents(self, bucket_name, object_name):
        """
        Get the contents of the specified object in the given bucket.

        Given the bucket name and object name, retrieve the contents of the object and return them as bytes.

        Parameters
        ----------
        bucket_name : str
            The name of the bucket to retrieve the object from
        object_name : str
            The name of the object to retrieve

        Returns
        -------
        bytes
            The contents of the object as bytes
        """
        object_data = self.client.get_object(bucket_name, object_name).read()
        return object_data
