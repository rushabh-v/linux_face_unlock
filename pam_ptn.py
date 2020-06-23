import execnet
import os

def call_python_version(Version, Module, Function, ArgumentList):
    gw      = execnet.makegateway("popen//python=python%s" % Version)
    channel = gw.remote_exec("""
        from %s import %s as the_function
        channel.send(the_function(*channel.receive()))
    """ % (Module, Function))
    channel.send(ArgumentList)
    return  channel.receive()

def pam_sm_authenticate(pamh, flags, args):
    print "facerec running.."
    os.chdir("/lib/Auth/RecFace/")
    try:
        if call_python_version("3", "compare", "authenticate", []):
            return pamh.PAM_SUCCESS
        else:
            return pamh.PAM_SYSTEM_ERR
    except Exception as e:
        print(e)


def pam_sm_open_session(pamh, flags, args):
    print "facerec running.."
    os.chdir("/lib/Auth/RecFace/")
    try:
        if call_python_version("3", "compare", "authenticate", []):
            return pamh.PAM_SUCCESS
        else:
            return pamh.PAM_SYSTEM_ERR
    except Exception as e:
        print(e)

def pam_sm_close_session(pamh, flags, argv):
    return pamh.PAM_SUCCESS

def pam_sm_setcred(pamh, flags, argv):
    return pamh.PAM_SUCCESS
