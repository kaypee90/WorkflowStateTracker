from dataclasses import dataclass
from abc import ABC, abstractmethod

@dataclass
class StateBase(ABC):
    name: ...
    children: ... = None

    @abstractmethod
    def transition(**kwargs):
        pass


class StateMixin(ABC):

    def transition(self, state):
        self.status = state

    @property
    def workflow_id(self):
        return self.workflow_id
