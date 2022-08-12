# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cosmos/bank/v1beta1/genesis.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from cosmos.bank.v1beta1 import bank_pb2 as cosmos_dot_bank_dot_v1beta1_dot_bank__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!cosmos/bank/v1beta1/genesis.proto\x12\x13\x63osmos.bank.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x1e\x63osmos/base/v1beta1/coin.proto\x1a\x1e\x63osmos/bank/v1beta1/bank.proto\"\xaa\x02\n\x0cGenesisState\x12\x31\n\x06params\x18\x01 \x01(\x0b\x32\x1b.cosmos.bank.v1beta1.ParamsB\x04\xc8\xde\x1f\x00\x12\x34\n\x08\x62\x61lances\x18\x02 \x03(\x0b\x32\x1c.cosmos.bank.v1beta1.BalanceB\x04\xc8\xde\x1f\x00\x12[\n\x06supply\x18\x03 \x03(\x0b\x32\x19.cosmos.base.v1beta1.CoinB0\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins\xc8\xde\x1f\x00\x12T\n\x0e\x64\x65nom_metadata\x18\x04 \x03(\x0b\x32\x1d.cosmos.bank.v1beta1.MetadataB\x1d\xf2\xde\x1f\x15yaml:\"denom_metadata\"\xc8\xde\x1f\x00\"\x80\x01\n\x07\x42\x61lance\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\t\x12Z\n\x05\x63oins\x18\x02 \x03(\x0b\x32\x19.cosmos.base.v1beta1.CoinB0\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins\xc8\xde\x1f\x00:\x08\xe8\xa0\x1f\x00\x88\xa0\x1f\x00\x42+Z)github.com/cosmos/cosmos-sdk/x/bank/typesb\x06proto3')



_GENESISSTATE = DESCRIPTOR.message_types_by_name['GenesisState']
_BALANCE = DESCRIPTOR.message_types_by_name['Balance']
GenesisState = _reflection.GeneratedProtocolMessageType('GenesisState', (_message.Message,), {
  'DESCRIPTOR' : _GENESISSTATE,
  '__module__' : 'cosmos.bank.v1beta1.genesis_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.bank.v1beta1.GenesisState)
  })
_sym_db.RegisterMessage(GenesisState)

Balance = _reflection.GeneratedProtocolMessageType('Balance', (_message.Message,), {
  'DESCRIPTOR' : _BALANCE,
  '__module__' : 'cosmos.bank.v1beta1.genesis_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.bank.v1beta1.Balance)
  })
_sym_db.RegisterMessage(Balance)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z)github.com/cosmos/cosmos-sdk/x/bank/types'
  _GENESISSTATE.fields_by_name['params']._options = None
  _GENESISSTATE.fields_by_name['params']._serialized_options = b'\310\336\037\000'
  _GENESISSTATE.fields_by_name['balances']._options = None
  _GENESISSTATE.fields_by_name['balances']._serialized_options = b'\310\336\037\000'
  _GENESISSTATE.fields_by_name['supply']._options = None
  _GENESISSTATE.fields_by_name['supply']._serialized_options = b'\252\337\037(github.com/cosmos/cosmos-sdk/types.Coins\310\336\037\000'
  _GENESISSTATE.fields_by_name['denom_metadata']._options = None
  _GENESISSTATE.fields_by_name['denom_metadata']._serialized_options = b'\362\336\037\025yaml:\"denom_metadata\"\310\336\037\000'
  _BALANCE.fields_by_name['coins']._options = None
  _BALANCE.fields_by_name['coins']._serialized_options = b'\252\337\037(github.com/cosmos/cosmos-sdk/types.Coins\310\336\037\000'
  _BALANCE._options = None
  _BALANCE._serialized_options = b'\350\240\037\000\210\240\037\000'
  _GENESISSTATE._serialized_start=145
  _GENESISSTATE._serialized_end=443
  _BALANCE._serialized_start=446
  _BALANCE._serialized_end=574
# @@protoc_insertion_point(module_scope)
