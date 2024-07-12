import requests

def get_weather(api_key, location):
    url = f"https://devapi.qweather.com/v7/weather/now?location={location}&key={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data.get('code') == '200':
            now = data['now']
            return {
                'location': location,
                'temperature': now['temp'],
                'weather': now['text']
            }
        else:
            return {"error": data.get('message', '无法获取天气数据')}
    else:
        return {"error": "请求失败"}

def get_tomorrow_weather(api_key, location):
    url = f"https://devapi.qweather.com/v7/weather/3d?location={location}&key={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data.get('code') == '200':
            return data['daily'][1]  # 获取明天的天气数据
        else:
            return {"error": data.get('message', '无法获取天气数据')}
    else:
        return {"error": "请求失败"}

def will_it_rain_tomorrow(tomorrow_weather):
    if '雨' in tomorrow_weather['textDay'] or '雨' in tomorrow_weather['textNight']:
        return True
    return False

if __name__ == "__main__":
    api_key = '62ed71f337ef4ef5a93f95b1af91ba12'  # 从和风天气获取的API密钥
    location = '101010100'  # 北京的地点ID
    
    tomorrow_weather = get_tomorrow_weather(api_key, location)
    if 'error' not in tomorrow_weather:
        if will_it_rain_tomorrow(tomorrow_weather):
            print("明天会下雨")
        else:
            print("明天不会下雨")
    else:
        print(tomorrow_weather['error'])