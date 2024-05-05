from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class File(_message.Message):
    __slots__ = ("filename", "content")
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    filename: str
    content: bytes
    def __init__(self, filename: _Optional[str] = ..., content: _Optional[bytes] = ...) -> None: ...

class WordCountResponse(_message.Message):
    __slots__ = ("word_counts",)
    WORD_COUNTS_FIELD_NUMBER: _ClassVar[int]
    word_counts: _containers.RepeatedCompositeFieldContainer[WordCount]
    def __init__(self, word_counts: _Optional[_Iterable[_Union[WordCount, _Mapping]]] = ...) -> None: ...

class WordCount(_message.Message):
    __slots__ = ("word", "count")
    WORD_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    word: str
    count: int
    def __init__(self, word: _Optional[str] = ..., count: _Optional[int] = ...) -> None: ...

class FileChunk(_message.Message):
    __slots__ = ("data",)
    DATA_FIELD_NUMBER: _ClassVar[int]
    data: bytes
    def __init__(self, data: _Optional[bytes] = ...) -> None: ...

class UploadStatus(_message.Message):
    __slots__ = ("success",)
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    success: bool
    def __init__(self, success: bool = ...) -> None: ...
