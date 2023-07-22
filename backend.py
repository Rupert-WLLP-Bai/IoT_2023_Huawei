# coding: utf-8

import json
from huaweicloudsdkcore.auth.credentials import GlobalCredentials
from huaweicloudsdkiam.v3.region.iam_region import IamRegion
from huaweicloudsdkcore.exceptions import exceptions
from huaweicloudsdkiam.v3 import *
import requests
from flask import Flask, request, jsonify
from flask_cors import cross_origin

app = Flask(__name__)
    
# 将上面的代码封装成一个api, 用于获取设备的影子数据
@app.route('/getShadow', methods=['GET'])
@cross_origin()
def getShadow():
    ak = "VQY1PB4VQU4RKHIRABBV"
    sk = "kQSPGRD6fekezCOqazdzczSmPkFghmPcS6QqMkT0"

    credentials = GlobalCredentials(ak, sk) \

    client = IamClient.new_builder() \
        .with_credentials(credentials) \
        .with_region(IamRegion.value_of("cn-north-4")) \
        .build()

    token = ''
    
    try:
        request = KeystoneCreateUserTokenByPasswordRequest()
        domainUser = PwdPasswordUserDomain(
            name="hw062436146"
        )
        userPassword = PwdPasswordUser(
            domain=domainUser,
            name="bjh",
            password="bjh123456"
        )
        passwordIdentity = PwdPassword(
            user=userPassword
        )
        listMethodsIdentity = [
            "password"
        ]
        identityAuth = PwdIdentity(
            methods=listMethodsIdentity,
            password=passwordIdentity
        )
        authbody = PwdAuth(
            identity=identityAuth
        )
        request.body = KeystoneCreateUserTokenByPasswordRequestBody(
            auth=authbody
        )
        response = client.keystone_create_user_token_by_password(request)
        # 将response字符串转为JSON对象
        responseDict = json.loads(str(response))
        # print(responseDict['X-Subject-Token'])
        
    except exceptions.ClientRequestException as e:
        print(e.status_code)
        print(e.request_id)
        print(e.error_code)
        print(e.error_msg)
        
    # 将获取到的token用于请求
    # 写在header中，格式为：X-Auth-Token: {token}
    token = responseDict['X-Subject-Token']
    res = requests.get('https://31aa25a0ff.st1.iotda-app.cn-north-4.myhuaweicloud.com:443/v5/iot/4e904ef96d5b49fca0b700215fb24b60/devices/64a82203ae80ef457fc07576_1230/shadow', headers={'X-Auth-Token': token})
    # 将res.text字符串转为JSON对象
    resDict = json.loads(res.text)
    return jsonify(resDict)

if __name__ == '__main__':
    app.run()