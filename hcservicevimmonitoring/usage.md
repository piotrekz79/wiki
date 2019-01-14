<!-- TITLE: The 5GinFIRE VIM resources monitoring -->
<!-- SUBTITLE: The 5GinFIRE VIM resources monitoring -->

# The 5GinFIRE VIM resources monitoring
The 5GinFIRE VIM resources monitoring service is a simple service that collects various resource information from VIM components of the 5GinFIRE infrastructure. It enables to retrieve historical data and usage. 
VIM components POST a monitoring message towards the [5GinFIRE Healthcheck service (HCS)](hcservice/usage)

![Hcs Elastic Architecture](/uploads/hcs/hcs-elastic-architecture.png "Hcs Elastic Architecture")

Results can be visualized through Kibana:

![Hcs Vim Kibana](/uploads/hcs/hcs-vim-kibana.png "Hcs Vim Kibana")


## How it works


VIM components POST a monitoring message towards the [5GinFIRE Healthcheck service (HCS)](http://wiki.5ginfire.eu/hcservice/usage)  to the url:

```text
http://status.5ginfire.eu/hcs/services/api/admin/components/{apikey}/simplemon
```
*apikey* is a unique string for each component. (apikeys for a Component will be given by the HCS admins, see  [5GinFIRE Healthcheck service (HCS)](http://wiki.5ginfire.eu/hcservice/usage))

with payload a JSON like the following:
```text
{
  "maxTotalCores": 120,
  "totalInstancesUsed": 14,
  "maxTotalVolumeGigabytes": 5000,
  "maxTotalBackupGigabytes": 1000,
  "totalRAMUsed": 83968,
  "maxTotalVolumes": 50,
  "totalCoresUsed": 38,
  "totalVolumesUsed": 12,
  "maxServerGroupMembers": 10,
  "maxTotalRAMSize": 256200,
  "totalGigabytesUsed": 662,
	...
	...
}
```


## Example implementation for Openstack as VIM


The following applies only to Openstack as VIM. However it can be adjusted for other VIMs.
Openstack provides some usage metrics for a tenant via the following example:


```text
user@controller:~$ source admin-rc
user@controller:~$ openstack limits show --absolute
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


Create a python file called for example **VIMStatusParser.py**:

```python
#!/usr/bin/python
import json
import sys

lines= sys.stdin
json_dict = dict()

for line in sys.stdin:
  items = line.split("|")
  # Get the second and fourth element
  if len(items)>3 and("Value" not in items[2]) :
     val = items[2].strip()
     json_dict[ items[1].strip() ] = int(val)

print(json.dumps(json_dict))

```


Create a file called **sendVIMStats.sh** :


```batchfile
#!/bin/bash
cd "$(dirname "$0")"

source admin-rc
openstack limits show --absolute | python VIMStatusParser.py | curl -XPOST 'http://status.5ginfire.eu/hcs/services/api/admin/components/53f7118f-xxxx-xxxx-xxxxx-xxxxxxxxxx/simplemon' -H 'Content-Type: application/json' -d @-
```


Finally schedule the script to post monitoring results every hour in crontab like the following example:

```batchfile
0 * * * * /home/user/sendVIMStats.sh
```






