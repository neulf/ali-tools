import requests
import hashlib
import hmac
import base64
import time
import urllib.parse

METHOD = "/mail/send"


class Mail:
    def __init__(self, api_key, api_secret, url="https://api.lifang.fun"):
        self.api_key = api_key
        self.api_secret = api_secret
        self.url = url

    def generate_signature(self, params):
        # 对参数按key进行排序，并生成key1=value1&key2=value2的格式字符串
        sorted_params = sorted(params.items())
        message = "&".join(f"{k}={v}" for k, v in sorted_params)

        # 添加API_KEY和时间戳
        timestamp = str(int(time.time()))
        message = f"{self.api_key}{timestamp}{message}"

        # 生成签名
        secret_bytes = bytes(self.api_secret, 'utf-8')
        message_bytes = bytes(message, 'utf-8')
        signature = hmac.new(secret_bytes, message_bytes, hashlib.sha256).digest()
        return base64.b64encode(signature).decode(), timestamp

    def send(self, to, subject, body):

        data = {
            'recipient': to,
            'subject': subject,
            'body': body
        }

        # 生成签名字符串和时间戳
        signature, timestamp = self.generate_signature(data)

        # 设置请求头
        headers = {
            'API-Key': self.api_key,
            'Signature': signature,
            'Timestamp': timestamp,
            'Content-Type': 'application/json'
        }

        print(f"Sending request to {self.url + METHOD}")
        print(f"Headers: {headers}")
        print(f"Data: {data}")

        # 发送请求
        response = requests.post(self.url + METHOD, json=data, headers=headers)

        # 检查响应状态码
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: {response.status_code}, {response.text}")
            response.raise_for_status()


# 使用示例
if __name__ == "__main__":
    api_key = 'Please contact Jason Lee'
    api_secret = 'Please contact Jason Lee'

    email = Mail(api_key, api_secret)

    to = '5988628@qq.com'
    subject = "你好"
    body = '你好，世界。'

    try:
        response = email.send(to, subject, body)
        print('成功:', response)
    except requests.exceptions.RequestException as e:
        print('请求失败:', e)