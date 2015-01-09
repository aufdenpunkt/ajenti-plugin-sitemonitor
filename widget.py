#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: chschw
# @Date:   2015-01-08 11:24:33
# @Last Modified by:   chschw
# @Last Modified time: 2015-01-08 14:44:45


from ajenti.api import plugin
from ajenti.plugins.dashboard.api import ConfigurableWidget


@plugin
class SiteMonitorWidget (ConfigurableWidget):
    name = _('Site monitor')
    icon = 'globe'

    def on_prepare(self):
        self.append(self.ui.inflate('sitemonitor:site-widget'))

    def on_start(self):
        self.find('website').text = self.config['website']
        status='ban-circle' # ok / remove

        if self.config['website'] != '':
            import httplib2
            h = httplib2.Http(".cache")

            try:
                valid_status = [200, 301, 302] 
                resp, content = h.request('http://' + self.config['website'])
                print resp.status
                if resp.status in valid_status:
                    status = 'ok-sign'
            except:
                pass

        self.find('status').icon = status

    def create_config(self):
        return {'website': ''}

    def on_config_start(self):
        pass

    def on_config_save(self):
        self.config['website'] = self.dialog.find('website').value
