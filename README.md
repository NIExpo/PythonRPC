# PythonRPC

1.   Copy Veristand_manualconnection.py to Mac [#Machinne 1] (I was running this on another Windows Machine in my case)
2.   Copy rpyc_MyService.py to Windows connected to RT machine [#Machine 2]
3.   This third step is an artifact of how Veristand examples are written. For your actual application, you won’t need this. Copy Veristand Engine Basic Demo Python examples to the folder where rpyc_MyService.py runs on your Windows machine connected to RT. The examples folder would contain legacy_mix.py, basic_example.py files and engine_demo folder
3.	Open Veristand on #Machine 1, deploy system definition file
4.	Run rpyc_MyService.py
5.	Finally, run Veristand_manual.py
6.	At this point, you should read RPM from remote machine
