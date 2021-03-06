# Automatically generated by pb2py
# fmt: off
from .. import protobuf as p


class CardanoTxRequest(p.MessageType):
    MESSAGE_WIRE_TYPE = 304

    def __init__(
        self,
        tx_index: int = None,
        tx_hash: bytes = None,
        tx_body: bytes = None,
    ) -> None:
        self.tx_index = tx_index
        self.tx_hash = tx_hash
        self.tx_body = tx_body

    @classmethod
    def get_fields(cls):
        return {
            1: ('tx_index', p.UVarintType, 0),
            2: ('tx_hash', p.BytesType, 0),
            3: ('tx_body', p.BytesType, 0),
        }
