#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: chschw
# @Date:   2015-01-08 11:24:33
# @Last Modified by:   chschw
# @Last Modified time: 2015-01-09 12:13:40


from ajenti.api import *
from ajenti.plugins import *


info = PluginInfo(
    title='Site monitor',
    icon='globe',
    dependencies=[
        PluginDependency('main'),
        PluginDependency('dashboard'),
        ModuleDependency('httplib2'),
        ModuleDependency('datetime')
    ],
)


def init():
    import widget
