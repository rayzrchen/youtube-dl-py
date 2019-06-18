from unittest.mock import MagicMock


class ProductionClass:
    def method(self):
        self.something(1, 2, 3)

    def something(self, a, b, c):
        pass


thing = ProductionClass()
thing.method = MagicMock(return_value=3)
thing.method.assert_called_with(3, 4, 5, key='value')

