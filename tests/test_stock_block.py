from nio.testing.block_test_case import NIOBlockTestCase

from ..stock_block import Stock


class TestStock(NIOBlockTestCase):

    def test_configure_start_stop(self):
        blk = Stock()
        self.configure_block(blk, {})
        blk.start()
        blk.stop()
