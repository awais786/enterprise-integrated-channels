"""
Tests for the base exporter.
"""

import unittest
from unittest import mock

from channel_integrations.integrated_channel.exporters import Exporter


class TestExporter(unittest.TestCase):
    """
    Tests for the base ``Exporter`` class.
    """

    def test_export(self):
        """
        The ``export`` method is not implemented at the base, and so should raise ``NotImplementedError``.
        """
        with self.assertRaises(NotImplementedError):
            Exporter(user=None, enterprise_configuration=mock.Mock(enterprise_customer=None)).export()
