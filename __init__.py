from nonebot import Bot
from nonebot.params import ShellCommandArgv, ShellCommandArgs
from nonebot.plugin.on import on_shell_command
from nonebot.rule import ArgumentParser, Namespace
from nonebot.log import logger
from nonebot.exception import ParserExit

from nonebot.adapters.onebot.v11 import Bot

parser = ArgumentParser()
parser.add_argument('--count')
parser.add_argument('--step')
parser.add_argument('--resolution')
parser.add_argument('--scale')
parser.add_argument('--present',action='store_true')
parser.add_argument('args',nargs='+')


command_test = on_shell_command("1", parser=parser)

@command_test.handle()
async def _(foo: ParserExit = ShellCommandArgs()):
    if foo.status == 0:
        await command_test.send(foo.message)  # help message
    else:
        await command_test.send(foo.message)  # error message

@command_test.handle()
async def _(bot:Bot,
            argv = ShellCommandArgv(), 
            args = ShellCommandArgs()):

    await command_test.send(f"{argv=} {args=}")
    logger.info(f"{argv=} {args=}")