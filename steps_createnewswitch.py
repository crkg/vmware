allpgs = [item for item in content.viewManager.CreateContainerView(content.rootFolder, [vim.DistributedVirtualPortgroup], True).view]
config_out = json.dumps(config, cls=VmomiJSONEncoder)
cout1=copy.deepcopy(config_out)
myconfig_obj = json.loads(config_out, cls=MyJSONDecoder)
dvs_hostonfig = dvs.config_configs = []
dvs_create_spec = vim.DistributedVirtualSwitch.CreateSpec()
dvs_config_spec = vim.DistributedVirtualSwitch.ConfigSpec()
dvs_config_spec.name = myconfig_obj.name+'-New'
dvs_config_spec.uplinkPortPolicy=myconfig_obj.uplinkPortPolicy
dvs_config_spec.maxPorts = myconfig_obj.maxPorts
for host in myconfig_obj.host:
    dvs_host_config = vim.dvs.HostMember.ConfigSpec()
    dvs_host_config.operation = vim.ConfigSpecOperation.add
    dvs_host_config.host = host.config.host
    dvs_host_config.backing = host.config.backing
    dvs_host_config.maxProxySwitchPorts = host.config.maxProxySwitchPorts
    dvs_host_config.vendorSpecificConfig = host.config.vendorSpecificConfig
    dvs_host_configs.append(dvs_host_config)
dvs_config_spec.host = dvs_host_configs
dvs_config_spec.configVersion = myconfig_obj.configVersion
myconfig_obj.numStandalonePorts = myconfig_obj.numStandalonePorts
dvs_config_spec.numStandalonePorts = myconfig_obj.numStandalonePorts
dvs_config_spec.defaultPortConfig = myconfig_obj.defaultPortConfig
# dvs_config_spec.uplinkPortgroup = myconfig_obj.uplinkPortgroup
# dvs_config_spec.uplinkPortgroup = myconfig_obj.uplinkPortgroup
# dvs_config_spec.uplinkPortgroup = GetVmodlType('vim.dvs.DistributedVirtualPortgroup[]')()
dvs_config_spec.extensionKey = myconfig_obj.extensionKey
dvs_config_spec.description = myconfig_obj.description
dvs_config_spec.policy = myconfig_obj.policy
dvs_config_spec.vendorSpecificConfig = myconfig_obj.vendorSpecificConfig
dvs_config_spec.contact = myconfig_obj.contact
dvs_config_spec.switchIpAddress = myconfig_obj.switchIpAddress
dvs_config_spec.defaultProxySwitchMaxNumPorts = myconfig_obj.defaultProxySwitchMaxNumPorts
dvs_config_spec.infrastructureTrafficResourceConfig = myconfig_obj.infrastructureTrafficResourceConfig
dvs_config_spec.networkResourceControlVersion = myconfig_obj.networkResourceControlVersion
dvs_create_spec.capability
dvs_create_spec = vim.DistributedVirtualSwitch.CreateSpec()
dvs_create_spec.productInfo = myconfig_obj.productInfo
dvs_create_spec.configSpec = dvs_config_spec
