# coding: utf-8
'''Apport package hook for Deepin Cloud Printer

   COPYRIGHT © 2003-2011 Martin-Éric Racine <martin-eric.racine@iki.fi>

   LICENSE
   This package is free software; you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation, either version 2 of the License or (at
   your option) any later version.
'''

from apport.hookutils import *

def add_info(report):
    attach_printing(report)
