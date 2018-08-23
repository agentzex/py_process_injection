from optparse import OptionParser
from py_process_injection import inject


def parse_command_line_arguments():
    parser = OptionParser("usage: %prog -p 123 -d 'C:\Users\pc\\bad.dll -i 1\nPlease make sure your injected process is a 32 bit process and your given dll is a 32 bit dll")
    parser.add_option("-p", dest="pid", help="PID of the process to inject")
    parser.add_option("-d", dest="dll_path", help="The path of the dll to inject to the remote process")
    parser.add_option("-i", dest="injection_type", help="Injection type of the chosen dll\n1 - Injecting the path of the dll to memory ( using LoadLibrary() )\n2 - Reflactive injection of the dll binary to memory")
    (options, args) = parser.parse_args()

    if not options.pid or not options.dll_path or not options.injection_type:
        parser.error("one or more arguments are missing")
    if int(options.injection_type) !=1 and int(options.injection_type)!=2:
        parser.error("You must select injection type 1 or 2")

    return int(options.pid), options.dll_path, int(options.injection_type)

if __name__ == "__main__":
    pid, dll_path, injection_type = parse_command_line_arguments()
    ret = inject(pid, dll_path, injection_type)
    print ret
