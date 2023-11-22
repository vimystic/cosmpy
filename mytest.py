from cosmpy.aerial.client import LedgerClient, NetworkConfig

ledger_client = LedgerClient(NetworkConfig.osmosis_chain_mainnet())

alice: str = 'osmo1f8rcf47jpqq2thq9vjsap9y0eclzqeqxaxusl2'
balances = ledger_client.query_bank_all_balances(alice)

print(balances)
