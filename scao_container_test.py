"""

"""


import phantom.rules as phantom
import json
from datetime import datetime, timedelta


@phantom.playbook_block()
def on_start(container):
    phantom.debug('on_start() called')

    # call 'container_update_2' block
    container_update_2(container=container)

    return

@phantom.playbook_block()
def container_update_2(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("container_update_2() called")

    parameters = []

    parameters.append({
        "container_input": 1,
        "name": None,
        "description": None,
        "label": None,
        "owner": None,
        "sensitivity": None,
        "severity": None,
        "status": "Closed",
        "tags": None,
        "input_json": None,
    })

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.custom_function(custom_function="community/container_update", parameters=parameters, name="container_update_2")

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