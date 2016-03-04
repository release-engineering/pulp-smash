# coding=utf-8
"""Tests for the RPM plugin that should only run internally.

This module is a skeleton that shows how to write tests that only execute
internally. Don't merge this code into the master branch.
"""
from __future__ import unicode_literals

import unittest2

from pulp_smash import utils


def setUpModule():  # pylint:disable=invalid-name
    """Skip tests if Pulp Smash is not on the internal network."""
    if not utils.is_internal():
        raise unittest2.SkipTest(
            'These tests require Pulp Smash to be on the internal network.'
        )


class DemoTestCase(unittest2.TestCase):
    """Demonstrate nothing at all, really."""

    def test_noop(self):
        """A test method must exist, or the module is skipped."""
