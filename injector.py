from py_process_injection import inject
import os
import psutil


def inject_dll(pid, dll_path, injection_type):
    try:
        dll_path = str(dll_path)
    except Exception , e:
        raise Exception("path for dll is not a string\n" + str(e))
    if not os.path.exists(dll_path):
        raise Exception("The given dll path doesn't exist on the system. Please make sure the path you've entered is correct")

    if not isinstance(pid, int):
        raise Exception("The PID given must be an int, not a string")
    c = psutil.process_iter()
    process_found = False
    for process in c:
        if process.pid == pid:
            process_found = True
            break
    if not process_found:
        raise Exception("The PID given is not running on this machine")

    if not isinstance(injection_type, int):
        raise Exception("The injection type given must be an int, not a string")
    if injection_type !=1 and injection_type !=2:
        raise Exception("Injection type given must be 1 or 2 as an int")

    ret = inject(pid, dll_path, injection_type)
    return ret
