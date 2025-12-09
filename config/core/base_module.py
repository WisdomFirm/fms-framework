from abc import ABC, abstractmethod

class BaseModule(ABC):
    """
    Abstract Base Class for all FMS modules.
    Ensures consistency across the framework.
    """
    
    def __init__(self, config):
        self.config = config

    @abstractmethod
    def execute(self):
        """
        The entry point for the module logic.
        Must return True if successful, False otherwise.
        """
        pass
