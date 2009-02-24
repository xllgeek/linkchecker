# -*- coding: iso-8859-1 -*-
# Copyright (C) 2000-2009 Bastian Kleineidam
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.
"""
Store metadata and options.
"""

import sys
import os
import logging.config
import urllib
import _LinkChecker_configdata as configdata
from .. import log, LOG_CHECK, LOG, ansicolor, lognames, clamav, get_config_dir
from . import confparse

Version = configdata.version
AppName = configdata.appname
App = AppName+u" "+Version
Author =  configdata.author
HtmlAuthor = Author.replace(u' ', u'&nbsp;')
Copyright = u"Copyright (C) 2000-2009 "+Author
HtmlCopyright = u"Copyright &copy; 2000-2009 "+HtmlAuthor
AppInfo = App+u"              "+Copyright
HtmlAppInfo = App+u", "+HtmlCopyright
Url = configdata.url
Email = configdata.author_email
UserAgent = u"%s/%s (+%s)" % (AppName, Version, Url)
Freeware = AppName+u""" comes with ABSOLUTELY NO WARRANTY!
This is free software, and you are welcome to redistribute it
under certain conditions. Look at the file `LICENSE' within this
distribution."""


def normpath (path):
    """
    Norm given system path with all available norm funcs in os.path.
    """
    return os.path.normcase(os.path.normpath(os.path.expanduser(path)))


# dynamic options
class Configuration (dict):
    """
    Storage for configuration options. Options can both be given from
    the command line as well as from configuration files.
    """

    def __init__ (self):
        """
        Initialize the default options.
        """
        super(Configuration, self).__init__()
        self['trace'] = False
        self["verbose"] = False
        self["complete"] = False
        self["warnings"] = True
        self["ignorewarnings"] = []
        self['quiet'] = False
        self["anchors"] = False
        self["anchorcaching"] = True
        self["externlinks"] = []
        self["internlinks"] = []
        self["noproxyfor"] = []
        self["interactive"] = False
        # on ftp, password is set by Pythons ftplib
        self["authentication"] = []
        self["proxy"] = urllib.getproxies()
        self["recursionlevel"] = -1
        self["wait"] = 0
        self['sendcookies'] = False
        self['storecookies'] = False
        self["status"] = False
        self["fileoutput"] = []
        # Logger configurations
        self["text"] = {
            "filename": "linkchecker-out.txt",
            'colorparent':  "default",
            'colorurl':     "default",
            'colorname':    "default",
            'colorreal':    "cyan",
            'colorbase':    "purple",
            'colorvalid':   "bold;green",
            'colorinvalid': "bold;red",
            'colorinfo':    "default",
            'colorwarning': "bold;yellow",
            'colordltime':  "default",
            'colordlsize':  "default",
            'colorreset':   "default",
        }
        self['html'] = {
            "filename":        "linkchecker-out.html",
            'colorbackground': '#fff7e5',
            'colorurl':        '#dcd5cf',
            'colorborder':     '#000000',
            'colorlink':       '#191c83',
            'colorwarning':    '#e0954e',
            'colorerror':      '#db4930',
            'colorok':         '#3ba557',
        }
        self['gml'] = {
            "filename": "linkchecker-out.gml",
        }
        self['sql'] = {
            "filename": "linkchecker-out.sql",
            'separator': ';',
            'dbname': 'linksdb',
        }
        self['csv'] = {
            "filename": "linkchecker-out.csv",
            'separator': ',',
            "quotechar": '"',
        }
        self['blacklist'] = {
            "filename": "~/.linkchecker/blacklist",
        }
        self['xml'] = {
            "filename": "linkchecker-out.xml",
        }
        self['gxml'] = {
            "filename": "linkchecker-out.gxml",
        }
        self['dot'] = {
            "filename": "linkchecker-out.dot",
            "encoding": "ascii",
        }
        self['none'] = {}
        self['output'] = 'text'
        self['logger'] = None
        self["warningregex"] = None
        self["warnsizebytes"] = None
        self["nntpserver"] = os.environ.get("NNTP_SERVER", None)
        self["threads"] = 10
        # socket timeout in seconds
        self["timeout"] = 60
        self["checkhtml"] = False
        self["checkcss"] = False
        self["checkhtmlw3"] = False
        self["checkcssw3"] = False
        self["scanvirus"] = False
        self["clamavconf"] = clamav.canonical_clamav_conf()

    def init_logging (self, status_logger, debug=None, handler=None):
        """
        Load logging.conf file settings to set up the
        application logging (not to be confused with check loggers).
        When debug is not None it is expected to be a list of
        logger names for which debugging will be enabled.

        If no thread debugging is enabled, threading will be disabled.
        """
        filename = normpath(os.path.join(get_config_dir(), "logging.conf"))
        if os.path.isfile(filename):
            logging.config.fileConfig(filename)
        if handler is None:
            handler = ansicolor.ColoredStreamHandler(strm=sys.stderr)
        handler.setFormatter(logging.Formatter("%(levelname)s %(message)s"))
        logging.getLogger(LOG).addHandler(handler)
        self.set_debug(debug)
        self.status_logger = status_logger

    def set_debug (self, debug):
        """Set debugging levels for configured loggers. The argument
        is a list of logger names to enable debug for."""
        if not debug:
            return
        # set debugging on given logger names
        if 'all' in debug:
            debug = lognames.keys()
        # disable threading if no thread debugging
        if "thread" not in debug:
            self['threads'] = 0
        for name in debug:
            logname = lognames[name]
            logging.getLogger(logname).setLevel(logging.DEBUG)

    def logger_new (self, loggertype, **kwargs):
        """
        Instantiate new logger and return it.
        """
        args = {}
        args.update(self[loggertype])
        args.update(kwargs)
        from ..logger import Loggers
        return Loggers[loggertype](**args)

    def logger_add (self, loggertype, loggerclass, loggerargs=None):
        """
        Add a new logger type to the known loggers.
        """
        if loggerargs is None:
            loggerargs = {}
        from ..logger import Loggers
        Loggers[loggertype] = loggerclass
        self[loggertype] = loggerargs

    def read (self, files=None):
        """
        Read settings from given config files.

        @raises: LinkCheckerError on syntax errors in the config file(s)
        """
        if files is None:
            cfiles = []
        else:
            cfiles = files[:]
        if not cfiles:
            # system wide config settings
            path = normpath(os.path.join(get_config_dir(), "linkcheckerrc"))
            cfiles.append(path)
            # per user config settings
            path = normpath("~/.linkchecker/linkcheckerrc")
            cfiles.append(path)
        # weed out invalid files
        cfiles = [f for f in cfiles if os.path.isfile(f)]
        log.debug(LOG_CHECK, "reading configuration from %s", cfiles)
        confparse.LCConfigParser(self).read(cfiles)
        self.sanitize()

    def sanitize (self):
        "Make sure the configuration is consistent."
        if self["anchors"]:
            if not self["warnings"]:
                self["warnings"] = True
                from ..checker import Warnings
                self["ignorewarnings"] = Warnings.keys()
            if 'url-anchor-not-found' in self["ignorewarnings"]:
                self["ignorewarnings"].remove('url-anchor-not-found')
        self['logger'] = self.logger_new(self['output'])
        if self['checkhtml']:
            try:
                import tidy
            except ImportError:
                log.warn(LOG_CHECK,
                    _("warning: tidy module is not available; " \
                     "download from http://utidylib.berlios.de/"))
                self['checkhtml'] = False
        if self['checkcss']:
            try:
                import cssutils
            except ImportError:
                log.warn(LOG_CHECK,
                    _("warning: cssutils module is not available; " \
                     "download from http://cthedot.de/cssutils/"))
                self['checkcss'] = False
        if self['scanvirus']:
            try:
                clamav.init_clamav_conf(self['clamavconf'])
            except clamav.ClamavError:
                self['scanvirus'] = False
