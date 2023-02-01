# Name: Liam Nutley
# Email: liam.nutley@yahoo.ie
# Problem 2

import boto3

def list_s3_files_using_client():   # List files in S3 bucket
    """
    This functions list all files in s3 bucket.
    :return: None
    """

    s3_client = boto3.client("s3")
    bucket_name = "testbucket-frompython-2"
    response = s3_client.list_objects_v2(Bucket=bucket_name)
    files = response.get("Contents")
    for file in files:
        print(f"file_name: {file['Key']}, size: {file['Size']}")

from PIL import Image   # Transparent Pixel test
im = Image.open("test.png").convert("RGBA")
im.load()
print(im.getpixel((0, 0)))

if im.getpixel != (0, 225):
    class ObjectWrapper:
        """Encapsulates S3 object actions."""
        def __init__(self, s3_object):
            """
            :param s3_object: A Boto3 Object resource. This is a high-level resource in Boto3
                            that wraps object actions in a class-like structure.
            """
            self.object = s3_object
            self.key = self.object.key

        def copy(self, dest_object):
            try:
                dest_object.copy_from(CopySource={
                    'Bucket': self.object.bucket_name,
                    'Key': self.object.key
                })
                dest_object.wait_until_exists()
                logger.info(
                    "Copied object from %s:%s to %s:%s.",
                    self.object.bucket_name, self.object.key,
                    dest_object.bucket_name, dest_object.key)
            except ClientError:
                logger.exception(
                    "Couldn't copy object from %s/%s to %s/%s.",
                    self.object.bucket_name, self.object.key,
                    dest_object.bucket_name, dest_object.key)
                raise
elif im.getpixel(0, 225):
    img = Image.open('loadimage.jpg')
    img = img.save('savedimage.jpg')


