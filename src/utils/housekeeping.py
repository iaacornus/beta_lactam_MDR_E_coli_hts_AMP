from os import path
from os import mkdir


class HouseKeeping:
    def __init__(self, PATHS_ARR) -> None:
        self.PATHS_ARR = PATHS_ARR

    def create_output_dir(self) -> int:

        for path_ in self.PATHS_ARR:
            if not path.exists(path_):
                mkdir(path_)

        return 1
