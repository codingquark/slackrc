# -*- coding: utf-8 -*-
from irc3.plugins.command import command
import irc3
import asyncio
from slackclient import SlackClient


@irc3.plugin
class Plugin(object):
    token = ""
    slacker = SlackClient(token)

    def __init__(self, bot):
        self.bot = bot
        Plugin.slacker.rtm_connect()
        Plugin.channel = Plugin.slacker.server.channels.find("")

    @irc3.event(irc3.rfc.PRIVMSG)
    def forward_to_slack_on_priv_msg(self,
                                     data=None,
                                     tags=None,
                                     target=None,
                                     mask=None,
                                     **kw):
        """Forward incoming msg to Slack"""
        print("Received")
        print("target: " + target)
        print("data: " + data)
        print("mask: " + mask.nick)
        msg = "*Message from:* " + mask + "\n*Saying:* " + data
        Plugin.channel.send_message(msg)

    @command(permission='view')
    def echo(self, mask, target, args):
        """Echo

            %%echo <message>...
        """
        yield ' '.join(args['<message>'])


def main():
    loop = asyncio.get_event_loop()

    config = dict(
        autojoins=['#'],
        host='irc.freenode.net', port=6667, ssl=False,
        timeout=30,
        includes=[
            'irc3.plugins.core',
            __name__,
        ],
        loop=loop)

    irc3.IrcBot(nick="damnbot",
                password="botdamn",
                **config).run(forever=False)

    loop.run_forever()

if __name__ == '__main__':
    main()
