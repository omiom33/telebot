"""File generated by TLObjects' generator. All changes will be ERASED"""
from ...tl.tlobject import TLObject
from typing import Optional, List, Union, TYPE_CHECKING
import os
import struct
if TYPE_CHECKING:
    from ...tl.types import TypeBool, TypeUser
    from ...tl.types.auth import TypeSentCodeType, TypeCodeType
    from ...tl.types.help import TypeTermsOfService



class Authorization(TLObject):
    CONSTRUCTOR_ID = 0xcd050916
    SUBCLASS_OF_ID = 0xb9e04e39

    def __init__(self, user, tmp_sessions=None):
        """
        :param TypeUser user:
        :param Optional[int] tmp_sessions:

        Constructor for auth.Authorization: Instance of Authorization.
        """
        self.user = user  # type: TypeUser
        self.tmp_sessions = tmp_sessions  # type: Optional[int]

    def to_dict(self):
        return {
            '_': 'Authorization',
            'user': None if self.user is None else self.user.to_dict(),
            'tmp_sessions': self.tmp_sessions
        }

    def __bytes__(self):
        return b''.join((
            b'\x16\t\x05\xcd',
            struct.pack('<I', (0 if self.tmp_sessions is None or self.tmp_sessions is False else 1)),
            b'' if self.tmp_sessions is None or self.tmp_sessions is False else (struct.pack('<i', self.tmp_sessions)),
            bytes(self.user),
        ))

    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int()

        _tmp_sessions = reader.read_int() if flags & 1 else None
        _user = reader.tgread_object()
        return cls(user=_user, tmp_sessions=_tmp_sessions)


class CheckedPhone(TLObject):
    CONSTRUCTOR_ID = 0x811ea28e
    SUBCLASS_OF_ID = 0x99a3d765

    def __init__(self, phone_registered):
        """
        :param TypeBool phone_registered:

        Constructor for auth.CheckedPhone: Instance of CheckedPhone.
        """
        self.phone_registered = phone_registered  # type: TypeBool

    def to_dict(self):
        return {
            '_': 'CheckedPhone',
            'phone_registered': self.phone_registered
        }

    def __bytes__(self):
        return b''.join((
            b'\x8e\xa2\x1e\x81',
            b'\xb5ur\x99' if self.phone_registered else b'7\x97y\xbc',
        ))

    @classmethod
    def from_reader(cls, reader):
        _phone_registered = reader.tgread_bool()
        return cls(phone_registered=_phone_registered)


class CodeTypeCall(TLObject):
    CONSTRUCTOR_ID = 0x741cd3e3
    SUBCLASS_OF_ID = 0xb3f3e401

    def to_dict(self):
        return {
            '_': 'CodeTypeCall'
        }

    def __bytes__(self):
        return b''.join((
            b'\xe3\xd3\x1ct',
        ))

    @classmethod
    def from_reader(cls, reader):
        return cls()


class CodeTypeFlashCall(TLObject):
    CONSTRUCTOR_ID = 0x226ccefb
    SUBCLASS_OF_ID = 0xb3f3e401

    def to_dict(self):
        return {
            '_': 'CodeTypeFlashCall'
        }

    def __bytes__(self):
        return b''.join((
            b'\xfb\xcel"',
        ))

    @classmethod
    def from_reader(cls, reader):
        return cls()


class CodeTypeSms(TLObject):
    CONSTRUCTOR_ID = 0x72a3158c
    SUBCLASS_OF_ID = 0xb3f3e401

    def to_dict(self):
        return {
            '_': 'CodeTypeSms'
        }

    def __bytes__(self):
        return b''.join((
            b'\x8c\x15\xa3r',
        ))

    @classmethod
    def from_reader(cls, reader):
        return cls()


class ExportedAuthorization(TLObject):
    CONSTRUCTOR_ID = 0xdf969c2d
    SUBCLASS_OF_ID = 0x5fd1ec51

    def __init__(self, id, bytes):
        """
        :param int id:
        :param bytes bytes:

        Constructor for auth.ExportedAuthorization: Instance of ExportedAuthorization.
        """
        self.id = id  # type: int
        self.bytes = bytes  # type: bytes

    def to_dict(self):
        return {
            '_': 'ExportedAuthorization',
            'id': self.id,
            'bytes': self.bytes
        }

    def __bytes__(self):
        return b''.join((
            b'-\x9c\x96\xdf',
            struct.pack('<i', self.id),
            self.serialize_bytes(self.bytes),
        ))

    @classmethod
    def from_reader(cls, reader):
        _id = reader.read_int()
        _bytes = reader.tgread_bytes()
        return cls(id=_id, bytes=_bytes)


class PasswordRecovery(TLObject):
    CONSTRUCTOR_ID = 0x137948a5
    SUBCLASS_OF_ID = 0xfa72d43a

    def __init__(self, email_pattern):
        """
        :param str email_pattern:

        Constructor for auth.PasswordRecovery: Instance of PasswordRecovery.
        """
        self.email_pattern = email_pattern  # type: str

    def to_dict(self):
        return {
            '_': 'PasswordRecovery',
            'email_pattern': self.email_pattern
        }

    def __bytes__(self):
        return b''.join((
            b'\xa5Hy\x13',
            self.serialize_bytes(self.email_pattern),
        ))

    @classmethod
    def from_reader(cls, reader):
        _email_pattern = reader.tgread_string()
        return cls(email_pattern=_email_pattern)


class SentCode(TLObject):
    CONSTRUCTOR_ID = 0x38faab5f
    SUBCLASS_OF_ID = 0x6ce87081

    def __init__(self, type, phone_code_hash, phone_registered=None, next_type=None, timeout=None, terms_of_service=None):
        """
        :param TypeSentCodeType type:
        :param str phone_code_hash:
        :param Optional[bool] phone_registered:
        :param Optional[TypeCodeType] next_type:
        :param Optional[int] timeout:
        :param Optional[TypeTermsOfService] terms_of_service:

        Constructor for auth.SentCode: Instance of SentCode.
        """
        self.type = type  # type: TypeSentCodeType
        self.phone_code_hash = phone_code_hash  # type: str
        self.phone_registered = phone_registered  # type: Optional[bool]
        self.next_type = next_type  # type: Optional[TypeCodeType]
        self.timeout = timeout  # type: Optional[int]
        self.terms_of_service = terms_of_service  # type: Optional[TypeTermsOfService]

    def to_dict(self):
        return {
            '_': 'SentCode',
            'type': None if self.type is None else self.type.to_dict(),
            'phone_code_hash': self.phone_code_hash,
            'phone_registered': self.phone_registered,
            'next_type': None if self.next_type is None else self.next_type.to_dict(),
            'timeout': self.timeout,
            'terms_of_service': None if self.terms_of_service is None else self.terms_of_service.to_dict()
        }

    def __bytes__(self):
        return b''.join((
            b'_\xab\xfa8',
            struct.pack('<I', (0 if self.phone_registered is None or self.phone_registered is False else 1) | (0 if self.next_type is None or self.next_type is False else 2) | (0 if self.timeout is None or self.timeout is False else 4) | (0 if self.terms_of_service is None or self.terms_of_service is False else 8)),
            bytes(self.type),
            self.serialize_bytes(self.phone_code_hash),
            b'' if self.next_type is None or self.next_type is False else (bytes(self.next_type)),
            b'' if self.timeout is None or self.timeout is False else (struct.pack('<i', self.timeout)),
            b'' if self.terms_of_service is None or self.terms_of_service is False else (bytes(self.terms_of_service)),
        ))

    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int()

        _phone_registered = bool(flags & 1)
        _type = reader.tgread_object()
        _phone_code_hash = reader.tgread_string()
        _next_type = reader.tgread_object() if flags & 2 else None
        _timeout = reader.read_int() if flags & 4 else None
        _terms_of_service = reader.tgread_object() if flags & 8 else None
        return cls(type=_type, phone_code_hash=_phone_code_hash, phone_registered=_phone_registered, next_type=_next_type, timeout=_timeout, terms_of_service=_terms_of_service)


class SentCodeTypeApp(TLObject):
    CONSTRUCTOR_ID = 0x3dbb5986
    SUBCLASS_OF_ID = 0xff5b158e

    def __init__(self, length):
        """
        :param int length:

        Constructor for auth.SentCodeType: Instance of either SentCodeTypeApp, SentCodeTypeSms, SentCodeTypeCall, SentCodeTypeFlashCall.
        """
        self.length = length  # type: int

    def to_dict(self):
        return {
            '_': 'SentCodeTypeApp',
            'length': self.length
        }

    def __bytes__(self):
        return b''.join((
            b'\x86Y\xbb=',
            struct.pack('<i', self.length),
        ))

    @classmethod
    def from_reader(cls, reader):
        _length = reader.read_int()
        return cls(length=_length)


class SentCodeTypeCall(TLObject):
    CONSTRUCTOR_ID = 0x5353e5a7
    SUBCLASS_OF_ID = 0xff5b158e

    def __init__(self, length):
        """
        :param int length:

        Constructor for auth.SentCodeType: Instance of either SentCodeTypeApp, SentCodeTypeSms, SentCodeTypeCall, SentCodeTypeFlashCall.
        """
        self.length = length  # type: int

    def to_dict(self):
        return {
            '_': 'SentCodeTypeCall',
            'length': self.length
        }

    def __bytes__(self):
        return b''.join((
            b'\xa7\xe5SS',
            struct.pack('<i', self.length),
        ))

    @classmethod
    def from_reader(cls, reader):
        _length = reader.read_int()
        return cls(length=_length)


class SentCodeTypeFlashCall(TLObject):
    CONSTRUCTOR_ID = 0xab03c6d9
    SUBCLASS_OF_ID = 0xff5b158e

    def __init__(self, pattern):
        """
        :param str pattern:

        Constructor for auth.SentCodeType: Instance of either SentCodeTypeApp, SentCodeTypeSms, SentCodeTypeCall, SentCodeTypeFlashCall.
        """
        self.pattern = pattern  # type: str

    def to_dict(self):
        return {
            '_': 'SentCodeTypeFlashCall',
            'pattern': self.pattern
        }

    def __bytes__(self):
        return b''.join((
            b'\xd9\xc6\x03\xab',
            self.serialize_bytes(self.pattern),
        ))

    @classmethod
    def from_reader(cls, reader):
        _pattern = reader.tgread_string()
        return cls(pattern=_pattern)


class SentCodeTypeSms(TLObject):
    CONSTRUCTOR_ID = 0xc000bba2
    SUBCLASS_OF_ID = 0xff5b158e

    def __init__(self, length):
        """
        :param int length:

        Constructor for auth.SentCodeType: Instance of either SentCodeTypeApp, SentCodeTypeSms, SentCodeTypeCall, SentCodeTypeFlashCall.
        """
        self.length = length  # type: int

    def to_dict(self):
        return {
            '_': 'SentCodeTypeSms',
            'length': self.length
        }

    def __bytes__(self):
        return b''.join((
            b'\xa2\xbb\x00\xc0',
            struct.pack('<i', self.length),
        ))

    @classmethod
    def from_reader(cls, reader):
        _length = reader.read_int()
        return cls(length=_length)

