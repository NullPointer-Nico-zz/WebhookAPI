from typing import BinaryIO, Union


class File:
    def __init__(self, file: Union[BinaryIO, str], name: str = "") -> None:
        if isinstance(file, str):
            self.file = open(file, "rb")
            self._manuel_open = True
            self.name = name if name else file
        else:
            self.file = file
            self._manuel_open = False
            self.name = name if name else file
        
        self._close = self.file.close
        self.file.close = lambda: None

    def seek(self, offset: int = 0, *args, **kwargs):
        return self.file.seek(offset, *args, **kwargs)

    def close(self, force: bool = False) -> None:
        self.file.close = self._close

        if self._manuel_open or force:
            self.file.close()