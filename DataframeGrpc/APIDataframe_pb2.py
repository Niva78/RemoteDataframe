# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: APIDataframe.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12\x41PIDataframe.proto\"\x18\n\x06Result\x12\x0e\n\x06result\x18\x01 \x01(\t2D\n\x0c\x41PIDataframe\x12\x19\n\x03Min\x12\x07.Result\x1a\x07.Result\"\x00\x12\x19\n\x03Max\x12\x07.Result\x1a\x07.Result\"\x00\x62\x06proto3')



_RESULT = DESCRIPTOR.message_types_by_name['Result']
Result = _reflection.GeneratedProtocolMessageType('Result', (_message.Message,), {
  'DESCRIPTOR' : _RESULT,
  '__module__' : 'APIDataframe_pb2'
  # @@protoc_insertion_point(class_scope:Result)
  })
_sym_db.RegisterMessage(Result)

_APIDATAFRAME = DESCRIPTOR.services_by_name['APIDataframe']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _RESULT._serialized_start=22
  _RESULT._serialized_end=46
  _APIDATAFRAME._serialized_start=48
  _APIDATAFRAME._serialized_end=116
# @@protoc_insertion_point(module_scope)
