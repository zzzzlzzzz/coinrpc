from requests import Session
from requests.exceptions import RequestException

from .exceptions import CoinRpcException


class CoinRpc:
    """
    CoinRpc core class
    """
    def __init__(self, url, attempts, timeout, static_payload=None, auth=None):
        """
        Initializer for CoinRpc

        :param url: URL to rpc node (ex. http://user:password@127.0.0.1:8332)
        :param attempts: Number attempts before fail
        :param timeout: Timeout for connection
        :param static_payload: Payload for adding to all rpc requests
        :param auth: Auth class (for ex. request.auth.HTTPDigestAuth)
        """
        self._url = url
        self._attempts = attempts
        self._timeout = timeout
        self.static_payload = {'jsonrpc': '2.0'}
        if static_payload:
            self.static_payload.update(static_payload)
        self._session = Session()
        self._session.auth = auth

    def __getattr__(self, item):
        """
        Return proxy function for rpc call

        :param item: Name of function
        :return: Result of rpc call
        """
        def invoke(*args, **kwargs):
            payload = {'method': item, 'params': list(args) or dict(kwargs), **self.static_payload}
            attempt = 0
            while True:
                try:
                    response = self._session.post(self._url, json=payload, timeout=self._timeout)
                    if response.status_code not in (200, 500):
                        raise ValueError('{0} {1}'.format(response.status_code, response.reason))
                    response = response.json()
                except (RequestException, ValueError) as e:
                    attempt += 1
                    if attempt >= self._attempts:
                        raise CoinRpcException(e)
                else:
                    error = response.get('error')
                    if error:
                        raise CoinRpcException(error)
                    return response.get('result')

        return invoke
