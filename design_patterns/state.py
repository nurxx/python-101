from abc import ABCMeta, abstractmethod

class State(metaclass=ABCMeta):
    @abstractmethod
    def change_state(self):
        raise ImplementationError('Not implemented <change_state> method')


class TurnedOn(State):
    def change_state(self):
        return 'Turned ON'


class TurnedOff(State):
    def change_state(self):
        return 'Turned OFF'


class Lamp(State):
    def __init__(self):
        self._state = None

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, new_state):
        self._state = new_state

    def change_state(self):
        self._state = self._state.change_state()


def main():
    lamp = Lamp()
    on = TurnedOn()
    off = TurnedOff()

    print("Lamp's current state: {0}".format(lamp.state))

    print('Turning ON ...')
    lamp.state = on
    lamp.change_state()
    print("Lamp's current state: {0}".format(lamp.state))

    print('Turning OFF ...')
    lamp.state = off
    lamp.change_state()
    print("Lamp's current state: {0}".format(lamp.state))

if __name__=='__main__':
    main()