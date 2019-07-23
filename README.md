# CoinRpc

CoinRpc is simple and tiny library for working with cryptocurrency nodes over JSON-RPC protocol.

````python
from coinrpc import *
from requests.auth import HTTPDigestAuth

# Retrive new address from bitcoin-like node
CoinRpc('http://rpcuser:rpcpassword@127.0.0.1:8332', 3, 10).getnewaddress()

# Retrive new address from monero-like node
CoinRpc('http://127.0.0.1:18082/json_rpc', 3, 10, {'id': 1}, HTTPDigestAuth('user', 'password')).make_integrated_address()
````