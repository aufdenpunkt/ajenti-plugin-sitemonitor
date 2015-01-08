#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: chschw
# @Date:   2015-01-08 11:24:33
# @Last Modified by:   chschw
# @Last Modified time: 2015-01-08 14:44:45


import httplib2
from ajenti.api import plugin
from ajenti.plugins.dashboard.api import ConfigurableWidget


@plugin
class SiteMonitorWidget(ConfigurableWidget):
    name = _('Site monitor')
    icon = 'globe'


    def on_prepare(self):
        self.append(self.ui.inflate('sitemonitor:site-widget'))


    def on_start(self):
        self.find('website').text = self.config['website']

        status = 'minus-square' # minus-square or check-square

        h = httplib2.Http(".cache")
        response, content = h.request(self.config['website'], "GET")

        self.find('status').icon = status


    def create_config(self):
        return {'website': ''}


    def on_config_start(self):
        pass


    def on_config_save(self):
        self.config['website'] = self.dialog.find('website').value
