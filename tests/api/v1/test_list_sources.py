# -*- encoding: utf-8 -*-
#
# Copyright © 2012 Julien Danjou
#
# Author: Julien Danjou <julien@danjou.info>
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.
"""Test listing users.
"""

import datetime
import logging

from ceilometer.collector import meter
from ceilometer import counter

from ceilometer.tests import api as tests_api


class TestListSource(tests_api.TestBase):

    def test_source(self):
        ydata = self.get('/sources/test_source')
        self.assert_("somekey" in ydata)
        self.assertEqual(ydata["somekey"], 666)

    def test_unknownsource(self):
        ydata = self.get('/sources/test_source_that_does_not_exist')
        self.assertEqual(ydata, {})
