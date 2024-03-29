# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: demo.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='demo.proto',
  package='demo',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\ndemo.proto\x12\x04\x64\x65mo\"-\n\x07Request\x12\"\n\x0crequest_data\x18\x01 \x01(\x0b\x32\x0c.demo.Person\"\"\n\nStrRequest\x12\x14\n\x0crequest_data\x18\x01 \x01(\t\"4\n\x08Response\x12(\n\rresponse_data\x18\x01 \x01(\x0b\x32\x11.demo.AddressBook\"$\n\x0bStrResponse\x12\x15\n\rresponse_data\x18\x01 \x01(\t\"1\n\x06Person\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\x05\x12\r\n\x05\x65mail\x18\x03 \x01(\t\"+\n\x0b\x41\x64\x64ressBook\x12\x1c\n\x06people\x18\x01 \x03(\x0b\x32\x0c.demo.Person2u\n\x08GRPCDemo\x12\x33\n\x0fSimpleGetMethod\x12\x10.demo.StrRequest\x1a\x0e.demo.Response\x12\x34\n\x10SimplePostMethod\x12\r.demo.Request\x1a\x11.demo.StrResponseb\x06proto3')
)




_REQUEST = _descriptor.Descriptor(
  name='Request',
  full_name='demo.Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='request_data', full_name='demo.Request.request_data', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=20,
  serialized_end=65,
)


_STRREQUEST = _descriptor.Descriptor(
  name='StrRequest',
  full_name='demo.StrRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='request_data', full_name='demo.StrRequest.request_data', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=67,
  serialized_end=101,
)


_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='demo.Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='response_data', full_name='demo.Response.response_data', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=103,
  serialized_end=155,
)


_STRRESPONSE = _descriptor.Descriptor(
  name='StrResponse',
  full_name='demo.StrResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='response_data', full_name='demo.StrResponse.response_data', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=157,
  serialized_end=193,
)


_PERSON = _descriptor.Descriptor(
  name='Person',
  full_name='demo.Person',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='demo.Person.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id', full_name='demo.Person.id', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='email', full_name='demo.Person.email', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=195,
  serialized_end=244,
)


_ADDRESSBOOK = _descriptor.Descriptor(
  name='AddressBook',
  full_name='demo.AddressBook',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='people', full_name='demo.AddressBook.people', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=246,
  serialized_end=289,
)

_REQUEST.fields_by_name['request_data'].message_type = _PERSON
_RESPONSE.fields_by_name['response_data'].message_type = _ADDRESSBOOK
_ADDRESSBOOK.fields_by_name['people'].message_type = _PERSON
DESCRIPTOR.message_types_by_name['Request'] = _REQUEST
DESCRIPTOR.message_types_by_name['StrRequest'] = _STRREQUEST
DESCRIPTOR.message_types_by_name['Response'] = _RESPONSE
DESCRIPTOR.message_types_by_name['StrResponse'] = _STRRESPONSE
DESCRIPTOR.message_types_by_name['Person'] = _PERSON
DESCRIPTOR.message_types_by_name['AddressBook'] = _ADDRESSBOOK
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Request = _reflection.GeneratedProtocolMessageType('Request', (_message.Message,), {
  'DESCRIPTOR' : _REQUEST,
  '__module__' : 'demo_pb2'
  # @@protoc_insertion_point(class_scope:demo.Request)
  })
_sym_db.RegisterMessage(Request)

StrRequest = _reflection.GeneratedProtocolMessageType('StrRequest', (_message.Message,), {
  'DESCRIPTOR' : _STRREQUEST,
  '__module__' : 'demo_pb2'
  # @@protoc_insertion_point(class_scope:demo.StrRequest)
  })
_sym_db.RegisterMessage(StrRequest)

Response = _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), {
  'DESCRIPTOR' : _RESPONSE,
  '__module__' : 'demo_pb2'
  # @@protoc_insertion_point(class_scope:demo.Response)
  })
_sym_db.RegisterMessage(Response)

StrResponse = _reflection.GeneratedProtocolMessageType('StrResponse', (_message.Message,), {
  'DESCRIPTOR' : _STRRESPONSE,
  '__module__' : 'demo_pb2'
  # @@protoc_insertion_point(class_scope:demo.StrResponse)
  })
_sym_db.RegisterMessage(StrResponse)

Person = _reflection.GeneratedProtocolMessageType('Person', (_message.Message,), {
  'DESCRIPTOR' : _PERSON,
  '__module__' : 'demo_pb2'
  # @@protoc_insertion_point(class_scope:demo.Person)
  })
_sym_db.RegisterMessage(Person)

AddressBook = _reflection.GeneratedProtocolMessageType('AddressBook', (_message.Message,), {
  'DESCRIPTOR' : _ADDRESSBOOK,
  '__module__' : 'demo_pb2'
  # @@protoc_insertion_point(class_scope:demo.AddressBook)
  })
_sym_db.RegisterMessage(AddressBook)



_GRPCDEMO = _descriptor.ServiceDescriptor(
  name='GRPCDemo',
  full_name='demo.GRPCDemo',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=291,
  serialized_end=408,
  methods=[
  _descriptor.MethodDescriptor(
    name='SimpleGetMethod',
    full_name='demo.GRPCDemo.SimpleGetMethod',
    index=0,
    containing_service=None,
    input_type=_STRREQUEST,
    output_type=_RESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='SimplePostMethod',
    full_name='demo.GRPCDemo.SimplePostMethod',
    index=1,
    containing_service=None,
    input_type=_REQUEST,
    output_type=_STRRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_GRPCDEMO)

DESCRIPTOR.services_by_name['GRPCDemo'] = _GRPCDEMO

# @@protoc_insertion_point(module_scope)
