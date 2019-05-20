#!/usr/bin/env python

"""Script to run tests using `robot.run` API.

Usage: %s path/to/tests.robot
"""

import sys
import shutil
import os
import time
from robot import run, pythonpathsetter

date = time.strftime("%Y%m")

shutil.rmtree('output', ignore_errors=True)
if not os.path.exists('output'):
    os.mkdir('output')

curdir = os.getcwd()
library_dir = os.path.join(curdir, 'resources', 'page_objects')
po_dir = os.path.join(curdir, 'resources', 'libraries', 'python', 'src')

pythonpathsetter.add_path(library_dir, end=True)
pythonpathsetter.add_path(po_dir, end=True)

if len(sys.argv) == 2:
    test_suite = sys.argv[1]
else:
    test_suite = ''

rc = run('test-specification',
         outputdir='output',
         loglevel='TRACE',
         variablefile=('resources/common/variable_file/'
                       'common_variables.py:test'),
         exclude=['ready', 'app'],
         include=test_suite,
         variable=[
             'USERNAME: payam.hossaini@outlook.com',
             'PASSWORD: TestPass123',
         ]
         )

sys.exit(rc)
