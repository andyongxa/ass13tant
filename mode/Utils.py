import json
import prettytable as pt


# 阿里云sdk返回body 转json
def res2json(response):
    _tmp = response.body.__str__().replace('\'', '"').replace('False', 'false').replace('True', 'true')
    return json.loads(_tmp)


# jsonlist转pt表格
def getTb(jsonlist, keys):
    table = pt.PrettyTable(keys)
    for _ in jsonlist:
        table.add_row([_[j] for j in keys])
    # json list转打印表格
    return table


def saveRecord(path, data):
    with open(path, 'a') as f:
        f.writelines(data+'\n')


def getRecord(path):
    with open(path, 'r') as f:
        data = f.readlines()
    codeDict = {}
    for i in data:
        codeDict[i.split('\n')[0].split(',')[0]] = i.split('\n')[0].split(',')[1]
    return codeDict


# 目前未用到
# class Message:
#     def __init__(self, Payload: bytes = b'', MessageType: int = 0, SchemaVersion: str = "1.01", SessionId: str = "",
#                  SequenceNumber: int = 0, CreatedDate=int(time.time() * 1000) & 0xFFFFFFFFFFFFFFFF):
#         self.MessageType = MessageType
#         self.SchemaVersion = SchemaVersion
#         self.SessionId = SessionId
#         self.CreatedDate = CreatedDate
#         self.SequenceNumber = SequenceNumber
#         self.Payload = Payload
#         self.PayloadLength = self.Payload.__len__()
#
#     def deserialize(self, input_bytes):
#         try:
#             self.MessageType = struct.unpack_from('<I', input_bytes, 0)[0]
#             # string
#             self.SchemaVersion = input_bytes[4:8].decode('utf-8').strip('\x00')
#             # string
#             self.SessionId = input_bytes[8:40].decode('utf-8').strip('\x00')
#             self.CreatedDate = struct.unpack_from('<Q', input_bytes, 40)[0]
#             self.SequenceNumber = struct.unpack_from('<q', input_bytes, 48)[0]
#             self.PayloadLength = struct.unpack_from('<I', input_bytes, 56)[0]
#             # []byte
#             self.Payload = input_bytes[60:]
#         except Exception as e:
#             print(f"Could not deserialize: {e}")
#
#     def serialize(self):
#         try:
#             result = bytearray()
#             result += struct.pack('<I', self.MessageType)
#             result += self.SchemaVersion.ljust(4, '\x00').encode('utf-8')
#             result += self.SessionId.ljust(32, '\x00').encode('utf-8')
#             result += struct.pack('<Q', self.CreatedDate)
#             result += struct.pack('<q', self.SequenceNumber)
#             result += struct.pack('<I', len(self.Payload))
#             result += self.Payload
#             return result
#         except Exception as e:
#             print(f"Could not serialize: {e}")
#             return None
#
#     def __str__(self):
#         return f"MessageType: {self.MessageType}, SchemaVersion: {self.SchemaVersion}, SessionId: {self.SessionId}, CreatedDate: {self.CreatedDate}, SequenceNumber: {self.SequenceNumber}, PayloadLength: {self.PayloadLength}, Payload: {self.Payload}"
#

