class sysBot:
    def __init__(self, name, version, author):
        self.__name = name
        self.__version = version
        self.__author = author

    def display_info(self):
        print(f"Bot Name: {self.__name}")
        print(f"Version: {self.__version}")
        print(f"Author: {self.__author}")

bot_name = input("Enter your bot's name: ")
bot_version = input("Enter your bot's version: ")
bot_author = input("Enter the author's name: ")

my_bot = sysBot(bot_name, bot_version, bot_author)
my_bot.display_info()
