import requests


def query_weather(api_key, city="Beijing", units="metric", language="zh_cn"):
    # 第一步：设置在线天气预报 API 接口
    url = "https://api.openweathermap.org/data/2.5/weather"

    # 第二步：设置天气预报接口参数
    params = {
        "q": city,  # 查询的城市，默认为北京
        "appid": api_key,  # API 密钥
        "units": units,  # 测量单位，默认为摄氏度
        "lang": language,  # 输出语言，默认为简体中文
    }

    # 第三步：请求天气预报接口
    response = requests.get(url, params=params)

    # 第四步：检查响应状态
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"查询失败，状态码：{response.status_code}")
        print("响应数据：", response.text)


if __name__ == '__main__':
    # 第一步：获取天气预报网站 API 访问密钥
    open_weather_key = 'open_weather_key'

    # 第二步：调用函数，查询北京的天气
    city_weather = query_weather(open_weather_key, city="beijing")

    # 第三步：打印天气信息
    print("city_weather", city_weather)
