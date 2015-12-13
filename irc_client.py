# -*- coding: utf-8 -*-
from irc3.plugins.command import command
import irc3
import asyncio


@irc3.plugin
class Plugin(object):

    def __init__(self, bot):
        self.bot = bot

    @irc3.event(irc3.rfc.JOIN)
    def say_hi(self, mask, channel, **kw):
        """Say hi when someone join a channel"""
        if mask.nick != self.bot.nick:
            self.bot.privmsg(channel, 'Hi %s!' % mask.nick)
        else:
            self.bot.privmsg(channel, 'Hi!')

    @irc3.event(irc3.rfc.PRIVMSG)
    def say_hi_on_privmsg(self,
                          data=None,
                          tags=None,
                          target=None,
                          mask=None,
                          **kw):
        """Say hi when someone privmsg"""
        print("Received")
        print("target: " + target)
        print("data: " + data)
        print("mask: " + mask.nick)
        self.bot.privmsg(mask.nick, "Hi!")

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

    irc3.IrcBot(nick="damnbot", **config).run(forever=False)

    loop.run_forever()

if __name__ == '__main__':
    main()
