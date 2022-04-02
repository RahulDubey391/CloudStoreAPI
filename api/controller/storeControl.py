from wsgiref import headers
from ..config import Config
from flask import jsonify
import datetime
from mimetypes import MimeTypes
from ..utilities import FileExtension,UrlGenerator,StoreCon

class StoreOperator:
    def postMediaURL(self,blob_name):
        fileExt = FileExtension(blob_name)
        flag = fileExt.checkExtension()
        ext_flag = flag 
        if ext_flag == False:
            resp = jsonify({'message':'File Extension not allowed'})
            resp.status_code = 400
            return resp
        else:
            content_type = MimeTypes().guess_type(blob_name)[0]    
            urlGen = UrlGenerator(Config.UPLOAD_BUCKET_NAME,blob_name,'PUT',1,content_type)
            resp = urlGen.GetURL()
            return resp
    
    def getMediaURL(self,blob_name):
        con = StoreCon(Config.UPLOAD_BUCKET_NAME)
        bucket = con.GetCon()
        blob = bucket.blob(blob_name)
        if blob.exists():
            urlGen = UrlGenerator(Config.UPLOAD_BUCKET_NAME,blob_name,'GET',1)
            resp = urlGen.GetURL()
            return resp
        else:
            resp = jsonify({'message':'File does not exists'})
            resp.status_code = 400
            return resp

    def deleteMedia(self,blob_name):
        con = StoreCon(Config.UPLOAD_BUCKET_NAME)
        bucket = con.GetCon()
        blob = bucket.blob(blob_name)
        blob.delete()
        resp = jsonify({'message':'Media %s Deleted'%blob_name})
        return resp

    def listMedia(self):
        con = StoreCon(Config.UPLOAD_BUCKET_NAME)
        bucket = con.GetCon()
        blobs = bucket.list_blobs()
        blob_names = []
        for blob in blobs:
            blob_names.append(blob.name)
        resp = jsonify({'message':{'Media Files':blob_names}})
        resp.status_code = 200
        return resp