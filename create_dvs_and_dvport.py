#Create vdswitch input ; datacenter_name:'From form' vdswitch_name ' from form '
def create_vdswitch(content, datacenter_name, vdswitch_name):
	vdswitch_name = vdswitch_name+'-NEW'
	datacenter = get_obj(content, [vim.Datacenter], datacenter_name)
		if datacenter:
			spec = vim.DistributedVirtualSwitch.CreateSpec()
			spec.configSpec = vim.DistributedVirtualSwitch.ConfigSpec(name=vdswitch_name)
			task = datacenter.networkFolder.CreateDistributedVirtualSwitch(spec)
			pyVim.task.WaitForTask(task)
			#vdswitch_mo = task.info.result
			print("Created Distributed Switch '{}' ({})".format(vdswitch_name, vdswitch_mo._moId))
    return vdswitch_mo._moId, vdswitch_name

### Create Distributed Switch portgroup
# Input : vdswitch_name :  'new name' , vdportgroup_name : ' old name from form';
def create_vdportgroup(content, vdswitch_name, ):
	dvs = get_obj(content, [vim.DistributedVirtualSwitch], vdswitch_name)
	dvsconfig = dvs.config
	portGroups = dvsconfig.uplinkPortgroup
	for portgroup in portGroups:
		vdportgroup_name = portgroup.name
		vdportgroup_name = vdportgroup_name+'-NEW'
		vdportgroup_type = "earlyBinding"
		vdportgroup_spec = vim.dvs.DistributedVirtualPortgroup.ConfigSpec(name=vdportgroup_name, type=vdportgroup_type)
		vdportgroup_specs = [vdportgroup_spec]
		task = vdswitch_mo.AddPortgroups(vdportgroup_specs)
		pyVim.task.WaitForTask(task)
		vdportgroup = None
    for vdportgroup_mo in vdswitch_mo.portgroup:
        if vdportgroup_mo.name == vdportgroup_name:
            vdportgroup = vdportgroup_mo._moId
            print(
                "Created Distributed Portgroup '{}' ({}) on Distributed Switch '{}' ({})".
                format(vdportgroup_name, vdportgroup, vdswitch_name, vdswitch))
    return vdportgroup

def fetch_vds_config(content,vdswitch_name):
	dvs = get_obj(content, [vim.DistributedVirtualSwitch], vdswitch_name)
	dvsconfig = dvs.config
	portGroup = dvsconfi.uplinkPortgroup
	
	

def get_obj(content, vimtype, name):
    obj = None
    container = content.viewManager.CreateContainerView(
        content.rootFolder, vimtype, True
    )
    for c in container.view:
        if c.name.upper() == name.upper():
            obj = c
            break
    return obj

def find_vdswitch(content, datacenter_name, vdswitch_name):
    for datacenter_mo in content.rootFolder.childEntity:
        if (isinstance(datacenter_mo, vim.Datacenter) and
                    datacenter_mo.name == datacenter_name):
            for vdswitch_mo in datacenter_mo.networkFolder.childEntity:
                if (isinstance(vdswitch_mo, vim.DistributedVirtualSwitch) and
                            vdswitch_mo.summary.name == vdswitch_name):
                    print("Found VDSwitch '{}' ({}) in Datacenter '{}' ({})".
                          format(vdswitch_name, vdswitch_mo._moId,
                                 datacenter_name, datacenter_mo._moId))
                    return vdswitch_mo
    return None
	
def find_vdportgroup_vdswitch(content,datacenter_name,vdswitch_name):
	vdswitch_mo = find_vdswitch(content,datacenter_name,vdswitch_name)
	if not vdswitch_mo:
		return "Swtich not found"
	vdportgroup_list = [vdportgroup_mo for vdportgroup_mo in vdswitch_mo.portgroup if vdportgroup_mo]
	return vdportgroup_list
