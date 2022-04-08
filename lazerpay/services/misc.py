from .._http_client import HTTPClient

class Misc:

    def __init__(self, headers, coins_url):
        self.headers   = headers
        self.coins_url = coins_url

    async def get_accepted_coins(self):
        """Requests all accepted coins"""
        async with HTTPClient(self.coins_url, headers=self.headers) as session:
            response, json_data = await session.requests("GET")
            return json_data  