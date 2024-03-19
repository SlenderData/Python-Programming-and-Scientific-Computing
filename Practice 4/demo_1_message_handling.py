# 当前日期：2024-03-19
# 姓名：马云骥
# 显示和发送消息

def show_messages(messages):
    # 显示列表中的所有消息
    for message in messages:
        print(message)


def send_messages(messages, sent_messages):
    # 打印每条消息，并将其移到新列表中
    while messages:
        current_message = messages.pop(0)  # 发送队首消息
        print(f"发送消息: {current_message}")
        sent_messages.append(current_message)


messages = ["Hello there!", "How are you?", "Welcome to Python programming."]
sent_messages = []

print("发送前原始消息列表:")
show_messages(messages)
print("")
send_messages(messages, sent_messages)
print("\n发送后原始消息列表:")
show_messages(messages)
print("\n已发送消息列表:")
show_messages(sent_messages)
