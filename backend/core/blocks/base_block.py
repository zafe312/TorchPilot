from abc import ABC, abstractmethod
from utils.logger import setup_logger

logger = setup_logger(__name__)

class BaseBlock(ABC):
    """
    Abstract base for all PyTorch graph blocks.
    """
    def __init__(self, name: str, **params):
        self.name = name
        self.params = params
        logger.debug(f"Initialized block {self.name} with params {self.params}")

    @abstractmethod
    def to_code(self) -> str:
        """
        Convert this block into a snippet of PyTorch code.
        """
        pass
