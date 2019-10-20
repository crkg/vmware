dvs_host_configs = []
pnic_specs=[]
dvs_create_spec = vim.DistributedVirtualSwitch.CreateSpec()
dvs_config_spec = vim.DistributedVirtualSwitch.ConfigSpec()
dvs_config_spec.name = config.name+'-New'
dvs_config_spec.uplinkPortPolicy=config.uplinkPortPolicy
dvs_config_spec.maxPorts = config.maxPorts
for host in config.host:
    dvs_host_config = vim.dvs.HostMember.ConfigSpec()
    dvs_host_config.operation = vim.ConfigSpecOperation.add
    dvs_host_config.host = host.config.host
    dvs_host_config.backing = host.config.backing
    pnic_spec = vim.dvs.HostMember.PnicSpec()
    pnic_spec.pnicDevice='vmnic1'
    pnic_specs.append(pnic_spec)
    dvs_host_config.backing.pnicSpec = pnic_specs
    dvs_host_config.maxProxySwitchPorts = host.config.maxProxySwitchPorts
    dvs_host_config.vendorSpecificConfig = host.config.vendorSpecificConfig
    dvs_host_configs.append(dvs_host_config)
dvs_config_spec.host = dvs_host_configs
dvs_config_spec.uplinkPortgroup = config.uplinkPortgroup
dvs_config_spec.configVersion = config.configVersion
config.numStandalonePorts = config.numStandalonePorts
dvs_config_spec.numStandalonePorts = config.numStandalonePorts
dvs_config_spec.extensionKey = config.extensionKey
dvs_config_spec.description = config.description
dvs_config_spec.policy = config.policy
dvs_config_spec.vendorSpecificConfig = config.vendorSpecificConfig
dvs_config_spec.contact = config.contact
dvs_config_spec.switchIpAddress = config.switchIpAddress
dvs_config_spec.defaultProxySwitchMaxNumPorts = config.defaultProxySwitchMaxNumPorts
dvs_config_spec.infrastructureTrafficResourceConfig = config.infrastructureTrafficResourceConfig
dvs_config_spec.networkResourceControlVersion = config.networkResourceControlVersion
dvs_create_spec.capability
dvs_create_spec = vim.DistributedVirtualSwitch.CreateSpec()
dvs_create_spec.productInfo = config.productInfo
dvs_create_spec.configSpec = dvs_config_spec
