# demo.py

# 导入gradio、random、time库，他们的功能大致如名字所示
import gradio as gr # 通过as指定gradio库的别名为gr
import random
import time

# 自定义函数，功能是随机选返回指定语句，并与用户输入的 chat_query 一起组织为聊天记录的格式返回
def chat(chat_query, chat_history):
        # 在How are you 等语句里随机挑一个返回，放到 bot_message 变量里
        bot_message = random.choice(["How are you?", "I love you", "I'm very hungry"])
        # 添加到 chat_history 变量里
        chat_history.append((chat_query, bot_message))
        # 返回 空字符，chat_history 变量，空字符用于清空 chat_query 组件，chat_history 用于更新 chatbot组件
        return "", chat_history

# gr.Blocks()：布局组件，创建并给了他一个名字叫 demo
with gr.Blocks() as demo:
    # gr.Chatbot()：输入输出组件，用于展示对话效果
    chatbot = gr.Chatbot([], elem_id="chat-box", label="聊天历史")
    # gr.Textbox()：输入输出组件，用于展示文字
    chat_query = gr.Textbox(label="输入问题", placeholder="输入需要咨询的问题")
    # gr.Button：控制组件，用于点击，可绑定不同的函数触发处理
    llm_submit_tab = gr.Button("发送", visible=True)
    
    # gr.Examples(): 输入输出组件，用于展示组件的样例，点击即可将内容输入给 chat_query 组件
    gr.Examples(["请介绍一下Datawhale。", "如何在大模型应用比赛中突围并获奖？", "请介绍一下基于Gradio的应用开发"], chat_query)

    # 定义gr.Textbox()文字组件 chat_query 的 submit 动作(回车提交)效果，执行函数为 chat, 第一个[chat_query, chatbot]是输入，第二个 [chat_query, chatbot] 是输出
    chat_query.submit(fn=chat, inputs=[chat_query, chatbot], outputs=[chat_query, chatbot])
    # 定义gr.Button()控制组件 llm_submit_tab 的 点击动作 效果，执行函数为 chat, 第一个[chat_query, chatbot]是输入，第二个 [chat_query, chatbot] 是输出，效果与上一行代码同
    llm_submit_tab.click(fn=chat, inputs=[chat_query, chatbot], outputs=[chat_query, chatbot])

# 运行demo
if __name__ == '__main__':
    demo.queue().launch()