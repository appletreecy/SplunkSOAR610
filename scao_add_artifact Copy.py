"""

"""


import phantom.rules as phantom
import json
from datetime import datetime, timedelta


@phantom.playbook_block()
def on_start(container):
    phantom.debug('on_start() called')

    # call 'code_1' block
    code_1(container=container)

    return

@phantom.playbook_block()
def code_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("code_1() called")

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...
    for i in range(2100):
        raw = {}
        cef = {}
        cef['sourceAddress'] = '1.1.1.1'
    

        success, message, artifact_id = phantom.add_artifact(
        container=container, raw_data=raw, cef_data=cef, label='netflow',
        name='test_event', severity='high',
        identifier=None,
        artifact_type='network')

    ################################################################################
    ## Custom Code End
    ################################################################################

    return


@phantom.playbook_block()
def on_finish(container, summary):
    phantom.debug("on_finish() called")

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    return