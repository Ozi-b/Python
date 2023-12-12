# There are a few issues with this implementation
# The first issue is that we can create and call the open method. This is an issue because the stream class is an abstract concept
# What does it mean to open a stream? Is a file or a network stream?
# So we shouldnt be able to indirectly create an instance of the stream class.
# We should always subclass it and create an instance of the subclass

from abc import ABC, abstractmethod


class InvalidOperationError(Exception):
    pass


class Stream(ABC):
    def __init__(self):
        self.opened = False

    def open(self):
        if self.opened:
            raise InvalidOperationError("Stream is already opened.")
        self.opened = True

    def close(self):
        if not self.opened:
            raise InvalidOperationError("Stream is already closed.")
        self.opened = False

    @abstractmethod
    def read(self):
        pass


class FileStream(Stream):
    def read(self):
        print("Reading data from a file.")


class NetworkStream(Stream):
    def read(self):
        print("Reading data from a network.")


class MemoryStream(Stream):
    def read(self):
        print("Reading data fromm a memory stream.")


# We want to make this stream class an abstract base class
stream = MemoryStream()
stream.open()
