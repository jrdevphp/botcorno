from bot.cogs.modules.create_dirs import create_dirs
from bot.cogs.modules.create_flags import create_flags
from bot.cogs.modules.database import *
from bot.cogs.modules.patch_fix import *
from bot.bot import *
import asyncio


create_dirs(['temp', 'config/cert'])
create_flags()


def run():
    try:
        main()

    except KeyboardInterrupt:
        print('Bot encerrado pelo usuário!')
        asyncio.run(conn.close())
        exit()

    except Exception as e:
        print(f'Erro: {e}\n\nBot encerrado!')



if __name__ == '__main__':
    run()
