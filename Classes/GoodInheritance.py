# Imagine you want to model the concept of a stream of data
# You can read a stream of data from a file, a network, or from memory
# All these streams have a few things in common
# you can open them, close them, read them and so on
# but how we read data from a stream is dependent upon the type of stream
# reading data from a file compared to a network is different for example


class InvalidOperationError(Exception):
    pass


class Stream:
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

# In this example, FileStream and NetworkStream both share the same parent of stream
# this means that they both share the same methods of opening and closing a file
# but reading a file and reading a network is different so they have their own read method


class FileStream(Stream):
    def read(self):
        print("Reading data from a file.")


class NetworkStream(Stream):
    def read(self):
        print("Reading data from a network.")
