from abc import ABC,abstractmethod
class BotStrategy(ABC):

    @abstractmethod
    def decide_move(self,board):
        """

        :type board: object
        """
        raise NotImplementedError
    
