from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class PRDescriptionRequest(_message.Message):
    __slots__ = ["repository_url", "branch_name", "committed_code"]
    REPOSITORY_URL_FIELD_NUMBER: _ClassVar[int]
    BRANCH_NAME_FIELD_NUMBER: _ClassVar[int]
    COMMITTED_CODE_FIELD_NUMBER: _ClassVar[int]
    repository_url: str
    branch_name: str
    committed_code: str
    def __init__(self, repository_url: _Optional[str] = ..., branch_name: _Optional[str] = ..., committed_code: _Optional[str] = ...) -> None: ...

class PRDescriptionResponse(_message.Message):
    __slots__ = ["PR_description"]
    PR_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    PR_description: str
    def __init__(self, PR_description: _Optional[str] = ...) -> None: ...

class SmartAutoCompleteRequest(_message.Message):
    __slots__ = ["repository_url", "branch_name", "current_file", "committed_code", "uncommitted_code", "recent_edits", "cursor_position"]
    REPOSITORY_URL_FIELD_NUMBER: _ClassVar[int]
    BRANCH_NAME_FIELD_NUMBER: _ClassVar[int]
    CURRENT_FILE_FIELD_NUMBER: _ClassVar[int]
    COMMITTED_CODE_FIELD_NUMBER: _ClassVar[int]
    UNCOMMITTED_CODE_FIELD_NUMBER: _ClassVar[int]
    RECENT_EDITS_FIELD_NUMBER: _ClassVar[int]
    CURSOR_POSITION_FIELD_NUMBER: _ClassVar[int]
    repository_url: str
    branch_name: str
    current_file: str
    committed_code: str
    uncommitted_code: str
    recent_edits: str
    cursor_position: str
    def __init__(self, repository_url: _Optional[str] = ..., branch_name: _Optional[str] = ..., current_file: _Optional[str] = ..., committed_code: _Optional[str] = ..., uncommitted_code: _Optional[str] = ..., recent_edits: _Optional[str] = ..., cursor_position: _Optional[str] = ...) -> None: ...

class SmartAutoCompleteResponse(_message.Message):
    __slots__ = ["completion_code"]
    COMPLETION_CODE_FIELD_NUMBER: _ClassVar[int]
    completion_code: str
    def __init__(self, completion_code: _Optional[str] = ...) -> None: ...

class ChatGPT4CodeRequest(_message.Message):
    __slots__ = ["repository_url", "branch_name", "current_file", "committed_code", "uncommitted_code", "text_description"]
    REPOSITORY_URL_FIELD_NUMBER: _ClassVar[int]
    BRANCH_NAME_FIELD_NUMBER: _ClassVar[int]
    CURRENT_FILE_FIELD_NUMBER: _ClassVar[int]
    COMMITTED_CODE_FIELD_NUMBER: _ClassVar[int]
    UNCOMMITTED_CODE_FIELD_NUMBER: _ClassVar[int]
    TEXT_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    repository_url: str
    branch_name: str
    current_file: str
    committed_code: str
    uncommitted_code: str
    text_description: str
    def __init__(self, repository_url: _Optional[str] = ..., branch_name: _Optional[str] = ..., current_file: _Optional[str] = ..., committed_code: _Optional[str] = ..., uncommitted_code: _Optional[str] = ..., text_description: _Optional[str] = ...) -> None: ...

class ChatGPT4CodeResponse(_message.Message):
    __slots__ = ["needs_more_info", "code"]
    NEEDS_MORE_INFO_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    needs_more_info: bool
    code: str
    def __init__(self, needs_more_info: bool = ..., code: _Optional[str] = ...) -> None: ...

class VirtualPairProgrammingRequest(_message.Message):
    __slots__ = ["repository_url", "branch_name", "current_file", "committed_code", "uncommitted_code", "stack_trace", "text_description"]
    REPOSITORY_URL_FIELD_NUMBER: _ClassVar[int]
    BRANCH_NAME_FIELD_NUMBER: _ClassVar[int]
    CURRENT_FILE_FIELD_NUMBER: _ClassVar[int]
    COMMITTED_CODE_FIELD_NUMBER: _ClassVar[int]
    UNCOMMITTED_CODE_FIELD_NUMBER: _ClassVar[int]
    STACK_TRACE_FIELD_NUMBER: _ClassVar[int]
    TEXT_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    repository_url: str
    branch_name: str
    current_file: str
    committed_code: str
    uncommitted_code: str
    stack_trace: str
    text_description: str
    def __init__(self, repository_url: _Optional[str] = ..., branch_name: _Optional[str] = ..., current_file: _Optional[str] = ..., committed_code: _Optional[str] = ..., uncommitted_code: _Optional[str] = ..., stack_trace: _Optional[str] = ..., text_description: _Optional[str] = ...) -> None: ...

class VirtualPairProgrammingResponse(_message.Message):
    __slots__ = ["code_pointer", "proposed_supplement", "text_description"]
    CODE_POINTER_FIELD_NUMBER: _ClassVar[int]
    PROPOSED_SUPPLEMENT_FIELD_NUMBER: _ClassVar[int]
    TEXT_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    code_pointer: str
    proposed_supplement: str
    text_description: str
    def __init__(self, code_pointer: _Optional[str] = ..., proposed_supplement: _Optional[str] = ..., text_description: _Optional[str] = ...) -> None: ...
