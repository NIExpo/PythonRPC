import rpyc


HOSTNAME = 'kalyan-ni'
PORT = 18861
connection = rpyc.connect(HOSTNAME, PORT)

print("Importing RTSeq Module")
#from niveristand import run_py_as_rtseq
#from niveristand.errors import RunError
#from niveristand.legacy import NIVeriStand
#from examples.engine_demo.engine_demo_basic import run_engine_demo

#Start accessing Remote Modules
subprocess = connection.root.subprocess
niveristand = connection.root.niveristand
RunError = connection.root.RunError
NIVeriStand = connection.root.NIVeriStand
examples = connection.root.examples
run_engine_demo = connection.root.run_engine_demo
run_py_as_rtseq = connection.root.run_py_as_rtseq

# Ensures NI VeriStand is running.
print("Launching veristand")
#NIVeriStand.LaunchNIVeriStand()

workspace = NIVeriStand.Workspace2('kalyan-ni')
try:
    # Uses Python real-time sequences to run a test.
    #To do: Get this working
    #run_py_as_rtseq(run_engine_demo)
    #print("Finished Deployment of SysDef File")
    #Uses Python real-time sequences to run a test.

    #Get values
    for i in range(100):
        ActualRPM = workspace.GetSingleChannelValue("ActualRPM")
        print("ActualRPM: ", ActualRPM)
except RunError as e:
    print("Test Failed: %d -  %s" % (str(e.error.error_code), e.error.message))
finally:
    # You can now disconnect from the system, so the next test can run.
    print("End of Test")
    #print("Disconnect")
    #workspace.DisconnectFromSystem('', True)