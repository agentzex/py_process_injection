from optparse import OptionParser
from py_process_injection import inject


def parse_command_line_arguments():
    parser = OptionParser("usage: %prog -p 123 -d 'C:\Users\pc\\bad.dll\nPlease make sure your injected process is a 32 bit process and your given dll is a 32 bit dll")
    parser.add_option("-p", dest="pid", help="PID of the process to inject")
    parser.add_option("-d", dest="dll_path", help="The path of the dll to inject to the remote process")
    (options, args) = parser.parse_args()

    if not options.pid or not options.dll_path:
        parser.error("one or more arguments are missing")

    return int(options.pid), options.dll_path

if __name__ == "__main__":
    pid, dll_path = parse_command_line_arguments()
    ret = inject(pid, dll_path)
    print ret
