# -*- coding: utf-8 -*-
import time
from slackclient import SlackClient


def main():
    token = "token"
    sc = SlackClient(token)
    if sc.rtm_connect():
        while True:
            print(sc.rtm_read())
            time.sleep(1)
            channel = sc.server.channels.find('channel')
            channel.send_message('test')
    else:
        print("Connection failed, invalid token?")

if __name__ == '__main__':
    main()
