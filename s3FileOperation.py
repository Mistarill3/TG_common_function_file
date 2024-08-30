import json
import os
import boto3
import botocore


s3 = boto3.resource("s3")
bucket = s3.Bucket(os.environ["S3_BUCKET_NAME"])


def downloadAndReadFile(fileName):
    print("==s3FileOperation.py downloadAndReadFile")
    print(json.dumps({"filename": str(fileName)}))
    downloadedFileName = "downloadedFile.txt"
    
    try:
        bucket.download_file(fileName, "/tmp/"+downloadedFileName)
        
    except botocore.exceptions.ClientError as e:
        print("==except")
        print(e.response["Error"])
        if e.response["Error"]["Code"] in (400, 403, 404, 429):
        #if (e.response["Error"]["Code"] == "400" or
            #e.response["Error"]["Code"] == "403" or
            #e.response["Error"]["Code"] == "404" or
            #e.response["Error"]["Code"] == "429"):
            return
        else:
            raise e

    with open("/tmp/" + downloadedFileName, mode="r") as f:
        fileContents = f.read()
        return fileContents



def writeAndUploadFile(newFileContents, fileName):
    print("==s3FileOperation.py writeAndUploadFile")
    print(json.dumps({"filename": str(fileName)}))

    with open("/tmp/test.txt", mode="w") as f:
        f.write(str(newFileContents))
    bucket.upload_file("/tmp/test.txt", fileName)



def deleteFile(fileName):
    print("==s3FileOperation.py deleteFile")
    print(json.dumps({"filename": str(fileName)}))

    try:
        bucket.delete_objects(Delete={
            "Objects": [
                {
                    "Key": fileName
                }
            ]})

    except botocore.exceptions.ClientError as e:
        print("==except")
        print(e.response["Error"])
        if e.response["Error"]["Code"] in (400, 403, 404, 429):
        #if (e.response["Error"]["Code"] == "400" or
            #e.response["Error"]["Code"] == "403" or
            #e.response["Error"]["Code"] == "404" or
            #e.response["Error"]["Code"] == "429"):
            return
        else:
            raise e
