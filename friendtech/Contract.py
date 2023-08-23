'''THIS FILE HAS CODE TO INTRACT WITH THE CONTRACT'''
import web3
from eth_account import Account


class Contract:
    def __init__(self, contractAddress="0xCF205808Ed36593aa40a44F10c7f7C2F67d4A4d4", BASE_MAINNET="https://developer-access-mainnet.base.org/", privateKey=None):
        self.CONTRACT_ADDRESS = contractAddress
        self.PRIVATE_KEY = privateKey
        self.BASE_MAINNET = BASE_MAINNET

    # READ FUNCTIONS
    def getBuyPrice(self, address, amount):
        '''returns buy price of shares in wei'''

        checkSumAddress = web3.Web3.toChecksumAddress(address)
        w3 = web3.Web3(web3.HTTPProvider(self.BASE_MAINNET))
        contractABI = open("./friendtech/contractABI.json", "r").read()
        contract = w3.eth.contract(
            address=self.CONTRACT_ADDRESS, abi=contractABI)
        buyPrice = contract.functions.getBuyPrice(
            w3.toChecksumAddress(checkSumAddress), amount).call()
        return buyPrice

    def getBuyPriceAfterFee(self, address, amount):
        '''returns buy price of a share after fees in wei'''

        checkSumAddress = web3.Web3.toChecksumAddress(address)
        w3 = web3.Web3(web3.HTTPProvider(self.BASE_MAINNET))
        contractABI = open("./friendtech/contractABI.json", "r").read()
        contract = w3.eth.contract(
            address=self.CONTRACT_ADDRESS, abi=contractABI)
        buyPiceAfterFee = contract.functions.getBuyPriceAfterFee(
            w3.toChecksumAddress(checkSumAddress), amount).call()
        return buyPiceAfterFee

    def getSellPrice(self, address, amount):
        '''returns sell price'''
        checkSumAddress = web3.Web3.toChecksumAddress(address)
        w3 = web3.Web3(web3.HTTPProvider(self.BASE_MAINNET))
        contractABI = open("./friendtech/contractABI.json", "r").read()
        contract = w3.eth.contract(
            address=self.CONTRACT_ADDRESS, abi=contractABI)
        sellPrice = contract.functions.getSellPrice(
            w3.toChecksumAddress(checkSumAddress), amount).call()
        return sellPrice

    def getSellPriceAfterFee(self, address, amount):
        '''returns sell price after fee'''
        checkSumAddress = web3.Web3.toChecksumAddress(address)
        w3 = web3.Web3(web3.HTTPProvider(self.BASE_MAINNET))
        contractABI = open("./friendtech/contractABI.json", "r").read()
        contract = w3.eth.contract(
            address=self.CONTRACT_ADDRESS, abi=contractABI)
        sellPriceAfterFee = contract.functions.getSellPriceAfterFee(
            w3.toChecksumAddress(checkSumAddress), amount).call()
        return sellPriceAfterFee

    def getSharesSupply(self, address):
        '''returns supply of share of given address'''
        checkSumAddress = web3.Web3.toChecksumAddress(address)
        w3 = web3.Web3(web3.HTTPProvider(self.BASE_MAINNET))
        contractABI = open("./friendtech/contractABI.json", "r").read()
        contract = w3.eth.contract(
            address=self.CONTRACT_ADDRESS, abi=contractABI)
        sharesSupply = contract.functions.sharesSupply(
            w3.toChecksumAddress(checkSumAddress)).call()
        return sharesSupply

    def getSharesOwned(self, address, subjectAddress):
        '''returns how many shares of subjectAdderss the address owns'''
        checkSumAddress = web3.Web3.toChecksumAddress(address)
        checkSumSubjectAddress = web3.Web3.toChecksumAddress(subjectAddress)
        w3 = web3.Web3(web3.HTTPProvider(self.BASE_MAINNET))
        contractABI = open("./friendtech/contractABI.json", "r").read()
        contract = w3.eth.contract(
            address=self.CONTRACT_ADDRESS, abi=contractABI)
        sharesOwned = contract.functions.sharesBalance(
            checkSumSubjectAddress, checkSumAddress).call()
        return sharesOwned

    # BETA FUNCTIONS. NOT THOROUGLY TESTED. USE AT YOUR OWN RISK
    def buyShares(self, addressToBuy, payableAmount,  shareCount=1):
        addressToBuyCheckSum = web3.Web3.toChecksumAddress(addressToBuy)
        userAccount = Account.from_key(self.PRIVATE_KEY)
        userAddressCheckSum = w3.toChecksumAddress(userAccount.address)
        w3 = web3.Web3(web3.HTTPProvider(self.BASE_MAINNET))
        contractABI = open("./friendtech/contractABI.json", "r").read()
        chainID = w3.eth.chain_id
        nounce = w3.eth.get_transaction_count(userAddressCheckSum)
        contract = w3.eth.contract(
            address=self.CONTRACT_ADDRESS, abi=contractABI)

        callFunction = contract.functions.buyShares(addressToBuyCheckSum, shareCount).buildTransaction({
            "value": payableAmount,
            "chainId": chainID,
            "from": userAddressCheckSum,
            "nounce": nounce
        })

        signedTransaction = w3.eth.account.sign_transaction(
            callFunction, private_key=self.PRIVATE_KEY)

        sendTransaction = web3.eth.send_raw_transaction(
            signedTransaction.rawTransaction)

        transactionReceipt = web3.eth.wait_for_transaction_receipt(
            sendTransaction)
        return transactionReceipt

    def sellShares(self, addressToSell, shareCount=1):
        addressToBuyCheckSum = web3.Web3.toChecksumAddress(addressToSell)
        userAccount = Account.from_key(self.PRIVATE_KEY)
        userAddressCheckSum = w3.toChecksumAddress(userAccount.address)
        w3 = web3.Web3(web3.HTTPProvider(self.BASE_MAINNET))
        contractABI = open("./friendtech/contractABI.json", "r").read()
        chainID = w3.eth.chain_id
        nounce = w3.eth.get_transaction_count(userAddressCheckSum)
        contract = w3.eth.contract(
            address=self.CONTRACT_ADDRESS, abi=contractABI)

        callFunction = contract.functions.buyShares(addressToBuyCheckSum, shareCount).buildTransaction({
            "value": payableAmount,
            "chainId": chainID,
            "from": userAddressCheckSum,
            "nounce": nounce
        })

        signedTransaction = w3.eth.account.sign_transaction(
            callFunction, private_key=self.PRIVATE_KEY)

        sendTransaction = web3.eth.send_raw_transaction(
            signedTransaction.rawTransaction)

        transactionReceipt = web3.eth.wait_for_transaction_receipt(
            sendTransaction)
        return transactionReceipt
