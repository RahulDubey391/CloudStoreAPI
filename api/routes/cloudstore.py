from ast import Store
from flask import Blueprint, request,jsonify
from ..controller import StoreOperator
from ..auth import Auth
from ..schema import StoreRequest
from marshmallow import ValidationError

CloudStoreEnd = Blueprint('CloudStoreEnd',__name__)

@CloudStoreEnd.route('/',methods=['GET'])
def index():
    return 'Welcome to CloudStore API'

@CloudStoreEnd.route('/uploadMedia',methods=['POST'])
def uploadMedia():
    args_json = request.get_json()
    try:
        storeSchema = StoreRequest()
        data = storeSchema.load(args_json)
    except:
        return jsonify({'message':'check your arguments'})

    file_name = data['file_name']
    flag = Auth.verify_token(data['access_token'])
    if flag:
        StoreOp = StoreOperator()
        return StoreOp.postMediaURL(file_name)
    elif flag == False:
        resp = jsonify({'message':'Access Token is invalid'})
        resp.status_code = 400
        return resp

@CloudStoreEnd.route('/getMedia',methods=['POST'])
def getMedia():
    args_json = request.get_json()
    try:
        storeSchema = StoreRequest()
        data = storeSchema.load(args_json)
    except:
        return jsonify({'message':'check your arguments'})

    file_name = data['file_name']
    flag = Auth.verify_token(data['access_token'])
    if flag == True:
        StoreOp = StoreOperator()
        return StoreOp.getMediaURL(file_name)
    elif flag == False:
        resp = jsonify({'message':'Access Token is invalid'})
        resp.status_code = 400
        return resp

@CloudStoreEnd.route('/deleteMedia',methods=['POST'])
def deleteMedia():
    args_json = request.get_json()
    try:
        storeSchema = StoreRequest()
        data = storeSchema.load(args_json)
    except:
        return jsonify({'message':'check your arguments'})

    file_name = data['file_name']
    flag = Auth.verify_token(data['access_token'])
    if flag == True:
        StoreOp = StoreOperator()
        return StoreOp.deleteMedia(file_name)
    elif flag == False:
        resp = jsonify({'message':'Access Token is invalid'})
        resp.status_code = 400
        return resp

@CloudStoreEnd.route('/listMedia',methods=['POST'])
def listMedia():
    args_json = request.get_json()
    try:
        storeSchema = StoreRequest()
        data = storeSchema.load(args_json)
    except:
        return jsonify({'message':'check your arguments'})

    token = data['access_token']
    flag = Auth.verify_token(token)
    if flag == True:
        StoreOp = StoreOperator()
        return StoreOp.listMedia()
    elif flag == False:
        resp = jsonify({'message':'Access Token is invalid'})
        resp.status_code = 400
        return resp