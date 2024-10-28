from bowling_error import BowlingError
from frame import Frame


class BowlingGame:

    def __init__(self):
        self._frames = []
    
    def add_frame(self, frame: Frame) -> None:
        if len(self._frames) > 9:
            raise BowlingError()
        self._frames.append(frame)

    def get_frame_at(self, i: int) -> Frame:
        try:
            return self._frames[i]
        except IndexError:
            raise BowlingError

    def calculate_score(self) -> int:
        score= 0
        for i, frame in enumerate(self._frames):
            if i >= 1 and self._frames[i - 1].is_spare():
                score += frame.get_first_throw()
            score += frame.score()

        return score

    def set_first_bonus_throw(self, bonus_throw: int) -> None:
        pass

    def set_second_bonus_throw(self, bonus_throw: int) -> None:
        pass
