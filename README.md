# friendtech - A python module to interact with friend.tech platform

Run `pip install friendtech` to install the module!

The module uses friend.tech APIs (by default) and you can change the nodeURL to use any other node.

Developed by [ItsAditya](https://twitter.com/itsaditya_xyz)

For support join discord: [FriendTechFeed](https://discord.gg/sVNcFK73YW)

## How to Use:

# Platform Info

1. Getting global activity (list of recent trades on the platform)

````python
import friendtech
import json


platform = friendtech.Platform()
globalActivity = platform.getGlobalActivity().json()
print(globalActivity)
````

2. Getting recently joined users

````python
import friendtech
import json


platform = friendtech.Platform()
recentlyJoined = platform.getRecentlyJoinedUsers().json()
print(recentlyJoined)
````

3. Getting address from twitter username

````python
import friendtech
import json


platform = friendtech.Platform()
addressInfo = platform.getAddressFromTwitterUsername("itsaditya_xyz").json()
print(addressInfo)
````


3. Getting share and profile info from address

````python
import friendtech
import json


platform = friendtech.Platform()
userInfo = platform.getInfoFromAddress("0xeab1e59d08e927ec19c9249f4841395bc4af43b8").json()
print(userInfo)
````