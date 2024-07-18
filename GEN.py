import random

def choose_reply():
    replies = ["祝你幸福，小可爱", "世界很大，不要浪费时间了", "玩游戏吗", "你无聊吗"]
    return random.choice(replies)

def main():
    while True:
        user_input = input("请输入任意文字（输入'退出'结束程序）：")
        if user_input.lower() == "退出":
            print("程序已退出。")
            break
        print("回复：", choose_reply())

if __name__ == "__main__":
    main()
