import requests


class Platform:
    def __init__(self, jwt="", backendURL="https://prod-api.kosetto.com", heders={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
        (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',

        

    }):
        self.BACKEND_URL = backendURL
        self.HEADERS = heders
        self.JWT = jwt

    def getRecentlyJoinedUsers(self):
        '''Returns Response object with list of recently joined users'''

        url = f'{self.BACKEND_URL}/lists/recently-joined'
        response = requests.get(url, headers=self.HEADERS)
        return response

    def getGlobalActivity(self):
        '''Returns Response object with list of all recent share trades on the platform'''
        url = f'{self.BACKEND_URL}/global-activity'
        response = requests.get(url, headers=self.HEADERS)
        return response

    def getAddressFromTwitterUsername(self, username):
        '''Returns base address of the user'''
        newHeader = self.HEADERS
        newHeader['Authorization'] = self.JWT
        url = f'{self.BACKEND_URL}/search/users?username={username}'
        print(newHeader)
        response = requests.get(url, headers=newHeader)
        return response

    def getInfoFromAddress(self, address):
        '''Returns user info from address'''
        url = f'{self.BACKEND_URL}/users/{address}'
        response = requests.get(url, headers=self.HEADERS)
        return response

    def getInfoFromUserID(self, userID):
        '''Returns info from userID of friendtech user.'''
        url = f'{self.BACKEND_URL}/users/by-id/{userID}'
        response = requests.get(url, headers=self.HEADERS)
        return response

    def getHolders(self, address):
        '''returns token holder of an address'''
        url = f'{self.BACKEND_URL}/users/{address}/token/holders'
        response = requests.get(url, headers=self.HEADERS)
        return response
    
    def getHoldings(self, address):
        '''returns token holdings of an address'''
        url = f'{self.BACKEND_URL}/users/{address}/token-holdings'
        response = requests.get(url, headers=self.HEADERS)
        return response