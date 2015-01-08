#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: chschw
# @Date:   2015-01-08 11:24:33
# @Last Modified by:   chschw
# @Last Modified time: 2015-01-08 14:43:05


from ajenti.api import *
from ajenti.plugins import *


info = PluginInfo(
    title='Site monitor',
    icon='fa-globe',
    dependencies=[
        PluginDependency('main'),
        PluginDependency('dashboard'),
        ModuleDependency('httplib2')
    ],
)


def init():
    import widget
