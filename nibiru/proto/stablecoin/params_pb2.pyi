"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class Params(google.protobuf.message.Message):
    """Params defines the parameters for the module."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    COLL_RATIO_FIELD_NUMBER: builtins.int
    FEE_RATIO_FIELD_NUMBER: builtins.int
    EF_FEE_RATIO_FIELD_NUMBER: builtins.int
    BONUS_RATE_RECOLL_FIELD_NUMBER: builtins.int
    DISTR_EPOCH_IDENTIFIER_FIELD_NUMBER: builtins.int
    ADJUSTMENT_STEP_FIELD_NUMBER: builtins.int
    PRICE_LOWER_BOUND_FIELD_NUMBER: builtins.int
    PRICE_UPPER_BOUND_FIELD_NUMBER: builtins.int
    IS_COLLATERAL_RATIO_VALID_FIELD_NUMBER: builtins.int
    coll_ratio: builtins.int
    """collRatio is the ratio needed as collateral to exchange for stables"""

    fee_ratio: builtins.int
    """feeRatio is the ratio taken as fees when minting or burning stables"""

    ef_fee_ratio: builtins.int
    """efFeeRatio is the ratio taken from the fees that goes to Ecosystem Fund"""

    bonus_rate_recoll: builtins.int
    """BonusRateRecoll is the percentage of extra stablecoin value given to the caller
    of 'Recollateralize' in units of governance tokens.
    """

    distr_epoch_identifier: typing.Text
    """distr_epoch_identifier defines the frequnecy of update for the collateral ratio"""

    adjustment_step: builtins.int
    """adjustmentStep is the size of the step taken when updating the collateral ratio"""

    price_lower_bound: builtins.int
    """priceLowerBound is the lower bound for the stable coin to trigger a collateral ratio update"""

    price_upper_bound: builtins.int
    """priceUpperBound is the upper bound for the stable coin to trigger a collateral ratio update"""

    is_collateral_ratio_valid: builtins.bool
    """isCollateralRatioValid checks if the collateral ratio is correctly updated"""

    def __init__(self,
        *,
        coll_ratio: builtins.int = ...,
        fee_ratio: builtins.int = ...,
        ef_fee_ratio: builtins.int = ...,
        bonus_rate_recoll: builtins.int = ...,
        distr_epoch_identifier: typing.Text = ...,
        adjustment_step: builtins.int = ...,
        price_lower_bound: builtins.int = ...,
        price_upper_bound: builtins.int = ...,
        is_collateral_ratio_valid: builtins.bool = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["adjustment_step",b"adjustment_step","bonus_rate_recoll",b"bonus_rate_recoll","coll_ratio",b"coll_ratio","distr_epoch_identifier",b"distr_epoch_identifier","ef_fee_ratio",b"ef_fee_ratio","fee_ratio",b"fee_ratio","is_collateral_ratio_valid",b"is_collateral_ratio_valid","price_lower_bound",b"price_lower_bound","price_upper_bound",b"price_upper_bound"]) -> None: ...
global___Params = Params
