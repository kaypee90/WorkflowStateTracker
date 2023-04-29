from dataclasses import dataclass
from core import StateBase, StateMixin


@dataclass
class Delivery(StateMixin):
    workflow_id: ... = None
    status: ... = "ready"

class ReadyState(StateBase):
    def __init__(self):
        super().__init__(
            "ready",
            ["awaiting_pickup", "cancelled"]
        )

    def transition(self, delivery, forced_state=None):
        if forced_state:
            if forced_state in self.children:
                delivery.transition(forced_state)
                print(f"{self.name} -> {forced_state}")
                return
            else:
                raise ValueError("invalid state")
        
        delivery.transition(self.children[0])
        print(f"{self.name} -> {self.children[0]}")


class AwaitingPickupState(StateBase):
    def __init__(self):
        super().__init__(
            "awaiting_pickup",
            ["assign_rider", "cancelled"]
        )

    def transition(self, delivery, forced_state=None):
        if forced_state:
            if forced_state in self.children:
                delivery.transition(forced_state)
                print(f"{self.name} -> {forced_state}")
                return
            else:
                raise ValueError("invalid state")
        
        delivery.transition(self.children[0])
        print(f"{self.name} -> {self.children[0]}")

class AssignRiderState(StateBase):
    def __init__(self):
        super().__init__(
            "assign_rider",
            ["on_route", "assign_rider", "cancelled"]
        )

    def transition(self, delivery, forced_state=None):
        if forced_state:
            if forced_state in self.children:
                delivery.transition(forced_state)
                print(f"{self.name} -> {forced_state}")
                return
            else:
                raise ValueError("invalid state")
        
        delivery.transition(self.children[0])
        print(f"{self.name} -> {self.children[0]}")


class OnRouteState(StateBase):
    def __init__(self):
        super().__init__(
            "on_route",
            ["delivered", "cancelled"]
        )

    def transition(self, delivery, forced_state=None):
        if forced_state:
            if forced_state in self.children:
                delivery.transition(forced_state)
                print(f"{self.name} -> {forced_state}")
                return
            else:
                raise ValueError("invalid state")
        
        delivery.transition(self.children[0])
        print(f"{self.name} -> {self.children[0]}")


class CancelledState(StateBase):
    def __init__(self):
        super().__init__("cancelled")

    def transition(self, forced_state=None):
        print(f"{self.name} is a terminal status")


class DeliveredState(StateBase):
    def __init__(self):
        super().__init__("delivered")

    def transition(self, forced_state=None):
        print(f"{self.name} is a terminal status")

delivery_registry = {
    "ready": ReadyState(),
    "awaiting_pickup": AwaitingPickupState(),
    "assign_rider": AssignRiderState(),
    "on_route": OnRouteState(),
    "cancelled": CancelledState(),
    "delivered": DeliveredState(),
}