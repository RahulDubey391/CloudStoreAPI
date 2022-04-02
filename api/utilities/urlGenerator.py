from .StorageConnection import StoreCon
import datetime
from flask import jsonify

class UrlGenerator:
    def __init__(self,bucket_name,blob_name,method,timeout,content_type=None):
        self.__bucket_name = bucket_name
        self.__blob_name = blob_name
        self.__method = method
        self.__timeout = timeout
        self.__content_type = content_type
    
    def __repr__(self):
        return 'UrlGenerator(%s %s %s %s %s)'%(self.__method,self.__blob_name,self.__bucket_name,self.__timeout,self.__content_type)

    def __GenerateURL(self):
        con = StoreCon(self.__bucket_name)
        bucket = con.GetCon()
        blob = bucket.blob(self.__blob_name)
        url = blob.generate_signed_url(
            version="v4",
            expiration=datetime.timedelta(minutes=self.__timeout),
            method=self.__method,
            content_type=self.__content_type,
            )

        resp = jsonify({'message':{'%s URL'%self.__method:url}})
        resp.status_code = 200
        return resp

    def GetURL(self):
        return self.__GenerateURL()
