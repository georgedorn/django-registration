#find the base.html template that overrides the project one, as urls are also overridden.

import os, sys
TESTS_PATH = os.path.dirname(__file__)
MODULE_PATH = os.path.dirname(TESTS_PATH)
TEST_TEMPLATE_PATH = os.path.join(MODULE_PATH, 'test_templates')
TEST_TEMPLATE_DIRS = (TEST_TEMPLATE_PATH,)


from registration.tests.default_backend import *
from registration.tests.forms import *
from registration.tests.models import *
from registration.tests.simple_backend import *
