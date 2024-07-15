import requests
import hashlib
import hmac
import base64
import time

METHOD = "/sms/send"


def format_phone_number(phone_number):
    if phone_number.startswith("0086"):
        # 替换 0086 为 +86
        formatted_number = "+86" + phone_number[4:]
    elif len(phone_number) == 11:
        # 在 11 位号码前加上 +86
        formatted_number = "+86" + phone_number
    else:
        # 对于不符合上述条件的号码，保持原样
        formatted_number = phone_number

    return formatted_number


class SMS:
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

    def send(self, phone, msg, run_date):
        # 确保phone和msg参数是字符串
        if not isinstance(phone, str):
            phone = str(phone)
        if not isinstance(msg, str):
            msg = str(msg)

        phone = format_phone_number(phone)

        data = {
            'phone': phone,
            'msg': msg,
            'run_date': run_date,
            'type': 'sms'
        }

        if data.get('run_date') is None:
            data.pop('run_date', None)

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
    api_key = ''
    api_secret = ''

    sms = SMS(api_key, api_secret)

    phone = '18600806692'
    msg = '你好，世界。'

    try:
        response = sms.send(phone, msg, '2024-07-15 15:07:00')
        # response = sms.send(phone, msg, None)
        print('成功:', response)
    except requests.exceptions.RequestException as e:
        print('请求失败:', e)
