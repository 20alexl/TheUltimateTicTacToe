#level_manager/level.py
class LevelManager:
    def __init__(self, stage = 3, initial_level=1, max_level = 3, min_level = 1):
        # Ensure the initial level is within the allowed range
        self._stage = stage
        self._max_level = max_level
        self._min_level = min_level
        self._level = initial_level

    @property
    def level(self):
        return self._level
    
    @property
    def stage(self):
        return self._stage

    @level.setter
    def set_level(self, value):
        # Ensure the value is within the allowed range
        if  self._min_level <= value <= self._max_level:
            self._level = value
        else:
            raise ValueError(f"Level must be between {self._min_level} and {self._max_level}.")

    @stage.setter
    def set_stage(self, value):
        # Set Stage above 3
        if  value >= 3:
            self._stage = value
        else:
            raise ValueError(f"Stage must be more than 3.")

    def advance(self):
        # Increase for baord size
        if self._level == self._stage:
            self._stage += 1
            self._max_level += 1
            self.set_level = 1
        else:
            self.increment()

    def increment(self):
        # Increment level if it's less than the maximum allowed value
        if self._level < self._max_level:
            self._level += 1
        else:
            print(f"Level is already at the maximum value of {self._max_level}.")

    def decrement(self):
        # Decrement level if it's greater than the minimum allowed value
        if self._level > self._min_level:
            self._level -= 1
        else:
            print(f"Level is already at the minimum value of {self._min_level}.")