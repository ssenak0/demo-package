import os
import sys
import json
import requests

sys.path.append(os.path.join(os.path.dirname(__file__),'../../'))

from sdks.novavision.src.base.environment import Environment

environment = Environment()
access_token = environment.access_token

ENDPOINT_URL = "http://127.0.0.1:8000/api"

def infer():
    # This is a sample request payload for ExecutorOne
    request_json = {
        'type': 'capsule', 
        'name': 'DemoPackageSena', 
        'configs': {
            'executor': {
                'name': 'ConfigExecutor', 
                'type': 'executor', 
                'field': 'dependentDropdownlist', 
                'value': {
                    'name': 'ExecutorOne', 
                    'type': 'object', 
                    'field': 'option', 
                    'value': {
                        'inputs': {
                            'inputImageOne': {
                                'name': 'inputImageOne', 
                                'type': 'object', 
                                'value': {
                                    'name': 'Image_dummy', 
                                    'value': '', 
                                    'type': 'Image', 
                                    'uID': 'dummy_id', 
                                    'mimeType': 'image/jpg', 
                                    'encoding': 'bytes', 
                                    'r_key': 'redis_dummy_key', 
                                    'shape_key': 'redis_shape_key'
                                }
                            }
                        }, 
                        'configs': {
                            'demoDependentDropdown': {
                                'name': 'DemoDependentDropdown', 
                                'value': {
                                    'name': 'OptionA', 
                                    'value': 'OptionA', 
                                    'type': 'string', 
                                    'field': 'option'
                                }, 
                                'type': 'object', 
                                'field': 'dependentDropdownlist', 
                                'restart': True
                            }
                        }
                    }
                }
            }
        }, 
        'uID': '1331112', 
        'debug': 'True'
    }
    
    headers = {
        "access-token": access_token
    }
    response = requests.post(ENDPOINT_URL, json=request_json, headers=headers, verify=False)
    print(response.raise_for_status())
    print(response.json())

if __name__ =="__main__":
    infer()
