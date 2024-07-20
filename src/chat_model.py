# chat_model.py

from typing import List, Iterable

from sparkai.llm.llm import ChatSparkLLM
from sparkai.core.messages import ChatMessage
from dwspark.config import Config
from loguru import logger

class ChatModel():
    def __init__(self, config: Config, domain: str = 'generalv3.5', model_url: str = 'wss://spark-api.xf-yun.com/v3.5/chat', stream:bool=False):
        '''
        初始化模型
        :param config: 项目配置文件
        :param domain: 调用模型
        :param llm_url: 模型地址
        :param stream: 是否启用流式调用
        '''
        self.spark = ChatSparkLLM(
            spark_api_url=model_url,
            spark_app_id=config.XF_APPID,
            spark_api_key=config.XF_APIKEY,
            spark_api_secret=config.XF_APISECRET,
            spark_llm_domain=domain,
            streaming=stream,
        )
        self.stream = stream

    def generate(self, msgs: str | List[ChatMessage]) -> str:
        '''
        批式调用
        :param msgs: 发送消息，接收字符串或列表形式的消息
        :return:
        '''
        if self.stream is True:
            raise Exception('模型初始化为流式输出，请调用generate_stream方法')

        messages = self.__trans_msgs(msgs)
        resp = self.spark.generate([messages])
        return resp.generations[0][0].text

    def generate_stream(self, msgs: str | List[ChatMessage]) -> Iterable[str]:
        '''
        流式调用
        :param msgs: 发送消息，接收字符串或列表形式的消息
        :return:
        '''
        if self.stream is False:
            raise Exception('模型初始化为流式输出，请调用generate方法')
        messages = self.__trans_msgs(msgs)
        resp_iterable = self.spark.stream(messages)
        for resp in resp_iterable:

            yield resp.content

    def __trans_msgs(self, msg: str):
        '''
        内部方法，将字符串转换为消息
        :param msgs: 字符串
        :return:
        '''
        if isinstance(msg, str):
            messages = [ChatMessage(role="user", content=msg)]
        else:
            messages = msg
        return messages