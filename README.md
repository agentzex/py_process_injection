# py_process_injection
<pre>
Python windows dll process injection wrapper

-p PID             PID of the process to inject
-d DLL_PATH        The path of the dll to inject to the remote process
-i INJECTION_TYPE  Injection type of the chosen dll:
                       1 - Injecting the path of the dll to memory ( using LoadLibrary() ) 
                       2 - Reflective injection of the dll binary to memory


Usage: python proc_inject.py -p "pid" -d "dll_path" -i 2

Example: python proc_inject.py -p 7636 -d C:\Users\myuser\\bad.dll -i 2
</pre>
