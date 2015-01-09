#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: chschw
# @Date:   2015-01-08 11:24:33
# @Last Modified by:   chschw
# @Last Modified time: 2015-01-09 12:47:43


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

        # Default value is Error
        status='ban-circle' # Icons: ok-sign (Success) / ban-circle (Error)
        p = 'http'

        if self.config['protocoll'] is True:
            self.find('type').icon = 'key'
            p = 'https'

        # If website url is given
        if self.config['website'] != '':
            import httplib2
            import datetime

            h = httplib2.Http(".cache")
            time = datetime.datetime.now().strftime('%d.%m.%Y at %H:%M:%S')

            # Try to make an request to website
            try:
                valid_status = [200, 301, 302]
                resp, content = h.request(p + '://' + self.config['website'])

                # If website is available has a valid status
                if resp.status in valid_status:
                    status = 'ok-sign'
            except:
                pass

        # Write icon in context
        self.find('status').icon = status
        self.find('checkdate').text = 'Last check on ' + time

    def create_config(self):
        return {
            'website': '',
            'protocoll': False
            }

    def on_config_start(self):
        self.dialog.find('website').value = self.config.get('website', '')
        self.dialog.find('protocoll').value = self.config.get('protocoll', False)

    def on_config_save(self):
        self.config['website'] = self.dialog.find('website').value
        self.config['protocoll'] = self.dialog.find('protocoll').value

