import abc
import struct
from datetime import datetime, date, timedelta


class TLObject:
    CONSTRUCTOR_ID = None
    SUBCLASS_OF_ID = None

    @staticmethod
    def pretty_format(obj, indent=None):
        """
        Pretty formats the given object as a string which is returned.
        If indent is None, a single line will be returned.
        """
        if isinstance(obj, TLObject):
            obj = obj.to_dict()

        if indent is None:
            if isinstance(obj, dict):
                return '{}({})'.format(
                    obj.get('_', 'dict'),
                    ', '.join(
                        f'{k}={TLObject.pretty_format(v)}'
                        for k, v in obj.items()
                        if k != '_'
                    ),
                )

            elif isinstance(obj, (str, bytes)) or not hasattr(obj, '__iter__'):
                return repr(obj)
            else:
                return f"[{', '.join(TLObject.pretty_format(x) for x in obj)}]"
        else:
            result = []
            if isinstance(obj, dict):
                result.extend((obj.get('_', 'dict'), '('))
                if obj:
                    result.append('\n')
                    indent += 1
                    for k, v in obj.items():
                        if k == '_':
                            continue
                        result.extend(
                            (
                                '\t' * indent,
                                k,
                                '=',
                                TLObject.pretty_format(v, indent),
                                ',\n',
                            )
                        )

                    result.pop()  # last ',\n'
                    indent -= 1
                    result.extend(('\n', '\t' * indent))
                result.append(')')

            elif isinstance(obj, (str, bytes)) or not hasattr(obj, '__iter__'):
                result.append(repr(obj))

            else:
                result.append('[\n')
                indent += 1
                for x in obj:
                    result.extend(('\t' * indent, TLObject.pretty_format(x, indent), ',\n'))
                indent -= 1
                result.extend(('\t' * indent, ']'))
            return ''.join(result)

    @staticmethod
    def serialize_bytes(data):
        """Write bytes by using Telegram guidelines"""
        if not isinstance(data, bytes):
            if isinstance(data, str):
                data = data.encode('utf-8')
            else:
                raise TypeError(f'bytes or str expected, not {type(data)}')

        r = []
        if len(data) < 254:
            padding = (len(data) + 1) % 4
            if padding != 0:
                padding = 4 - padding

            r.append(bytes([len(data)]))
        else:
            padding = len(data) % 4
            if padding != 0:
                padding = 4 - padding

            r.append(bytes([
                254,
                len(data) % 256,
                (len(data) >> 8) % 256,
                (len(data) >> 16) % 256
            ]))
        r.extend((data, bytes(padding)))
        return b''.join(r)

    @staticmethod
    def serialize_datetime(dt):
        if not dt:
            return b'\0\0\0\0'

        if isinstance(dt, datetime):
            dt = int(dt.timestamp())
        elif isinstance(dt, date):
            dt = int(datetime(dt.year, dt.month, dt.day).timestamp())
        elif isinstance(dt, float):
            dt = int(dt)
        elif isinstance(dt, timedelta):
            # Timezones are tricky. datetime.now() + ... timestamp() works
            dt = int((datetime.now() + dt).timestamp())

        if isinstance(dt, int):
            return struct.pack('<I', dt)

        raise TypeError(f'Cannot interpret "{dt}" as a date.')

    def __eq__(self, o):
        return isinstance(o, type(self)) and self.to_dict() == o.to_dict()

    def __ne__(self, o):
        return not isinstance(o, type(self)) or self.to_dict() != o.to_dict()

    def __str__(self):
        return TLObject.pretty_format(self)

    def stringify(self):
        return TLObject.pretty_format(self, indent=0)

    def to_dict(self):
        raise NotImplementedError

    def __bytes__(self):
        raise NotImplementedError

    @classmethod
    def from_reader(cls, reader):
        raise NotImplementedError


class TLRequest(TLObject):
    """
    Represents a content-related `TLObject` (a request that can be sent).
    """
    @staticmethod
    def read_result(reader):
        return reader.tgread_object()

    async def resolve(self, client, utils):
        pass
