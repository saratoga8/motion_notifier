from behave import *

use_step_matcher("re")


@when("user schedules a recurrent action")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: When user schedules a recurrent action')