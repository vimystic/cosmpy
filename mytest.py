from cosmpy.aerial.client import LedgerClient, NetworkConfig

# connect to Fetch.ai network using default parameters
ledger_client = LedgerClient(NetworkConfig.osmosis_chain_mainnet())

alice: str = 'osmo1f8rcf47jpqq2thq9vjsap9y0eclzqeqxaxusl2'
balances = ledger_client.query_bank_all_balances(alice)

# show all coin balances
for coin in balances:
  print(f'{coin.amount}{coin.denom}')