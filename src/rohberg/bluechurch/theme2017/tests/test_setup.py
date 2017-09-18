# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plone import api
from rohberg.bluechurch.theme2017.testing import ROHBERG_BLUECHURCH_THEME2017_INTEGRATION_TESTING  # noqa

import unittest


class TestSetup(unittest.TestCase):
    """Test that rohberg.bluechurch.theme2017 is properly installed."""

    layer = ROHBERG_BLUECHURCH_THEME2017_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if rohberg.bluechurch.theme2017 is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'rohberg.bluechurch.theme2017'))

    def test_browserlayer(self):
        """Test that IRohbergBluechurchTheme2017Layer is registered."""
        from rohberg.bluechurch.theme2017.interfaces import (
            IRohbergBluechurchTheme2017Layer)
        from plone.browserlayer import utils
        self.assertIn(IRohbergBluechurchTheme2017Layer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = ROHBERG_BLUECHURCH_THEME2017_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['rohberg.bluechurch.theme2017'])

    def test_product_uninstalled(self):
        """Test if rohberg.bluechurch.theme2017 is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'rohberg.bluechurch.theme2017'))

    def test_browserlayer_removed(self):
        """Test that IRohbergBluechurchTheme2017Layer is removed."""
        from rohberg.bluechurch.theme2017.interfaces import \
            IRohbergBluechurchTheme2017Layer
        from plone.browserlayer import utils
        self.assertNotIn(IRohbergBluechurchTheme2017Layer, utils.registered_layers())
