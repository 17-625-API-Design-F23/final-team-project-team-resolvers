from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Change(_message.Message):
    __slots__ = ["file_path", "change_type", "change_content"]
    FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    CHANGE_TYPE_FIELD_NUMBER: _ClassVar[int]
    CHANGE_CONTENT_FIELD_NUMBER: _ClassVar[int]
    file_path: str
    change_type: str
    change_content: str
    def __init__(self, file_path: _Optional[str] = ..., change_type: _Optional[str] = ..., change_content: _Optional[str] = ...) -> None: ...

class PRDescriptionRequest(_message.Message):
    __slots__ = ["repository_url", "source_branch", "committed_changes"]
    REPOSITORY_URL_FIELD_NUMBER: _ClassVar[int]
    SOURCE_BRANCH_FIELD_NUMBER: _ClassVar[int]
    COMMITTED_CHANGES_FIELD_NUMBER: _ClassVar[int]
    repository_url: str
    source_branch: str
    committed_changes: _containers.RepeatedCompositeFieldContainer[Change]
    def __init__(self, repository_url: _Optional[str] = ..., source_branch: _Optional[str] = ..., committed_changes: _Optional[_Iterable[_Union[Change, _Mapping]]] = ...) -> None: ...

class PRDescriptionResponse(_message.Message):
    __slots__ = ["PR_description"]
    PR_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    PR_description: str
    def __init__(self, PR_description: _Optional[str] = ...) -> None: ...

class SmartAutoCompleteRequest(_message.Message):
    __slots__ = ["repository_url", "branch_name", "committed_changes", "uncommitted_changes", "recent_edits", "code_context"]
    class CodeContext(_message.Message):
        __slots__ = ["current_line", "previous_lines", "next_lines"]
        CURRENT_LINE_FIELD_NUMBER: _ClassVar[int]
        PREVIOUS_LINES_FIELD_NUMBER: _ClassVar[int]
        NEXT_LINES_FIELD_NUMBER: _ClassVar[int]
        current_line: str
        previous_lines: str
        next_lines: str
        def __init__(self, current_line: _Optional[str] = ..., previous_lines: _Optional[str] = ..., next_lines: _Optional[str] = ...) -> None: ...
    REPOSITORY_URL_FIELD_NUMBER: _ClassVar[int]
    BRANCH_NAME_FIELD_NUMBER: _ClassVar[int]
    COMMITTED_CHANGES_FIELD_NUMBER: _ClassVar[int]
    UNCOMMITTED_CHANGES_FIELD_NUMBER: _ClassVar[int]
    RECENT_EDITS_FIELD_NUMBER: _ClassVar[int]
    CODE_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    repository_url: str
    branch_name: str
    committed_changes: _containers.RepeatedCompositeFieldContainer[Change]
    uncommitted_changes: _containers.RepeatedCompositeFieldContainer[Change]
    recent_edits: str
    code_context: SmartAutoCompleteRequest.CodeContext
    def __init__(self, repository_url: _Optional[str] = ..., branch_name: _Optional[str] = ..., committed_changes: _Optional[_Iterable[_Union[Change, _Mapping]]] = ..., uncommitted_changes: _Optional[_Iterable[_Union[Change, _Mapping]]] = ..., recent_edits: _Optional[str] = ..., code_context: _Optional[_Union[SmartAutoCompleteRequest.CodeContext, _Mapping]] = ...) -> None: ...

class SmartAutoCompleteResponse(_message.Message):
    __slots__ = ["completion_code"]
    COMPLETION_CODE_FIELD_NUMBER: _ClassVar[int]
    completion_code: str
    def __init__(self, completion_code: _Optional[str] = ...) -> None: ...

class ChatGPT4CodeRequest(_message.Message):
    __slots__ = ["repository_url", "branch_name", "committed_changes", "uncommitted_changes", "text_description"]
    REPOSITORY_URL_FIELD_NUMBER: _ClassVar[int]
    BRANCH_NAME_FIELD_NUMBER: _ClassVar[int]
    COMMITTED_CHANGES_FIELD_NUMBER: _ClassVar[int]
    UNCOMMITTED_CHANGES_FIELD_NUMBER: _ClassVar[int]
    TEXT_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    repository_url: str
    branch_name: str
    committed_changes: _containers.RepeatedCompositeFieldContainer[Change]
    uncommitted_changes: _containers.RepeatedCompositeFieldContainer[Change]
    text_description: str
    def __init__(self, repository_url: _Optional[str] = ..., branch_name: _Optional[str] = ..., committed_changes: _Optional[_Iterable[_Union[Change, _Mapping]]] = ..., uncommitted_changes: _Optional[_Iterable[_Union[Change, _Mapping]]] = ..., text_description: _Optional[str] = ...) -> None: ...

class ChatGPT4CodeResponse(_message.Message):
    __slots__ = ["gpt_response"]
    GPT_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    gpt_response: str
    def __init__(self, gpt_response: _Optional[str] = ...) -> None: ...

class VirtualPairProgrammingRequest(_message.Message):
    __slots__ = ["repository_url", "branch_name", "uncommitted_changes", "text_description"]
    REPOSITORY_URL_FIELD_NUMBER: _ClassVar[int]
    BRANCH_NAME_FIELD_NUMBER: _ClassVar[int]
    UNCOMMITTED_CHANGES_FIELD_NUMBER: _ClassVar[int]
    TEXT_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    repository_url: str
    branch_name: str
    uncommitted_changes: _containers.RepeatedCompositeFieldContainer[Change]
    text_description: str
    def __init__(self, repository_url: _Optional[str] = ..., branch_name: _Optional[str] = ..., uncommitted_changes: _Optional[_Iterable[_Union[Change, _Mapping]]] = ..., text_description: _Optional[str] = ...) -> None: ...

class VirtualPairProgrammingResponse(_message.Message):
    __slots__ = ["code_pointer"]
    class CodePointer(_message.Message):
        __slots__ = ["delta_code", "text_description"]
        DELTA_CODE_FIELD_NUMBER: _ClassVar[int]
        TEXT_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        delta_code: Change
        text_description: str
        def __init__(self, delta_code: _Optional[_Union[Change, _Mapping]] = ..., text_description: _Optional[str] = ...) -> None: ...
    CODE_POINTER_FIELD_NUMBER: _ClassVar[int]
    code_pointer: _containers.RepeatedCompositeFieldContainer[VirtualPairProgrammingResponse.CodePointer]
    def __init__(self, code_pointer: _Optional[_Iterable[_Union[VirtualPairProgrammingResponse.CodePointer, _Mapping]]] = ...) -> None: ...
