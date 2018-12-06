<!-- TITLE: The 5GinFIRE Central Logging service -->
<!-- SUBTITLE: The 5GinFIRE Central Logging service -->

# The 5GinFIRE Central Logging service

![Hcs Elastic Architecture](/uploads/hcs/hcs-elastic-architecture.png "Hcs Elastic Architecture")

The 5GinFIRE Central Logging Service is a simple service that collects various logging information from  components of the 5GinFIRE infrastructure. It enables to retrieve historical data, usage and actions of various components.
The service allows all registered Components to POST a logging message through the [5GinFIRE Healthcheck service (HCS)](hcservice/usage) and this message is stored in an Elasticsearch cluster and later on examined via a Kibana services as the next figure shows:

![Hcs Centrallog Kibana](/uploads/hcs/hcs-centrallog-kibana.png "Hcs Centrallog Kibana")


## How it works

Components POST a logging message towards the [5GinFIRE Healthcheck service (HCS)](hcservice/usage)  to the url:

```text
http://status.5ginfire.eu/hcs/services/api/admin/components/{apikey}/log"
```

*apikey* is a unique string for each component. (apikeys for a Component will be given by the HCS admins, see  [5GinFIRE Healthcheck service (HCS)](hcservice/usage))

with payload a JSON like the following:
```text
{ 
   "clevel":"INFO", 
   "message":"user logged in"
}
```

**clevel** must be one of: INFO, WARN, ERROR


Example:

```text
curl -XPOST "http://status.5ginfire.eu/hcs/services/api/admin/components/53f7118f-xxxx-xxxx-xxxx-xxxxxxxxxx/log" -H 'Content-Type: application/json' -d '{"clevel":"INFO", "message":"user logged in"}'

```

