# jason-lee-tools

A tools for private cloud by Jason Lee.

## Installation

```bash
pip install jason-lee-tools


## 获取天气预报
api_key = ''  # 从和风天气获取的API密钥
location = '101010100'  # 北京的地点ID
weather = get_weather(api_key, location)
if 'error' not in weather:
    print(f"Location: {weather['location']}")
    print(f"Temperature: {weather['temperature']}°C")
    print(f"Weather: {weather['weather']}")
else:
    print(weather['error'])

## 发送短信提醒
api_key = '如有需要，找阿力'
api_secret = '如有需要，找阿力'

sms = SMS(api_key, api_secret)

phone = '18600806692'
msg = '你好，世界。'

try:
    response = sms.send(phone, msg)
    print('成功:', response)
except requests.exceptions.RequestException as e:
    print('请求失败:', e)

## 发送提醒邮件
api_key = '如有需要，找阿力'
api_secret = '如有需要，找阿力'

email = Mail(api_key, api_secret)

to = '5988628@qq.com'
subject = "你好"
body = '你好，世界。'

try:
    response = email.send(to, subject, body)
    print('成功:', response)
except requests.exceptions.RequestException as e:
    print('请求失败:', e)