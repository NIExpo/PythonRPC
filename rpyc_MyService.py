import rpyc
import niveristand
import examples
from niveristand.legacy import NIVeriStand
from examples.engine_demo.engine_demo_basic import run_engine_demo
from niveristand import run_py_as_rtseq
from niveristand.errors import RunError
import subprocess

class MyService(rpyc.Service):
   exposed_niveristand = niveristand
   exposed_examples = examples
   exposed_RunError = niveristand.errors.RunError
   exposed_NIVeriStand = NIVeriStand
   exposed_subprocess = subprocess
   exposed_run_engine_demo = run_engine_demo
   exposed_run_py_as_rtseq = run_py_as_rtseq
   exposed_RunError = RunError
   
if __name__ == "__main__":
   from rpyc.utils.server import ThreadedServer
   t = ThreadedServer(MyService, port = 18861, protocol_config = {"allow_public_attrs" : True, "allow_all_attrs" : True})
   print("Starting the RPC Service")
   t.start()