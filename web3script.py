from web3 import Web3
infura_url = "https://mainnet.infura.io/v3/a85f2f1e78ba427ab6120e60d4ee92e3"
web3 = Web3(Web3.HTTPProvider(infura_url))
conStatus = web3.isConnected()
print(conStatus)
ethWallet = "ETH_ADDRESS"
balance = web3.eth.getBalance(ethWallet)
print(balance)
