"""
Example implementation of a traffic light system using the state design pattern
"""

from abc import ABC, abstractmethod
import time

RED_TIMEOUT_S: float = 4.0
YELLOW_TIMEOUT_S: float = 1.0
GREEN_TIMEOUT_S: float = 3.0
SYSTEM_RUN_TIME_S: float = 17.0


class InvalidStateError(Exception):
    """Error for requests to invalid states"""


# State interface that all states must adhere to
class AbstractTrafficState(ABC):
    """Interface for all traffic light states to implement"""

    @abstractmethod
    def enter(self, traffic_light: "TrafficLight") -> None:
        """Behavior when entering the state.

        :param traffic_light: TrafficLight system (state handler)
        """


# Concrete states to meet requirements
class Red(AbstractTrafficState):
    """Implementation of the behaviors within the Red light state."""

    def enter(self, traffic_light: "TrafficLight") -> None:
        print("Entering the Red state.")
        time.sleep(RED_TIMEOUT_S)
        print("Red light timer expired.")
        traffic_light.next_state = Green()


class Yellow(AbstractTrafficState):
    """Implementation of the behaviors within the Yellow light state."""

    def enter(self, traffic_light: "TrafficLight") -> None:
        print("Entering the Yellow state.")
        time.sleep(YELLOW_TIMEOUT_S)
        print("Yellow light timer expired.")
        traffic_light.next_state = Red()


class Green(AbstractTrafficState):
    """Implementation of the behaviors within the Green light state"""

    def enter(self, traffic_light: "TrafficLight") -> None:
        print("Entering the Green state.")
        time.sleep(GREEN_TIMEOUT_S)
        print("Green light timer expired.")
        traffic_light.next_state = Yellow()


class NullState(AbstractTrafficState):
    """Empty state for initialization"""

    def enter(self, traffic_light: "TrafficLight") -> None:
        raise InvalidStateError("Invalid state requested!!")


# State machine handler - representation of state machine
class TrafficLight:
    """Implementation of the traffic light state machine"""

    def __init__(self) -> None:
        self.red: AbstractTrafficState = Red()
        self.yellow: AbstractTrafficState = Yellow()
        self.green: AbstractTrafficState = Green()
        self.null: AbstractTrafficState = NullState()

        self.current_state: AbstractTrafficState = self.red
        self.next_state: AbstractTrafficState = self.null

    def run(self, duration_s: float = SYSTEM_RUN_TIME_S) -> None:
        """Runs the traffic light state machine"""
        start_time: float = time.time()
        while time.time() - start_time < duration_s:
            self.current_state.enter(self)
            self.current_state = self.next_state


def main() -> None:
    """Script for example state machine execution"""
    traffic_light = TrafficLight()

    # Run the state machine
    traffic_light.run()


if __name__ == "__main__":
    main()
