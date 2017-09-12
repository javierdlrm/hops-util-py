"""
Utility functions to retrieve information about available services and setting up security for the Hops platform.

These utils facilitates development by hiding complexity for programs interacting with Hops services.
"""

import socket
import subprocess
import os
import pydoop.hdfs as hdfs

pdir = os.getcwd()
logpath = pdir + "/events"
os.makedirs(logpath)
logdir = os.path.dirname(logpath)

def register():

    pypath = os.getenv("PYSPARK_PYTHON")
    pydir = os.path.dirname(pypath)

    #find free port
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('',0))
    addr, port = s.getsockname()
    s.close()

    subprocess.Popen([pypath, "%s/tensorboard"%pydir, "--logdir=%s"%logdir, "--port=%d"%port, "--debug"])
    host = socket.gethostname()
    tb_url = "http://{0}:{1}".format(host, port)

    #dump tb host:port to hdfs
    hdfs.dump(tb_url, hdfs.project_path() + "/Jupyter/.jupyter.tensorboard", user=hdfs.project_user())


def get_logdir():
    return logdir
