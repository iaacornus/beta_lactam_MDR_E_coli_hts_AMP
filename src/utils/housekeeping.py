from os import path
from os import mkdir


class HouseKeeping:
    def __init__(self, PATHS_ARR) -> None:
        self.PATHS_ARR = PATHS_ARR

    def create_output_dir(self, path_) -> int:
        if path_ in self.PATHS_ARR and path.exists(path_):
            return 1

        self.PATHS_ARR.append(path_)

        if not path.exists(path_): # double checking
            mkdir(path_)

        return 0
