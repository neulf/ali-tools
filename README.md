# jason-lee-tools

A tools for private cloud by Jason Lee.

## Installation

```bash
pip install jason-lee-tools

## 发送短信提醒
api_key = '如有需要，找阿力'
api_secret = '如有需要，找阿力'

sms = SMS(api_key, api_secret)

phone = '18600806692'
msg = '你好，世界。'

try:
    response = sms.send(phone, msg, '2024-07-15 13:46:00') #如果是立刻发哦送，最后一个参数可以为None
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
    response = email.send(to, subject, body, '2024-07-15 13:46:00') #如果是立刻发哦送，最后一个参数可以为None
    print('成功:', response)
except requests.exceptions.RequestException as e:
    print('请求失败:', e)

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
    
## 了解明天是否会下雨
api_key = ''  # 从和风天气获取的API密钥
location = '101010100'  # 北京的地点ID

tomorrow_weather = get_tomorrow_weather(api_key, location)
if 'error' not in tomorrow_weather:
    if will_it_rain_tomorrow(tomorrow_weather):
        print("明天会下雨")
    else:
        print("明天不会下雨")
else:
    print(tomorrow_weather['error'])                     