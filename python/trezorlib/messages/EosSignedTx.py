# Automatically generated by pb2py
# fmt: off
from .. import protobuf as p


class EosSignedTx(p.MessageType):
    MESSAGE_WIRE_TYPE = 605

    def __init__(
        self,
        signature: str = None,
    ) -> None:
        self.signature = signature

    @classmethod
    def get_fields(cls):
        return {
            1: ('signature', p.UnicodeType, 0),
        }
