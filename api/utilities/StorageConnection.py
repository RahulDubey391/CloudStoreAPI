from google.cloud import storage

class StoreCon:
    def __init__(self,bucket_name):
        self.__credentials_file_path = '/app/credentials.json'
        self.__bucket_name = bucket_name

    def __repr__(self):
        return 'Bucket({%s})'%(self.__bucket_name)

    def __get_con(self):
        client = storage.Client().from_service_account_json(self.__credentials_file_path)
        bucket = client.get_bucket(self.__bucket_name)
        return bucket

    def GetCon(self):
        return self.__get_con()