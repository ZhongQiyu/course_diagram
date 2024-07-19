# demo.py

import requests
import time
import hashlib
import base64
import json
from sparkai.llm.llm import ChatSparkLLM, ChunkPrintHandler
from sparkai.core.messages import ChatMessage

# Replace these with your own values
APPID = 'ccb83ac9'  # 替换为你的AppID
API_KEY = '14362ac45a6c18985ee0731c06235cb0'  # 替换为你的API Key
API_SECRET = 'ZGM1MzIzZmIwNTAwYzM4Y2Y1MjlkZGY3'  # 替换为你的API Secret
AUDIO_FILE = 'path_to_your_audio_file.wav'  # 替换为你的音频文件路径

# 星火认知大模型Spark Max的URL值
SPARKAI_URL = 'wss://spark-api.xf-yun.com/v3.5/chat'

# 星火认知大模型调用秘钥信息
SPARKAI_APP_ID = 'ccb83ac9'
SPARKAI_API_SECRET = 'ZGM1MzIzZmIwNTAwYzM4Y2Y1MjlkZGY3'
SPARKAI_API_KEY = '14362ac45a6c18985ee0731c06235cb0'

# 星火认知大模型Spark Max的domain值
SPARKAI_DOMAIN = 'generalv3.5'

# 获取时间戳
def get_timestamp():
    return str(int(time.time()))

# 生成签名
def get_signature(api_key, api_secret, timestamp):
    signature = api_key + timestamp + api_secret
    hash = hashlib.md5()
    hash.update(signature.encode('utf-8'))
    return hash.hexdigest()

# 获取鉴权参数
def get_auth_params(api_key, api_secret):
    timestamp = get_timestamp()
    signature = get_signature(api_key, api_secret, timestamp)
    params = {
        'appid': APPID,
        'timestamp': timestamp,
        'sign': signature,
    }
    return params

# 读取音频文件
def read_audio(file_path):
    with open(file_path, 'rb') as f:
        audio_data = f.read()
    return audio_data

# 发送请求
def send_request(url, headers, data):
    response = requests.post(url, headers=headers, data=data)
    return response.json()

# 调用讯飞ASR服务
def call_asr():
    url = "http://api.xfyun.cn/v1/service/v1/iat"
    audio_data = read_audio(AUDIO_FILE)
    audio_base64 = base64.b64encode(audio_data).decode('utf-8')

    params = get_auth_params(API_KEY, API_SECRET)
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8',
        'X-Appid': APPID,
        'X-CurTime': params['timestamp'],
        'X-Param': base64.b64encode(json.dumps({
            'engine_type': 'sms16k',
            'aue': 'raw'
        }).encode('utf-8')).decode('utf-8'),
        'X-CheckSum': params['sign'],
    }
    data = {
        'audio': audio_base64
    }

    response = send_request(url, headers, data)
    print("ASR Response:", response)
    return response

# 调用讯飞Spark大语言模型
def call_llm(user_input):
    spark = ChatSparkLLM(
        spark_api_url=SPARKAI_URL,
        spark_app_id=SPARKAI_APP_ID,
        spark_api_key=SPARKAI_API_KEY,
        spark_api_secret=SPARKAI_API_SECRET,
        spark_llm_domain=SPARKAI_DOMAIN,
        streaming=False,
    )
    messages = [ChatMessage(
        role="user",
        content=user_input
    )]
    handler = ChunkPrintHandler()
    response = spark.generate([messages], callbacks=[handler])
    print("LLM Response:", response)
    return response

if __name__ == "__main__":
    # 调用ASR
    asr_result = call_asr()

    # 假设ASR结果中包含识别到的文本内容
    if 'data' in asr_result and 'result' in asr_result['data']:
        recognized_text = asr_result['data']['result']
        print("Recognized Text:", recognized_text)

        # 调用LLM
        llm_result = call_llm(recognized_text)
        print("LLM Result:", llm_result)
    else:
        print("ASR failed to recognize text.")
