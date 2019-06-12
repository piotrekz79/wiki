<!-- TITLE: 5GinFIRE Contributions -->
<!-- SUBTITLE: A quick summary of 5GinFIRE contributions -->

# Multi-site deployments with OSM R5
## Usage 
The following test describes a procedure to enable the multi-site deployment of network services in OSM Release FIVE, avoiding the utilization of a Wan Infrastructure Manager (WIM). This procedure has been developed in the context of the  [H2020 5GinFIRE project](https://5ginfire.eu).

1)  Create a “dummy WIM” account in the OSM, specifying which VIMs will be used for multi-site deployments. This step is needed because in this type of deployments the RO first verifies the existence of a WIM account with the information about all the involved VIMs; and if it does not exist, the deployment is rejected. This information is defined by the OSM information model and can be provided in a JSON file at the WIM account creation time.
