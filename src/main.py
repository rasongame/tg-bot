from core.bot import bot
from config import cfg

def main():
    bot(cfg["API_TOKEN"])
if __name__ == '__main__':
    main()