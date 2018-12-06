<!-- TITLE: The 5GinFIRE Central Logging service -->
<!-- SUBTITLE: The 5GinFIRE Central Logging service -->

# The 5GinFIRE Central Logging service

![Hcs Elastic Architecture](/uploads/hcs/hcs-elastic-architecture.png "Hcs Elastic Architecture")

The 5GinFIRE Central Logging Service is a simple service that collects various logging information from  components of the 5GinFIRE infrastructure. It enables to retrieve historical data, usage and actions of various components.
The service allows all registered Components to POST a logging message through the [5GinFIRE Healthcheck service (HCS)](hcservice/usage) and this message is stored in an Elasticsearch cluster and later on examined via a Kibana services as the next figure shows:

