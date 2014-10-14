from nio.metadata.properties import ListProperty
from nio.common.discovery import Discoverable, DiscoverableType
from nio.common.signal.base import Signal
from .http_blocks.rest.rest_block import RESTPolling


@Discoverable(DiscoverableType.block)
class Stock(RESTPolling):

    _yql_base_url = ("https://query.yahooapis.com/v1/public/yql?"
                     "q=select%20*%20from%20yahoo.finance.quote%20where"
                     "%20symbol%20in%20({0})&format=json"
                     "&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys")

    queries = ListProperty(str, title='Symbols/Tickers')

    def __init__(self):
        super().__init__()

    def start(self):
        super().start()
        # RESTPolling handles scheduling the poll job,
        # but we want one poll on start.
        self.poll()

    def _prepare_url(self, paging=False):
        sym_str = ",".join(['"' + sym + '"' for sym in self.queries])
        self._url = self._yql_base_url.format(sym_str)

        return {"Content-Type": "application/json"}

    def _process_response(self, resp):
        body = resp.json()

        try:
            results = body['query']['results']
        except Exception:
            self._logger.error("Invalid resposnse format: {0}".format(body))
            results = None

        if not results or not isinstance(results, dict):
            self._logger.warning("No results found: {0}".format(results))
            return [], None

        # If only one query, then quote is a dict instead of a list
        quote = results.get('quote', [])
        if not isinstance(quote, list):
            quote = [quote]

        # No paging
        return [Signal(s) for s in quote], None
