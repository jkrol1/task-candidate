from codec.csv import TextFileCodec
from storage.local import LocalStorageReader

if __name__ == '__main__':
    codec = TextFileCodec()
    reader = LocalStorageReader(TextFileCodec())
    data = reader.read("check.csv")
