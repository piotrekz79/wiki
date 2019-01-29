<!-- TITLE: Exploring SURROGATES VNFs -->

# Introduction
In the SURROGATES experiment the ITAv OBU capabilities regarding network mobility are exploited to offer 11p/4G hybrid communications as a base enabler to offload processing tasks from the same unit. This is carried out by virtualizing OBU instances at the edge of the 5GINFIRE cloud. A base monitoring system considering sensor data from the vehicle sends raw information to an OBU virtual instance. Here, pre-processing, aggregation and pattern recognition tasks can be carried out. Processed information is then available for global Cooperative Intelligent Transportation Systems (C-ITS) services.

The idea is to offload data analytics tasks from OBUs, which should focus on actions of higher priority such as maintaining vehicle connectivity, managing communication flows or applying security measures to data traffic. As can be seen in Figure 1, the approach chosen in SURROGATES is to create virtualized images of OBUs near the edge of the network, where raw data sent from in-vehicle sensors is processed. Hence, a monitoring middleware is considered for the OBU to gather continuously raw data that are sent to the data processing functions delegated into the cloud-edge. Data analytics tasks envisaged include pre-processing, aggregation and pattern recognition. Processed or cached information are accessed by vehicular services requiring a global view of the road. An OBU manager module has been defined to be the initial contact point from physical OBUs wanting to connect to its virtual counterpart. This manager is also an NFV module, and communicates with OSM to indicate the need for a virtual OBU instance. OSM is in charge of creating and managing these instances, which could be potentially instantiated on demand. Data to be collected from the OBUs consider navigation information, diagnosis and mechanical monitoring details of the car, and readings from other sensors connected to the OBU.

![Surrogate 1](/uploads/surrogates/surrogate-1.png "Surrogate 1")
Figure 1 - Architecture of SURROGATES.
## Information collected through OBD-II

# Running the Experiment
## Connection

## Setup