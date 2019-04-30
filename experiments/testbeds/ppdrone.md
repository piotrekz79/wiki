<!-- TITLE: PPDR ONE Experiment example  -->
<!-- SUBTITLE: Network performance testing for PPDR-ready network architectures -->

# PPDR ONE Experiment example
## Experiment Overview

The example scenario utilizes qMON Monitoring solution implemented as VxFs and NSD to enable client-server network performance measurements between different VIM hosts or VIM providers.

![Ppdrone Experiment Example Small](/uploads/ppdrone/ppdrone-experiment-example-small.png "Ppdrone Experiment Example Small")
**Figure 1: PPDRONE Experiment Example**

## qMON Monitoring Solution

qMON Intervention Monitoring solution is a telco-grade 5G-ready measurement automation system for mobile, fixed and cloud environments (TRL9). It provides:
* Probes, management backend and analytics tools
* Live network and service tests/troubleshooting 
* Real-time performance and SLS/SLA monitoring
* Drive and benchmark testing for broadband PPDR networks (LTE/4G and 5G)
* PPDR network coverage and mission critical application performance assessment
* QoE/QoS prediction in live BB PPDR networks

![Qmon System Architecture](/uploads/ppdrone/qmon-system-architecture-small.png "Qmon System Architecture")
**Figure 2: qMON System Architecture**

The qMON system comprises 4 main parts based either on cloud VMs, containers or dedicated consumer and industrial HW:
* **qMON NetworkSensor** – Autonomous distributed agent for emulating user (mobile/fixed) activities and active services/applications
* **qMON Manage** – cloud-based back-end agent management
* **qMON Collector**– centralized data and KPI collection infrastructure;
* **qMON Insight** – Advanced KPI analysis and visualizations using professional real-time and offline BI analytics tools (Kibana, Grafana and Tableau).

![Qmon](/uploads/ppdrone/qmon.png "Qmon")
**Figure 3: qMON System Components**

Various network KPIs are measured and saved during the measurements, among them but not limited to, are the following KPIs:

* RTT (round trip time)
* DNS
* IPERF Download
* IPERF Upload
* HTTP/FTP Download
* WEB MOS
* FTP UPLOAD

If the qMON NetworkSensor runs on phsyical device with a modem (Linux-based PC or Android) the radio KPIs are also collected (e.g. RSRP, RSRQ, CA State…)

## Components description

qMON NetworkSensor is provided to experimenters as a VxF in client and server mode. 

### VxF

**qMON NetworkSensor Client VxF**

* Acts as a measurement client
* Emulates end user
* Can be deployed as as simple service (client only) or in client-server mode.

Example template for qMON NetworkSensor Client VxF:


```text
vnfd:vnfd-catalog:
    vnfd:
    -   connection-point:
        -   name: ens3
            type: VPORT
        -   name: ens4
            type: VPORT
        description: qMON Cloud Agent VNF with 2 nic
        id: qmon_vnfd_2net
        logo: inin-64.png
        mgmt-interface:
            cp: ens3
        monitoring-param:
        -   aggregation-type: AVERAGE
            id: metric_vim_client_load
            name: metric_vim_client_load
            vnf-metric:
                vnf-metric-name-ref: load
        -   aggregation-type: AVERAGE
            id: metric_vim_client_loadpct
            name: metric_vim_client_loadpct
            vnf-metric:
                vnf-metric-name-ref: load_pct
        -   aggregation-type: AVERAGE
            id: metric_vim_client_users
            name: metric_vim_client_users
            vnf-metric:
                vnf-metric-name-ref: users
        -   aggregation-type: AVERAGE
            id: metric_vim_client_mempct
            name: metric_vim_client_mempct
            vnf-metric:
                vnf-metric-name-ref: mem_pct
        -   aggregation-type: AVERAGE
            id: metric_vim_client_qmonrtt
            name: metric_vim_client_qmonrtt
            vnf-metric:
                vnf-metric-name-ref: qmon_rtt
        name: qmon_vnf_2net
        short-name: qmon_vnf_2net
        vdu:
        -   cloud-init-file: qmon_cloud_init.cfg
            count: 1
            description: qmon_vnfd_2net-VM
            id: qmon_vnfd_2net-VM
            image: qoe_vnf
            interface:
            -   external-connection-point-ref: ens3
                name: ens3
                type: EXTERNAL
                virtual-interface:
                    bandwidth: '0'
                    type: VIRTIO
                    vpci: 0000:00:0a.0
            -   external-connection-point-ref: ens4
                name: ens4
                type: EXTERNAL
                virtual-interface:
                    bandwidth: '0'
                    type: VIRTIO
                    vpci: 0000:00:0a.0
            name: qmon_vnfd_2net-VM
            vm-flavor:
                memory-mb: 2048
                storage-gb: 20
                vcpu-count: 2
        vendor: ININ
        version: '1.0'
        vnf-configuration:
            config-primitive:
            -   name: set-work-order
                parameter:
                -   data-type: STRING
                    default-value: ''
                    name: woid
                -   data-type: STRING
                    default-value: mndev.iinstitute.eu
                    name: mn
                -   data-type: STRING
                    default-value: xxxx
                    name: apikey
            -   name: set-mn-url
                parameter:
                -   data-type: STRING
                    default-value: ''
                    name: mn
            -   name: set-server-key
                parameter:
                -   data-type: STRING
                    default-value: ''
                    name: apikey
            -   name: set-server-ip
                parameter:
                -   data-type: STRING
                    default-value: ''
                    name: ip
            initial-config-primitive:
            -   name: config
                parameter:
                -   name: ssh-hostname
                    value: <rw_mgmt_ip>
                -   name: ssh-username
                    value: ubuntu
                -   name: ssh-password
                    value: qoe
                -   name: mode
                    value: client
                seq: '1'
            -   name: set-second-net
                seq: '2'
            -   name: set-second-net-dhcp
                seq: '3'
            -   name: set-work-order
                parameter:
                -   name: woid
                    value: '257'
                -   name: mn
                    value: mndev.iinstitute.eu
                -   name: apikey
                    value: xxxxx
                seq: '4'
            -   name: set-server-ip
                parameter:
                -   name: ip
                    value: 10.154.98.10
                seq: '6'
            -   name: set-qmon-monitoring
                seq: '7'
            juju:
                charm: qmon-2net
            metrics:
            -   name: load
            -   name: load_pct
            -   name: users
            -   name: mem_pct
            -   name: qmon_rtt

```

**qMON NetworkSensor Server VxF**

* acts as a measurement server,
* support multiple measurement clients,
* can be deployed as as simple service (server only) or in client-server mode.

Example template for qMON NetworkSensor Server VxF:

```text
vnfd:vnfd-catalog:
    vnfd:
    -   connection-point:
        -   name: ens3
            type: VPORT
        -   name: ens4
            type: VPORT
        description: qMON Cloud Reference Server VNF with 2 nic
        id: qmon_server_vnfd_2net
        logo: inin-64.png
        mgmt-interface:
            cp: ens3
        monitoring-param:
        -   aggregation-type: AVERAGE
            id: metric_vim_server_load
            name: metric_vim_server_load
            vnf-metric:
                vnf-metric-name-ref: load
        -   aggregation-type: AVERAGE
            id: metric_vim_server_loadpct
            name: metric_vim_server_loadpct
            vnf-metric:
                vnf-metric-name-ref: load_pct
        -   aggregation-type: AVERAGE
            id: metric_vim_server_users
            name: metric_vim_server_users
            vnf-metric:
                vnf-metric-name-ref: users
        -   aggregation-type: AVERAGE
            id: metric_vim_server_mempct
            name: metric_vim_server_mempct
            vnf-metric:
                vnf-metric-name-ref: mem_pct
        name: qmon_server_vnf_2net
        short-name: qmon_server_vnf_2net
        vdu:
        -   cloud-init-file: qmon_cloud_init.cfg
            count: 1
            description: qmon_server_vnfd_2net-VM
            id: qmon_server_vnfd_2net-VM
            image: qoe_server_vnf
            interface:
            -   external-connection-point-ref: ens3
                name: ens3
                type: EXTERNAL
                virtual-interface:
                    bandwidth: '0'
                    type: VIRTIO
                    vpci: 0000:00:0a.0
            -   external-connection-point-ref: ens4
                name: ens4
                type: EXTERNAL
                virtual-interface:
                    bandwidth: '0'
                    type: VIRTIO
                    vpci: 0000:00:0a.0
            name: qmon_server_vnfd_2net-VM
            vm-flavor:
                memory-mb: 2048
                storage-gb: 20
                vcpu-count: 2
        vendor: ININ
        version: '1.0'
        vnf-configuration:
            initial-config-primitive:
            -   name: config
                parameter:
                -   name: ssh-hostname
                    value: <rw_mgmt_ip>
                -   name: ssh-username
                    value: ubuntu
                -   name: ssh-password
                    value: qoe
                -   name: mode
                    value: server
                seq: '1'
            -   name: set-second-net
                seq: '2'
            -   name: set-second-net-dhcp
                seq: '3'
            juju:
                charm: qmon-2net
            metrics:
            -   name: load
            -   name: load_pct
            -   name: users
            -   name: mem_pct

```

### NSD

Along with VxFs, the NSD templates are also available to experimenters enabling them to setup different network service topologies such as:

* Client NSD (enables single qMON NetworkSensor Client VxF)
* Server NSD (enables single qMON NetworkSensor Server VxF)
* Client-Server NSD (enables qMON NetworkSensor Client and Server VxFs, fully configured through charms, supports multi-VIM deployment).

**qMON Client NSD**

This network service instantiates single qMON NetworkSensor Client VxF which allows measurements to the preconfigured qMON NetworkSensor Server (either deployed manually by PPDR ONE stuff or deployed as a VxF by the experimenter). Client NSD can be deployed on different hosts in the same VIM or on different VIMs.

![Qmon Client Nsd](/uploads/ppdrone/qmon-client-nsd.png "Qmon Client Nsd")
**Figure 4: qMON Simple Client NSD**

Example template for qMON NetworkSensor Client NSD:

```text
nsd:nsd-catalog:
    nsd:
    -   constituent-vnfd:
        -   member-vnf-index: 1
            vnfd-id-ref: qmon_vnfd
        description: qMON Cloud Agent Single VNF Service
        id: qmon_vnf_nsd
        logo: qmon-64.png
        name: qmon_vnf_ns
        short-name: qmon_vnf_ns
        vendor: ININ
        version: '1.0'
        vld:
        -   id: provider-dev
            mgmt-network: 'true'
            name: provider-dev
            short-name: provider-dev
            vim-network-name: provider-dev
            vnfd-connection-point-ref:
            -   member-vnf-index-ref: 1
                vnfd-connection-point-ref: ens3
                vnfd-id-ref: qmon_vnfd

```

**qMON Server NSD**

This network service instantiates single qMON NetworkSensor Server VxF which allows multiple qMON NetworkSensor Clients (either deployed manually by PPDR ONE stuff or deployed as a VxF by the experimenter. For example, this NSD can be used to instantiate measurement server in the PPDR ONE Portable node and run qMON NetworkServer Client on the Android device connected to RAN hosted by the same PPDR ONE node. This enables testing 5G topologies such as Isolated Operations for PPDR while collecting network and radio KPIs. 

![Qmon Server Nsd](/uploads/ppdrone/qmon-server-nsd.png "Qmon Server Nsd")
**Figure 5: qMON Simple Server NSD**

Example template for qMON NetworkSensor Server NSD:

```text
nsd:nsd-catalog:
    nsd:
    -   constituent-vnfd:
        -   member-vnf-index: 1
            vnfd-id-ref: qmon_server_vnfd
        description: qMON Cloud Reference Server VNF Service
        id: qmon_server_vnf_nsd
        logo: qmon-64.png
        name: qmon_server_vnf_ns
        short-name: qmon_server_vnf_ns
        vendor: ININ
        version: '1.0'
        vld:
        -   id: provider
            mgmt-network: 'true'
            name: provider
            short-name: provider
            vim-network-name: provider
            vnfd-connection-point-ref:
            -   member-vnf-index-ref: 1
                vnfd-connection-point-ref: ens3
                vnfd-id-ref: qmon_server_vnfd

```

**Client-Server NSD**

This network service instantiates qMON NetworkSensor Client and Server VxFs. It can run in the same VIM or between different VIM providers to measure connectivity parameters between different clouds. It support configuration of parameters to allow fully automated deployment (via static IP configuration) or it can be deployed and configured later via “configuration primitives” via OSM. The service uses two networks, one for management (e.g. charms from OSM) and one for data connectivity with the latter being the one actually under test. 

![Qmon Server Nsd](/uploads/ppdrone/qmon-server-nsd.png "Qmon Server Nsd")
**Figure 6: qMON Simple Server NSD**

The example of Client-Server NSD:

```text
nsd:nsd-catalog:
    nsd:
    -   constituent-vnfd:
        -   member-vnf-index: 1
            vnfd-id-ref: qmon_server_vnfd
        -   member-vnf-index: 2
            vnfd-id-ref: qmon_client_vnfd
        description: qMON Cloud Client Server VNF Service (Static IP, auto config)
        id: qmon_client_server_nsd
        logo: qmon-64.png
        name: qmon_client_server_ns
        short-name: qmon_client_server_ns
        vendor: ININ
        version: '1.0'
        vld:
        -   id: provider
            mgmt-network: 'true'
            name: provider
            short-name: provider
            vim-network-name: provider
            vnfd-connection-point-ref:
            -   member-vnf-index-ref: 1
                vnfd-connection-point-ref: ens3
                vnfd-id-ref: qmon_server_vnfd
            -   member-vnf-index-ref: 2
                vnfd-connection-point-ref: ens3
                vnfd-id-ref: qmon_client_vnfd
        -   id: provider2
            name: provider2
            short-name: provider2
            vim-network-name: provider2
            vnfd-connection-point-ref:
            -   ip-address: 10.154.98.10
                member-vnf-index-ref: 1
                vnfd-connection-point-ref: ens4
                vnfd-id-ref: qmon_server_vnfd
            -   ip-address: 10.154.98.11
                member-vnf-index-ref: 2
                vnfd-connection-point-ref: ens4
                vnfd-id-ref: qmon_client_vnfd

```

## Deployment of the experiment
The deployment of qMON VxF can be easily recreated by utilizing provided VxF and NSD templates. PPDR ONE stuff is available for support and help with the configuration on different network topologies. 

The qMON NetworkSensor Client and Server VxFs use specific OpenStack image, so if deployment should occur in multiple VIMs, the image must be present on all involved VIM providers.

## Results and analytics
All the results, measurement KPIs and test metadata is stored in the qMON Cloud in MySQL/MSSQL database. They can be made available to the experimentors online, via dump or via some other tool such as Elasticserch, Influxdb or Prometheus. Additionally, Grafana dashboards are available to experimenters to allow near real-time monitoring of the KPIs.

![Grafana Overview](/uploads/ppdrone/grafana-overview.png "Grafana Overview")
**Figure 7: Grafana qMON Overview Dashboard**

![Grafana Ping](/uploads/ppdrone/grafana-ping.png "Grafana Ping")
**Figure 8: Grafana qMON Ping Dashboard**