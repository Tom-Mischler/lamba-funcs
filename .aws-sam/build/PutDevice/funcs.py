import json
import os
from pprint import pprint
import boto3
from botocore.config import Config
from boto3.dynamodb.conditions import Key
from botocore.exceptions import ClientError


def get_devices(event, context):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(os.environ.get('devicesTable'))
    try:
        response = table.scan()
        devices = response['Items']
    except ClientError:
        return {
            "statusCode": 404,
            "error": "Devices not found"
        }
    else:
        return {
            "statusCode": 200,
            "body": {"devices": json.dumps(devices)},
            "headers": {'Access-Control-Allow-Origin': '*'}
        }


def put_device(event, context):
    deviceType="testType"
    deviceName="testName"
    id=event['pathParameters']['id']
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(os.environ.get('devicesTable'))
    res = table.put_item(
            Item={
                'id': id,
                'deviceType': deviceType,
                'deviceName': deviceName,
            }
        )
    return {
            "statusCode": 200,
            "body": json.dumps({"device": {"deviceId": id, "deviceName": deviceName, "deviceType": deviceType}}),
            "headers": {'Access-Control-Allow-Origin': '*'}
        }

# def delete_device(event, context):
#     deviceType="testType"
#     deviceName="testName"
#     id=event['pathParameters']['id']
#     dynamodb = boto3.resource('dynamodb')
#     table = dynamodb.Table(os.environ.get('devicesTable'))
#     res = table.delete(Key={'id': id})
#     return {
#             "statusCode": 200,
#             "body": json.dumps({"device": {"deviceId": id, "deviceName": deviceName, "deviceType": deviceType}}),
#             "headers": {'Access-Control-Allow-Origin': '*'}
#         }
