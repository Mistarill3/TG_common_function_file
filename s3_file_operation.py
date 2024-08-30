import json
import os
import boto3
import botocore


s3 = boto3.resource("s3")
bucket = s3.Bucket(os.environ["S3_BUCKET_NAME"])


def download_and_read_file(file_name):
    print("== s3_file_operation.py download_and_read_file")
    print(json.dumps({"file_name": str(file_name)}))
    downloaded_file_name = "downloaded_file.txt"
    
    try:
        bucket.download_file(file_name, "/tmp/"+downloaded_file_name)
        
    except botocore.exceptions.ClientError as e:
        print("== except")
        print(e.response["Error"])
        if e.response["Error"]["Code"] in (400, 403, 404, 429):
            return
        else:
            raise e

    with open("/tmp/" + downloaded_file_name, mode="r") as f:
        file_contents = f.read()
        return file_contents


def write_and_upload_file(new_file_contents, file_name):
    print("== s3_file_operation.py write_and_upload_file")
    print(json.dumps({"filename": str(file_name)}))

    with open("/tmp/test.txt", mode="w") as f:
        f.write(str(new_file_contents))
    bucket.upload_file("/tmp/test.txt", file_name)


def delete_file(file_name):
    print("== s3_file_operation.py delete_file")
    print(json.dumps({"filename": str(file_name)}))

    try:
        bucket.delete_objects(Delete={
            "Objects": [
                {
                    "Key": file_name
                }
            ]})

    except botocore.exceptions.ClientError as e:
        print("== except")
        print(e.response["Error"])
        if e.response["Error"]["Code"] in (400, 403, 404, 429):
            return
        else:
            raise e
