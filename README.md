# friendtech - A python module to interact with friend.tech platform

Run `pip install friendtech` to install the module!

The module uses friend.tech APIs (by default) and you can change the nodeURL to use any other node.

Developed by [ItsAditya](https://twitter.com/itsaditya_xyz)

For support join discord: [FriendTechFeed](https://discord.gg/sVNcFK73YW)

## How to Use:

# Platform Info

1. Getting global activity (list of recent trades on the platform)

```python
import friendtech
import json


platform = friendtech.Platform()
globalActivity = platform.getGlobalActivity().json()
print(globalActivity)
```

2. Getting recently joined users

```python
import friendtech
import json


platform = friendtech.Platform()
recentlyJoined = platform.getRecentlyJoinedUsers().json()
print(recentlyJoined)
```

3. Getting address from twitter username

```python
import friendtech
import json

jwt = <YOUR JWT TOKEN> # get this from local storage of friendtech in your browser
platform = friendtech.Platform(jwt=jwt)
addressInfo = platform.getAddressFromTwitterUsername("itsaditya_xyz").json()
print(addressInfo)
```

3. Getting share and profile info from address

```python
import friendtech
import json


platform = friendtech.Platform()
userInfo = platform.getInfoFromAddress("0xeab1e59d08e927ec19c9249f4841395bc4af43b8").json()
print(userInfo)
```

# Contract

1. Getting buy price of a share

```python
import friendtech

contract = friendtech.Contract()
buyPrice = contract.getBuyPrice("0xeab1e59d08e927ec19c9249f4841395bc4af43b8", 1)
print(buyPrice)
```

2. Getting buy price after fee of a share

```python
import friendtech

contract = friendtech.Contract()
buyPrice = contract.getBuyPriceAfterFee("0xeab1e59d08e927ec19c9249f4841395bc4af43b8", 1)
print(buyPrice)
```

3. Getting sell price of a share

```python
import friendtech

contract = friendtech.Contract()
sellPrice = contract.getSellPrice("0xeab1e59d08e927ec19c9249f4841395bc4af43b8", 1)
print(sellPrice)
```

4. Getting sell price after fee of a share

```python
import friendtech

contract = friendtech.Contract()
sellPrice = contract.getSellPriceAfterFee("0xeab1e59d08e927ec19c9249f4841395bc4af43b8", 1)
print(sellPrice)
```

5. Getting shares supply

```python
import friendtech

contract = friendtech.Contract()
shareSupply = contract.getSharesSupply("0xeab1e59d08e927ec19c9249f4841395bc4af43b8")
print(shareSupply)
```

6. Getting shares owned by an address for subjectAddress

```python
import friendtech

contract = friendtech.Contract()
address = "0xeab1e59d08e927ec19c9249f4841395bc4af43b8"
subjectAddress = "0x61da0a10f748a4d0c7060cd0d9907f9174f59a15"
sharesOwned = contract.getSharesSupply(address, subjectAddress)
print(sharesOwned)
```

# WRITING FUNCTIONS OF CONTRACT

To execute writing functions you will need a wallet that has some eth on base network

1. Create a new wallet (store the private key in .env always!)

```python
from eth_account import Account
import secrets
priv = secrets.token_hex(32)
private_key = "0x" + priv
print ("SAVE BUT DO NOT SHARE THIS:", private_key)
acct = Account.from_key(private_key)
print("Address:", acct.address)
```

