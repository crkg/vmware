import ssl
import atexit
import sys
import time
from pyVmomi import vim, vmodl
from pyVim import connect, task
from pyVim.connect import Disconnect

context = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
context.verify_mode = ssl.CERT_NONE
srv_inst = connect.SmartConnect(host='vcsa-01a.corp.local', user='administrator@corp.local', pwd='VMware1!', port=443, sslContext= context)
content = srv_inst.RetrieveContent()


def get_obj(content, vimtype, name):
    obj = None
    container = content.viewManager.CreateContainerView(
        content.rootFolder, vimtype, True)
    for c in container.view:
        if name:
            if c.name == name:
                obj = c
                break
        else:
            obj = c
            break
	return obj
	
dvs = get_obj(content, [vim.DistributedVirtualSwitch], 'vdswitch_name')
selection_set = []
dvs_ss = vim.dvs.DistributedVirtualPortgroupSelection()
dvs_ss.dvsUuid = dvs.uuid
for pg in dvs.portgroup:
	dvs_ss.portgroupKey.append(pg.key)
selection_set.append(dvs_ss)
bkp = content.dvSwitchManager.DVSManagerExportEntity_Task(selection_set)


from pyVmomi.VmomiSupport import VmomiJSONEncoder

Use this to create your list:
jsonSerialized= json.dumps(pfVmomiObj, cls=VmomiJSONEncoder)

Then in the mapped function, use this to recover the object:
pfVmomiObj = json.loads(jsonSerialized)
