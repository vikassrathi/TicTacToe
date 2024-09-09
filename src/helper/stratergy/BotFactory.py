from src.Models.BotDifficulty import BotDifficulty
from src.helper.stratergy.botstrategy.Easy import Easy


class BotFactory:


    @staticmethod
    def getBot(difficulty):
        if difficulty==BotDifficulty.EASY:
            return Easy