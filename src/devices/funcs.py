import json
import boto3
from botocore.config import Config

dynamo_config = Config(
    region_name='eu-west-2',
    signature_version='v4',
    retries = {
        'max_attemps': 10,
        'mode': 'standard'
    }
)

client = boto3.client('kinesis', config=dynamo_config)


def get_devices(context, event):
    return {
        "statusCode": 400,
        "body": json.dumps([
            {"id": "a", "devType": "co2", "name": "device1"},
            {"id": "b", "devType": "temperature", "name": "device2"}
        ]),
        "headers": {'Access-Control-Allow-Origin': '*'}
    }