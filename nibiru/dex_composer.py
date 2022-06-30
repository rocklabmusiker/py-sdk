from dataclasses import dataclass

from .proto.dex.v1 import (
    tx_pb2 as dex_tx_pb,
    pool_pb2 as pool_tx_pb,
)

from .proto.cosmos.base.v1beta1 import coin_pb2 as cosmos_base_coin_pb

from typing import List


@dataclass
class PoolAsset:
    token: cosmos_base_coin_pb.Coin
    weight: str


class DexComposer:
    # DEX
    def create_pool(self, creator: str, swap_fee: str, exit_fee: str, assets: List[PoolAsset]):
        pool_assets = [pool_tx_pb.PoolAsset(token=a.token, weight=a.weight) for a in assets]

        return dex_tx_pb.MsgCreatePool(
            creator = creator,
            poolParams = pool_tx_pb.PoolParams(swapFee=swap_fee, exitFee=exit_fee),
            poolAssets = pool_assets,
        )

    def join_pool(self, sender: str, pool_id: int, tokens: List[cosmos_base_coin_pb.Coin]):
        return dex_tx_pb.MsgJoinPool(
            sender = sender,
            pool_id = pool_id,
            tokens_in = tokens,
        )

    def exit_pool(self, sender: str, pool_id: int, pool_shares: cosmos_base_coin_pb.Coin):
        return dex_tx_pb.MsgExitPool(
            sender = sender,
            pool_id = pool_id,
            pool_shares = pool_shares,
        )

    def swap_assets(self, sender: str, pool_id: int, token_in: cosmos_base_coin_pb.Coin, token_out_denom):
        return dex_tx_pb.MsgSwapAssets(
            sender = sender,
            pool_id = pool_id,
            token_in = token_in,
            token_out_denom = token_out_denom,
        )
