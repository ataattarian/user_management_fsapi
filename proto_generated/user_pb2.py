# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: user.proto
# Protobuf Python Version: 5.27.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    27,
    2,
    '',
    'user.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\nuser.proto\x12\x04user\"\x19\n\x0bUserRequest\x12\n\n\x02id\x18\x01 \x01(\x05\"`\n\x13RegisterUserRequest\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x12\n\nfirst_name\x18\x02 \x01(\t\x12\x11\n\tlast_name\x18\x03 \x01(\t\x12\x10\n\x08password\x18\x04 \x01(\t\"j\n\x11UpdateUserRequest\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x10\n\x08username\x18\x02 \x01(\t\x12\x12\n\nfirst_name\x18\x03 \x01(\t\x12\x11\n\tlast_name\x18\x04 \x01(\t\x12\x10\n\x08password\x18\x05 \x01(\t\"\x1f\n\x11\x44\x65leteUserRequest\x12\n\n\x02id\x18\x01 \x01(\x05\"%\n\x12\x44\x65leteUserResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\"S\n\x0cUserResponse\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x10\n\x08username\x18\x02 \x01(\t\x12\x12\n\nfirst_name\x18\x03 \x01(\t\x12\x11\n\tlast_name\x18\x04 \x01(\t\"5\n\x10UserListResponse\x12!\n\x05users\x18\x01 \x03(\x0b\x32\x12.user.UserResponse\"\x0e\n\x0c\x45mptyRequest2\xb2\x02\n\x0bUserService\x12\x30\n\x07GetUser\x12\x11.user.UserRequest\x1a\x12.user.UserResponse\x12\x36\n\x08GetUsers\x12\x12.user.EmptyRequest\x1a\x16.user.UserListResponse\x12\x39\n\nUpdateUser\x12\x17.user.UpdateUserRequest\x1a\x12.user.UserResponse\x12?\n\nDeleteUser\x12\x17.user.DeleteUserRequest\x1a\x18.user.DeleteUserResponse\x12=\n\x0cRegisterUser\x12\x19.user.RegisterUserRequest\x1a\x12.user.UserResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'user_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_USERREQUEST']._serialized_start=20
  _globals['_USERREQUEST']._serialized_end=45
  _globals['_REGISTERUSERREQUEST']._serialized_start=47
  _globals['_REGISTERUSERREQUEST']._serialized_end=143
  _globals['_UPDATEUSERREQUEST']._serialized_start=145
  _globals['_UPDATEUSERREQUEST']._serialized_end=251
  _globals['_DELETEUSERREQUEST']._serialized_start=253
  _globals['_DELETEUSERREQUEST']._serialized_end=284
  _globals['_DELETEUSERRESPONSE']._serialized_start=286
  _globals['_DELETEUSERRESPONSE']._serialized_end=323
  _globals['_USERRESPONSE']._serialized_start=325
  _globals['_USERRESPONSE']._serialized_end=408
  _globals['_USERLISTRESPONSE']._serialized_start=410
  _globals['_USERLISTRESPONSE']._serialized_end=463
  _globals['_EMPTYREQUEST']._serialized_start=465
  _globals['_EMPTYREQUEST']._serialized_end=479
  _globals['_USERSERVICE']._serialized_start=482
  _globals['_USERSERVICE']._serialized_end=788
# @@protoc_insertion_point(module_scope)