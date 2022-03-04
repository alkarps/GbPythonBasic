from time import sleep


class TrafficLight:
    __states = (("RED", 7, 1), ("YELLOW", 2, 2), ("GREEN", 5, 0))

    def __init__(self):
        self.__current_state = 0

    def running(self):
        current_time = 0
        while True:
            current_time += 1
            current_state = self.__states[self.__current_state]
            print(current_state[0])
            if current_time == current_state[1]:
                current_time = 0
                self.__current_state = current_state[2]
            sleep(1)


TrafficLight().running()