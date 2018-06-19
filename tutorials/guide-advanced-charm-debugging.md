# Guide: Advanced Charm Debugging

This tutorial gives some pointers on how to debug proxy charms used in OSM.

## Handling exceptions

When writing an action, exceptions should be handled. The bare minimum that will save a lot of time for developers and testers is writing the exception into the action output. In the next example it is possible to see how to redirect the exception info to the action output.

~~~~python
@when('actions.config')
def configurate():
    try:
        cmd = 'sudo su -c "/root/configurate.sh"'
        result, _ = charms.sshproxy._run(cmd)
    except:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        err = traceback.format_exception(exc_type, exc_value, exc_traceback)
        action_fail('configuration failed:' + str(err))
    else:
        action_set({'output': result})
    finally:
        remove_flag('actions.config')
~~~~

In this example it is shown an action that runs a configuration script as root. In case any exception is raised, its informations and values can be checked in the output of the action.

## Checking status of the charms

Another trick that can be used is running the following command:

~~~~bash
juju status
~~~~

This command will show all the running chams inside the VCA. This command is important to check in which state the charm is and if it stopped or if it malfunctioned.

## Checking the status of an action

After issuing an action to be performed by OSM, there might be a need to check it status if the UI doesn't update. To do this, the following command can be run:

~~~~bash
juju show-action-status --name <action-name>
~~~~

It shows every action with that action, plus the ID, timestamp and result.

## Checking the output of an action

In case an error occurred and there is a need to check the exception/error code that was writen into the output. To check the output, run the following command in the VCA:

~~~~bash
juju show-action-output <action-id>
~~~~

It will show the output, so this is another reason to output the exceptions into the **action_fail()** function.

## Running the charm manually

To run the code of the charm manually, use the following command:

~~~~bash
juju debug-hooks <unit-name>
~~~~

Note: check the **unit-name** using **juju status**.

When running the charms in manual mode, you must run all commands by hand like connect to the VDU using ssh, retrieve the configuration parameters, among other things.
