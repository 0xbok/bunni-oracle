import requests
import json
import math
from web3 import Web3

localrpc="http://127.0.0.1:8545"
w3 = Web3(Web3.HTTPProvider(localrpc))

pool_abi = [
    {"inputs":[],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"owner","type":"address"},{"indexed":True,"internalType":"int24","name":"tickLower","type":"int24"},{"indexed":True,"internalType":"int24","name":"tickUpper","type":"int24"},{"indexed":False,"internalType":"uint128","name":"amount","type":"uint128"},{"indexed":False,"internalType":"uint256","name":"amount0","type":"uint256"},{"indexed":False,"internalType":"uint256","name":"amount1","type":"uint256"}],"name":"Burn","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"owner","type":"address"},{"indexed":False,"internalType":"address","name":"recipient","type":"address"},{"indexed":True,"internalType":"int24","name":"tickLower","type":"int24"},{"indexed":True,"internalType":"int24","name":"tickUpper","type":"int24"},{"indexed":False,"internalType":"uint128","name":"amount0","type":"uint128"},{"indexed":False,"internalType":"uint128","name":"amount1","type":"uint128"}],"name":"Collect","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"sender","type":"address"},{"indexed":True,"internalType":"address","name":"recipient","type":"address"},{"indexed":False,"internalType":"uint128","name":"amount0","type":"uint128"},{"indexed":False,"internalType":"uint128","name":"amount1","type":"uint128"}],"name":"CollectProtocol","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"sender","type":"address"},{"indexed":True,"internalType":"address","name":"recipient","type":"address"},{"indexed":False,"internalType":"uint256","name":"amount0","type":"uint256"},{"indexed":False,"internalType":"uint256","name":"amount1","type":"uint256"},{"indexed":False,"internalType":"uint256","name":"paid0","type":"uint256"},{"indexed":False,"internalType":"uint256","name":"paid1","type":"uint256"}],"name":"Flash","type":"event"},{"anonymous":False,"inputs":[{"indexed":False,"internalType":"uint16","name":"observationCardinalityNextOld","type":"uint16"},{"indexed":False,"internalType":"uint16","name":"observationCardinalityNextNew","type":"uint16"}],"name":"IncreaseObservationCardinalityNext","type":"event"},{"anonymous":False,"inputs":[{"indexed":False,"internalType":"uint160","name":"sqrtPriceX96","type":"uint160"},{"indexed":False,"internalType":"int24","name":"tick","type":"int24"}],"name":"Initialize","type":"event"},{"anonymous":False,"inputs":[{"indexed":False,"internalType":"address","name":"sender","type":"address"},{"indexed":True,"internalType":"address","name":"owner","type":"address"},{"indexed":True,"internalType":"int24","name":"tickLower","type":"int24"},{"indexed":True,"internalType":"int24","name":"tickUpper","type":"int24"},{"indexed":False,"internalType":"uint128","name":"amount","type":"uint128"},{"indexed":False,"internalType":"uint256","name":"amount0","type":"uint256"},{"indexed":False,"internalType":"uint256","name":"amount1","type":"uint256"}],"name":"Mint","type":"event"},{"anonymous":False,"inputs":[{"indexed":False,"internalType":"uint8","name":"feeProtocol0Old","type":"uint8"},{"indexed":False,"internalType":"uint8","name":"feeProtocol1Old","type":"uint8"},{"indexed":False,"internalType":"uint8","name":"feeProtocol0New","type":"uint8"},{"indexed":False,"internalType":"uint8","name":"feeProtocol1New","type":"uint8"}],"name":"SetFeeProtocol","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"sender","type":"address"},{"indexed":True,"internalType":"address","name":"recipient","type":"address"},{"indexed":False,"internalType":"int256","name":"amount0","type":"int256"},{"indexed":False,"internalType":"int256","name":"amount1","type":"int256"},{"indexed":False,"internalType":"uint160","name":"sqrtPriceX96","type":"uint160"},{"indexed":False,"internalType":"uint128","name":"liquidity","type":"uint128"},{"indexed":False,"internalType":"int24","name":"tick","type":"int24"}],"name":"Swap","type":"event"},{"inputs":[{"internalType":"int24","name":"tickLower","type":"int24"},{"internalType":"int24","name":"tickUpper","type":"int24"},{"internalType":"uint128","name":"amount","type":"uint128"}],"name":"burn","outputs":[{"internalType":"uint256","name":"amount0","type":"uint256"},{"internalType":"uint256","name":"amount1","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"recipient","type":"address"},{"internalType":"int24","name":"tickLower","type":"int24"},{"internalType":"int24","name":"tickUpper","type":"int24"},{"internalType":"uint128","name":"amount0Requested","type":"uint128"},{"internalType":"uint128","name":"amount1Requested","type":"uint128"}],"name":"collect","outputs":[{"internalType":"uint128","name":"amount0","type":"uint128"},{"internalType":"uint128","name":"amount1","type":"uint128"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"recipient","type":"address"},{"internalType":"uint128","name":"amount0Requested","type":"uint128"},{"internalType":"uint128","name":"amount1Requested","type":"uint128"}],"name":"collectProtocol","outputs":[{"internalType":"uint128","name":"amount0","type":"uint128"},{"internalType":"uint128","name":"amount1","type":"uint128"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"factory","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"fee","outputs":[{"internalType":"uint24","name":"","type":"uint24"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"feeGrowthGlobal0X128","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"feeGrowthGlobal1X128","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"recipient","type":"address"},{"internalType":"uint256","name":"amount0","type":"uint256"},{"internalType":"uint256","name":"amount1","type":"uint256"},{"internalType":"bytes","name":"data","type":"bytes"}],"name":"flash","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint16","name":"observationCardinalityNext","type":"uint16"}],"name":"increaseObservationCardinalityNext","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint160","name":"sqrtPriceX96","type":"uint160"}],"name":"initialize","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"liquidity","outputs":[{"internalType":"uint128","name":"","type":"uint128"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"maxLiquidityPerTick","outputs":[{"internalType":"uint128","name":"","type":"uint128"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"recipient","type":"address"},{"internalType":"int24","name":"tickLower","type":"int24"},{"internalType":"int24","name":"tickUpper","type":"int24"},{"internalType":"uint128","name":"amount","type":"uint128"},{"internalType":"bytes","name":"data","type":"bytes"}],"name":"mint","outputs":[{"internalType":"uint256","name":"amount0","type":"uint256"},{"internalType":"uint256","name":"amount1","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"observations","outputs":[{"internalType":"uint32","name":"blockTimestamp","type":"uint32"},{"internalType":"int56","name":"tickCumulative","type":"int56"},{"internalType":"uint160","name":"secondsPerLiquidityCumulativeX128","type":"uint160"},{"internalType":"bool","name":"initialized","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint32[]","name":"secondsAgos","type":"uint32[]"}],"name":"observe","outputs":[{"internalType":"int56[]","name":"tickCumulatives","type":"int56[]"},{"internalType":"uint160[]","name":"secondsPerLiquidityCumulativeX128s","type":"uint160[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"name":"positions","outputs":[{"internalType":"uint128","name":"liquidity","type":"uint128"},{"internalType":"uint256","name":"feeGrowthInside0LastX128","type":"uint256"},{"internalType":"uint256","name":"feeGrowthInside1LastX128","type":"uint256"},{"internalType":"uint128","name":"tokensOwed0","type":"uint128"},{"internalType":"uint128","name":"tokensOwed1","type":"uint128"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"protocolFees","outputs":[{"internalType":"uint128","name":"token0","type":"uint128"},{"internalType":"uint128","name":"token1","type":"uint128"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint8","name":"feeProtocol0","type":"uint8"},{"internalType":"uint8","name":"feeProtocol1","type":"uint8"}],"name":"setFeeProtocol","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"slot0","outputs":[{"internalType":"uint160","name":"sqrtPriceX96","type":"uint160"},{"internalType":"int24","name":"tick","type":"int24"},{"internalType":"uint16","name":"observationIndex","type":"uint16"},{"internalType":"uint16","name":"observationCardinality","type":"uint16"},{"internalType":"uint16","name":"observationCardinalityNext","type":"uint16"},{"internalType":"uint8","name":"feeProtocol","type":"uint8"},{"internalType":"bool","name":"unlocked","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"int24","name":"tickLower","type":"int24"},{"internalType":"int24","name":"tickUpper","type":"int24"}],"name":"snapshotCumulativesInside","outputs":[{"internalType":"int56","name":"tickCumulativeInside","type":"int56"},{"internalType":"uint160","name":"secondsPerLiquidityInsideX128","type":"uint160"},{"internalType":"uint32","name":"secondsInside","type":"uint32"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"recipient","type":"address"},{"internalType":"bool","name":"zeroForOne","type":"bool"},{"internalType":"int256","name":"amountSpecified","type":"int256"},{"internalType":"uint160","name":"sqrtPriceLimitX96","type":"uint160"},{"internalType":"bytes","name":"data","type":"bytes"}],"name":"swap","outputs":[{"internalType":"int256","name":"amount0","type":"int256"},{"internalType":"int256","name":"amount1","type":"int256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"int16","name":"","type":"int16"}],"name":"tickBitmap","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"tickSpacing","outputs":[{"internalType":"int24","name":"","type":"int24"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"int24","name":"","type":"int24"}],"name":"ticks","outputs":[{"internalType":"uint128","name":"liquidityGross","type":"uint128"},{"internalType":"int128","name":"liquidityNet","type":"int128"},{"internalType":"uint256","name":"feeGrowthOutside0X128","type":"uint256"},{"internalType":"uint256","name":"feeGrowthOutside1X128","type":"uint256"},{"internalType":"int56","name":"tickCumulativeOutside","type":"int56"},{"internalType":"uint160","name":"secondsPerLiquidityOutsideX128","type":"uint160"},{"internalType":"uint32","name":"secondsOutside","type":"uint32"},{"internalType":"bool","name":"initialized","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"token0","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"token1","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"}
]

liq_amounts_abi = [
    {
      "inputs": [],
      "name": "T",
      "type": "error"
    },
    {
      "inputs": [
        {
          "internalType": "uint160",
          "name": "sqrtRatioX96",
          "type": "uint160"
        },
        {
          "internalType": "uint160",
          "name": "sqrtRatioAX96",
          "type": "uint160"
        },
        {
          "internalType": "uint160",
          "name": "sqrtRatioBX96",
          "type": "uint160"
        },
        {
          "internalType": "uint128",
          "name": "liquidity",
          "type": "uint128"
        }
      ],
      "name": "getAmountsForLiquidity",
      "outputs": [
        {
          "internalType": "uint256",
          "name": "amount0",
          "type": "uint256"
        },
        {
          "internalType": "uint256",
          "name": "amount1",
          "type": "uint256"
        }
      ],
      "stateMutability": "pure",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "int24",
          "name": "tick",
          "type": "int24"
        }
      ],
      "name": "getSqrtRatioAtTick",
      "outputs": [
        {
          "internalType": "uint160",
          "name": "sqrtPriceX96",
          "type": "uint160"
        }
      ],
      "stateMutability": "pure",
      "type": "function"
    }
  ]

# Change on each local test deployment
LiqAmounts="0x46d4674578a2daBbD0CEAB0500c6c7867999db34"

def get_token_price(chain, contract_address, vs_currency):
    url = f"https://api.coingecko.com/api/v3/simple/token_price/{chain}"
    params = {
        "contract_addresses": contract_address,
        "vs_currencies": vs_currency,
        "include_last_updated_at": "True"
    }
    response = requests.get(url, params=params)
    data = response.json()

    # Extract the token price from the response
    price = data.get(contract_address.lower(), {}).get(vs_currency.lower())
    print("price", contract_address, price)
    if price:
        return price
    else:
        return None

def get_token_base(token_address):
    payload = {
        "jsonrpc": "2.0",
        "method": "eth_call",
        "params": [
            {
                "to": token_address,
                "data": "0x313ce567"  # Function signature for decimals()
            },
            "latest"
        ],
        "id": 1
    }
    headers = {"Content-Type": "application/json"}
    response = requests.post(localrpc, data=json.dumps(payload), headers=headers)
    result = response.json()

    # Extract the decimals from the response
    decimals_hex = result.get("result")
    if decimals_hex:
        decimals = int(decimals_hex, 16)
        return decimals
    else:
        return None

def get_sqrt_x96(price0usd, price1usd):
    return math.sqrt(price0usd/price1usd) * (2**96)

def get_valueusd(token, amount, price):
    return int(price*amount*(10**18)/(10**get_token_base(token)))

def lp_price(token0, amount0, price0usd, token1, amount1, price1usd):
    return get_valueusd(token0, amount0, price0usd) + get_valueusd(token1, amount1, price1usd)

def get_amounts_for_liquidity(sqrtX96, sqrtAX96, sqrtBX96, liquidity):
    contract = w3.eth.contract(address=LiqAmounts, abi=liq_amounts_abi)
    (amount0, amount1) = contract.functions.getAmountsForLiquidity(sqrtX96, sqrtAX96, sqrtBX96, liquidity).call()
    return (amount0, amount1)

def get_sqrt_ratio_at_tick(tick):
    contract = w3.eth.contract(address=LiqAmounts, abi=liq_amounts_abi)
    ratio = contract.functions.getSqrtRatioAtTick(tick).call()
    return ratio

def quoteusd(pool, tick_lower, tick_higher, liquidity):
    contract = w3.eth.contract(address=pool, abi=pool_abi)
    token0 = contract.functions.token0().call()
    token1 = contract.functions.token1().call()

    price0 = get_token_price("ethereum", token0, "usd")
    price1 = get_token_price("ethereum", token1, "usd")

    (amount0, amount1) = get_amounts_for_liquidity(int(get_sqrt_x96(price0, price1)), get_sqrt_ratio_at_tick(tick_lower), get_sqrt_ratio_at_tick(tick_higher), liquidity)

    return lp_price(token0, amount0, price0, token1, amount1, price1)

print(quoteusd("0xCBCdF9626bC03E24f779434178A73a0B4bad62eD", 257220, 257820, 644350055919596))

