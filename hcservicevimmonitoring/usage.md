<!-- TITLE: The 5GinFIRE VIM resources monitoring -->
<!-- SUBTITLE: The 5GinFIRE VIM resources monitoring -->

# The 5GinFIRE VIM resources monitoring

![Hcs Elastic Architecture](/uploads/hcs/hcs-elastic-architecture.png "Hcs Elastic Architecture")

The 5GinFIRE VIM resources monitoring service is a simple service that collects various resource information from VIM components of the 5GinFIRE infrastructure. It enables to retrieve historical data and usage. 
![Hcs Vim Kibana](/uploads/hcs/hcs-vim-kibana.png "Hcs Vim Kibana")


## How it works


VIM components POST a monitoring message towards the [5GinFIRE Healthcheck service (HCS)](hcservice/usage)  to the url:

```text
http://status.5ginfire.eu/hcs/services/api/admin/components/{apikey}/simplemon
```
*apikey* is a unique string for each component. (apikeys for a Component will be given by the HCS admins, see  [5GinFIRE Healthcheck service (HCS)](hcservice/usage))

with payload a JSON like the following:
```text
{"totalSnapshotsUsed": 1, "maxTotalCores": 120, "maxTotalBackups": 10, "totalServerGroupsUsed": 0, "maxPersonalitySize": 10240, "totalInstancesUsed": 14, "totalBackupsUsed": 0, "maxTotalVolumeGigabytes": 5000, "maxServerMeta": 128, "maxTotalBackupGigabytes": 1000, "totalRAMUsed": 83968, "maxTotalVolumes": 50, "totalSecurityGroupsUsed": 1, "totalFloatingIpsUsed": 0, "maxPersonality": 5, "maxImageMeta": 128, "totalCoresUsed": 38, "totalVolumesUsed": 12, "maxServerGroups": 10, "maxSecurityGroups": 10, "maxTotalFloatingIps": 10, "maxTotalInstances": 50, "totalBackupGigabytesUsed": 0, "maxTotalSnapshots": 50, "maxSecurityGroupRules": 20, "maxTotalKeypairs": 100, "maxServerGroupMembers": 10, "maxTotalRAMSize": 256200, "totalGigabytesUsed": 662}
```


## Example implementation for Openstack as VIM



The following apply only to Openstack as VIM. However it can be adjusted for other VIMs.
Openstack provides some usage metrics for a tenant via the follwoing example:


```text
localadmin@controller:~$ source admin-rc
localadmin@controller:~$ openstack limits show --absolute
+--------------------------+--------+
| Name                     |  Value |
+--------------------------+--------+
| maxServerMeta            |    128 |
| maxTotalInstances        |     50 |
| maxPersonality           |      5 |
| totalServerGroupsUsed    |      0 |
| maxImageMeta             |    128 |
| maxPersonalitySize       |  10240 |
| maxTotalRAMSize          | 256200 |
| maxServerGroups          |     10 |
| maxSecurityGroupRules    |     20 |
| maxTotalKeypairs         |    100 |
| totalCoresUsed           |     38 |
| totalRAMUsed             |  83968 |
| maxSecurityGroups        |     10 |
| totalFloatingIpsUsed     |      0 |
| totalInstancesUsed       |     14 |
| maxServerGroupMembers    |     10 |
| maxTotalFloatingIps      |     10 |
| totalSecurityGroupsUsed  |      1 |
| maxTotalCores            |    120 |
| totalSnapshotsUsed       |      1 |
| maxTotalBackups          |     10 |
| maxTotalVolumeGigabytes  |   5000 |
| maxTotalSnapshots        |     50 |
| maxTotalBackupGigabytes  |   1000 |
| totalBackupGigabytesUsed |      0 |
| maxTotalVolumes          |     50 |
| totalVolumesUsed         |     12 |
| totalBackupsUsed         |      0 |
| totalGigabytesUsed       |    662 |
+--------------------------+--------+
```

Note: admin-rc file contains some tenant information for example:  OS_USER_DOMAIN_NAME, OS_PROJECT_NAME, OS_USERNAME, OS_PASSWORD, etc. as used for the openstack command



