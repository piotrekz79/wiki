<!-- TITLE: 5GinFIRE Contributions -->
<!-- SUBTITLE: A quick summary of 5GinFIRE contributions -->

# Multi-site deployments with OSM R5
## Usage 
The following test describes a procedure to enable the multi-site deployment of network services in OSM Release FIVE, avoiding the utilization of a Wan Infrastructure Manager (WIM). This procedure has been developed in the context of the  [H2020 5GinFIRE project](https://5ginfire.eu).

1)  Create a “dummy WIM” account in the OSM, specifying which VIMs will be used for multi-site deployments. This step is needed because in this type of deployments the RO first verifies the existence of a WIM account with the information about all the involved VIMs; and if it does not exist, the deployment is rejected. This information is defined by the OSM information model and can be provided in a JSON file at the WIM account creation time.

The following OSM-CLI command shows the creation of a WIM account, and uses a specific JSON file that is also provided as an example ([Dummy Wim Port Mappings](/uploads/contributions-osm-r-5-multi-site/dummy-wim-port-mappings.json "Dummy Wim Port Mappings")):

`osm wim-create --name dummy-wim --wim_type odl --url http://dummy-wim-odl --wim_port_mapping dummy_wim_port_mappings.json`
