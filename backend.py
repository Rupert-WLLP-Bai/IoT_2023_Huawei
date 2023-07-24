# coding: utf-8

import json
from huaweicloudsdkcore.auth.credentials import GlobalCredentials
from huaweicloudsdkiam.v3.region.iam_region import IamRegion
from huaweicloudsdkcore.exceptions import exceptions
from huaweicloudsdkiam.v3 import *
from huaweicloudsdkcore.auth.credentials import BasicCredentials
from huaweicloudsdkcore.auth.credentials import DerivedCredentials
from huaweicloudsdkiotda.v5.region.iotda_region import IoTDARegion
from huaweicloudsdkcore.exceptions import exceptions
from huaweicloudsdkiotda.v5 import *

import requests
from flask import Flask, request, jsonify
from flask_cors import cross_origin

from flask_mail import Mail, Message

app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.qq.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = '1762161822@qq.com'
app.config['MAIL_PASSWORD'] = 'iwcrlvyimvtgdfja'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)

# 开启debug模式
app.config['DEBUG'] = True

# 将上面的代码封装成一个api, 用于获取设备的影子数据


@app.route('/getShadow', methods=['GET'])
@cross_origin()
def getShadow():
    ak = "LZT2LTWDS6KD7OCDGNC0"
    sk = "ZZPVHKvor5J2yeV9ssFCo65URh4eypaIEoDXpq2b"

    credentials = GlobalCredentials(ak, sk) \

    client = IamClient.new_builder() \
        .with_credentials(credentials) \
        .with_region(IamRegion.value_of("cn-north-4")) \
        .build()

    token = ''

    try:
        request = KeystoneCreateUserTokenByPasswordRequest()
        domainUser = PwdPasswordUserDomain(
            name="hw038474682"
        )
        userPassword = PwdPasswordUser(
            domain=domainUser,
            name="test",
            password="test123456"
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
    res = requests.get(
        'https://ad6c403b9e.st1.iotda-app.cn-north-4.myhuaweicloud.com:443/v5/iot/acc46a22c95b4b698483139e6f85df6f/devices/64ba9642b84c1334befb9589_060807/shadow', headers={'X-Auth-Token': token})
    # 将res.text字符串转为JSON对象
    resDict = json.loads(res.text)
    return jsonify(resDict)

# 向板子发送消息"ON"或"OFF"


@app.route('/sendMessage/<msg>', methods=['GET'])
@cross_origin()
def sendMessage(msg: str):
    ak = "LZT2LTWDS6KD7OCDGNC0"
    sk = "ZZPVHKvor5J2yeV9ssFCo65URh4eypaIEoDXpq2b"

    credentials = GlobalCredentials(ak, sk) \

    client = IamClient.new_builder() \
        .with_credentials(credentials) \
        .with_region(IamRegion.value_of("cn-north-4")) \
        .build()

    token = ''

    try:
        request = KeystoneCreateUserTokenByPasswordRequest()
        domainUser = PwdPasswordUserDomain(
            name="hw038474682"
        )
        userPassword = PwdPasswordUser(
            domain=domainUser,
            name="test",
            password="test123456"
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
    res = requests.post('https://ad6c403b9e.st1.iotda-app.cn-north-4.myhuaweicloud.com:443/v5/iot/acc46a22c95b4b698483139e6f85df6f/devices/64ba9642b84c1334befb9589_060807/commands',
                        headers={'X-Auth-Token': token}, json={"service_id": "Cable_anti-stealing", "command_name": "autoControl", "paras": {"alarm": "{}".format(msg)}})
    # 将res.text字符串转为JSON对象
    resDict = json.loads(res.text)
    return jsonify(resDict)

# 向板子发送消息重置电缆状态


@app.route('/resetStatus/<status>', methods=['GET'])
@cross_origin()
def resetStatus(status: str):
    ak = "LZT2LTWDS6KD7OCDGNC0"
    sk = "ZZPVHKvor5J2yeV9ssFCo65URh4eypaIEoDXpq2b"

    credentials = GlobalCredentials(ak, sk) \

    client = IamClient.new_builder() \
        .with_credentials(credentials) \
        .with_region(IamRegion.value_of("cn-north-4")) \
        .build()

    token = ''

    try:
        request = KeystoneCreateUserTokenByPasswordRequest()
        domainUser = PwdPasswordUserDomain(
            name="hw038474682"
        )
        userPassword = PwdPasswordUser(
            domain=domainUser,
            name="test",
            password="test123456"
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
    res = requests.post('https://ad6c403b9e.st1.iotda-app.cn-north-4.myhuaweicloud.com:443/v5/iot/acc46a22c95b4b698483139e6f85df6f/devices/64ba9642b84c1334befb9589_060807/commands',
                        headers={'X-Auth-Token': token}, json={"service_id": "Cable_anti-stealing", "command_name": "reset", "paras": {"cable_status": "{}".format(status)}})
    # 将res.text字符串转为JSON对象
    resDict = json.loads(res.text)
    return jsonify(resDict)
    
# 使用GET写一个发送邮件的api
@app.route('/sendEmail/<email_address>/<subject>/<content>', methods=['GET'])
@cross_origin()
def sendEmailByGet(email_address: str, subject: str, content: str):
    # 发送邮件
    msg = Message(
        subject=subject,
        sender=app.config['MAIL_USERNAME'],
        recipients=[email_address],
        body=content
    )
    mail.send(msg)
    return "success"

# 使用POST写一个发送邮件的api
@app.route('/sendEmailByPost', methods=['POST'])
@cross_origin()
def sendEmailByPost():
    email_address = request.form.get('email_address')
    subject = request.form.get('subject')
    content = request.form.get('content')
    # 发送邮件
    msg = Message(
        subject=subject,
        sender=app.config['MAIL_USERNAME'],
        recipients=[email_address],
        body=content
    )
    mail.send(msg)
    return "success"

if __name__ == '__main__':
    app.run()
