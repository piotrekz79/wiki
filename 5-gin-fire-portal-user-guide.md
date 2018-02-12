<!-- TITLE: 5GinFIRE Portal User Guide -->
<!-- SUBTITLE: User Guide for the Web Portal -->

# 5GinFIRE Portal User Guide

Welcome to the 5GinFIRE Portal User Guide.
5GinFIRE offered services and tools target to accommodate the following envisaged user roles. All users are assumed to be Authenticated:
* Experimenter: This role represents the user that will utilize our services and tools to deploy an experiment. That is the experiment description in terms of e.g.: NSD (Network Service Descriptor) or TOSCA Specification (in future versions)
* VxF developer: This role is responsible to upload  VNF and NSD Descriptors in the 5GinFIRE services
* Testbed provider: This role represents users that are responsible for testbed administration, configuration, integration, adaptation, support, etc
* Services administrator: This role represents the user that are responsible for maintenance of the 5GinFIRE services

Finally an anonymous user role exists who has some really simple usage scenarios (e.g. signup through the portal)

## Terminology
Please see the used terminology at the [architecture pages](5-gin-fire-terminology-experimentation-workflow-and-architecture#terminology)


## Architecture

The portal consists of two main components: The portal web frontend and the portal API backend. The Web front end communicates with the backend via a RESTful API. 
Moreover, the portal backend implements: An interface towards the OSM API in order to on-board VxF and NSDs to the OSM repository and get related information, and an interface towards an identity provider and a portal repository that reflects the artefacts of the OSM repository

Please check the [portal Architecture and Design](portalArchitectureDesign) section

## Supported processes
The process to upload/onboard VNFs, Experiements in terms of NSDs are as follows:

### 	Uploading a VxF

![Portal Diag 1](/uploads/portal-diag-1.png "Portal Diag 1")
During this process (see Figure ) the following occurs:
•	A VxF developer submits a VxF archive (he can later manage if needed some metadata)
•	The administrator can manage the VxF (e.g. edit it)
•	The administrator On-Boards the VxF to the target MANO
•	The administrator can optionally mark the VxF:
o	As public in order to be publicly visible by all portal users
o	As Certified which means this is certified by a certain entity


### Uploading an Experiment Descriptor/NSD


![Portal Diagtwo](/uploads/portal-diagtwo.png "Portal Diagtwo")
During this process (see Figure ) the following occurs:
•	An experimenter submits an experiment in terms of an NSD archive (he can later manage if needed some metadata)
•	The administrator can manage the NSD (e.g. edit it)
•	The administrator on-boards the NSD to the target MANO
•	The administrator can optionally mark the VxF:
o	As valid, which means this NSD can be indeed deployed to VIMs
o	As public in order to be publicly visible by all portal users


### Request a new experiment deployment

![Portal Diagthree](/uploads/portal-diagthree.png "Portal Diagthree")

During this process (see Figure ) the following occurs:
•	An experimenter requests a new experiment deployment (which NSD, tentative dates, target infrastructure, etc.). The request is marked as UNDER_REVIEW
•	The administrator is notified about the new request and he has the following options:
o	Schedule the deployment for the requested dates or propose other dates. The request is marked as SCHEDULED
o	Reject the request for some reason. The Request is marked as REJECTED
o	Deploy the request to target VIM(s). The Request is marked as RUNNING
o	Finalize the deployment and release resources. The Request is marked as COMPLETED
On every change of the request-lifecycle the experimenter is notified.



## Public user Web interface/Landing page  

Initially (beside authorized user roles) there are anonymous/public users who can only see the published VxFs and experiments without needing a portal account. The main interface that all kind of users have access is the landing page that can be seen in figure below:

![Fig 13](/uploads/fig-13.png "Fig 13")

At the menu on the top we can see experiments and VxFs tabs which redirect users accordingly. Additionally, an authorized user gets access to its account by inserting its username and password at the fields bellow the “Sign in” label. A user can sign up in order to get an authorized account by clicking on sign up text description next to sign in button and then it is redirected at the user page . After that the user inserts its details in the appropriate fields and then when is submitting an email is send for account confirmation.
**Initially a user has a role of Experimenter/VxF developer**

Next, we continue by describing the user interface for every authorized user role separately. At the start we review the landing page which is shown up when a user is logged in the portal and then we walk through all the available menus provided by the user interface.

## 	VxF developer user interface description
The first user role we are going to describe is the VxF developer. In the next figure you can see the landing page for this role:

![Fig 15](/uploads/fig-15.png "Fig 15") Available experiments, VxF developer login page

On the top part of the interface we can distinguish the options that are provided to the VxF developer role. When a user of this role is logged in its account the experiments option is selected by default. On the left part of the page we can see all the available categories in terms of experiments that are to be uploaded by either the experimenter or the service administrator user role. The categories mentioned previously are designated by service administrators except for the “All” category which includes all the published experiments by service administrators and the pre-existing “None” category which is created by portal installation. Finally, at the bottom of the interface we can find the published experiments belonging to the opted category.
Similarly with the previous description in the next Figure at VxF menu option we can list all the available published VxFs uploaded by either the VxF developers or the service administrators:
![Fig 16](/uploads/fig-16.png "Fig 16")

The options of the Admin tab of the menu can be seen in Figure  below:
![Fig 17](/uploads/fig-17.png "Fig 17")

The only submenu of this tab is the Registered VxFs which are presented in the main body of the page in Figure . In this section a VxF developer can list the registered VxFs in the VxF repository and additionally at the table provided by the interface the user can see some details about each VxF. Additionally, below each field descriptor a text box is provided in order to help user to search for a specific VxF based on the corresponding search feature. Apart from this kind of search a search text box can been found below the table where a general search decoupled from VxF's features can be performed. The VxF developer can also delete, edit and review some information on the fly for each record of the table by clicking accordingly the desired button at the last column of the provided table. Finally, above the table there are two green buttons available where a user can upload a VxF archive or create a new one. In the first case the user just uploads the VxF archive on the VxF repository by choosing also the category in which the VxF belongs and by writing some terms of use for this as well. You can see the user interface of this procedure at next Figure .

![Fig 18](/uploads/fig-18.png "Fig 18")
In the second case a more refined procedure is provided by making the VxF developer able to insert some basic metadata of the uploaded VxF archive through the user interface in Figure 19.

![Fig 19](/uploads/fig-19.png "Fig 19")
The most obvious metadata are the name, version, teaser, vendor, logo, description and terms of use of VxF. For the rest of the metadata there are some predefined values available. At packaging format field the VxF developer provides the type of the VxF file. For instance the available formats could be OSM Release TWO or TOSCA. Regarding the last two metadata fields, the Category field refers to the category in which the VxF belongs to as we have also indicated in the first case, and the Supported MANO Platforms field contains a list of the supported MANO platforms like OSM TWO etc. Those platforms are declared by the services administrator role through its interface as we will see in the next section.
Finalizing, the description of VxF developer user role we present the interfaces of edit and info button of each VxF. In the case of the edit button the interface is the same as Figure 19 but the only difference is that a descriptor metadata field is provided as well. In that field we can overview the YAML description of the chosen VxF. The interface of the info button as well as the details button of the available VxFs in the Figure 20 can be seen in the figure below:
![Fig 20](/uploads/fig-20.png "Fig 20")
As we can see here the most information have already been provided by either the VxF package or the VxF developer as we have described earlier in the previous parts but also some new fields are visible that is Organization, Date created, Last Update, UUID, Certified by and Onboarded to MANO providers. Most of those fields are self-explainable apart from perhaps the Onboarded to MANO providers field, which contains the MANO provider on which this VxF has been deployed. Finally, a VxF developer can download the stored VxF package just by clicking the green button on the top side of the page.

## Experimenter user interface description

The second user role we are going to describe is the experimenter. In the next figure you can see the 
landing page for this role:

![Fig 21](/uploads/fig-21.png "Fig 21")

As we can note this page is almost identical to the page of VxF developer role but differs to the menu 
on the top side of the page. A new tab Deployments has been added comparing with the previous 
menu.  In  addition,  the  submenu  of  Admin  tab  has  been  changed  to  registered  experiment 
descriptors as we will see later on.  In the next parts of this section we will describe only the new 
functionalities  available  to  the  experimenter  role  omitting  the  common  already  described  at  VxF 
developer section. The first menu we are going to describe is Deployments and especially its only 
submenu  that  is  deploy  experiments.  The  user  interface  for  this  submenu  is  shown  up  in  figure 
below:

![Fig 22](/uploads/fig-22.png "Fig 22")

This  screen  lists  the  deployed  experiments  by  the  services  administrator  role.  Similarly  with  the 
available VxF screen for each field a text box is provided in order to help the user to search for a 
specific deployed experiment based on the corresponding search feature. Also, a general search is 
provided  under  the  table.  All  those  fields  are  described  at  the  interface  which  is  shown  up  after 
clicking on the green button on the top side of the page whose role is to create a new deployment by 
selecting one of the available experiments. Finally, the status column denotes the current state of 
each  deployment  and  is  managed  by  the  services  administrator  role.  The  available  states  will  be 
described later on in services administrator role section. By pressing the green button the layout in 
next figure is shown up:

![Fig 23](/uploads/fig-23.png "Fig 23")

In this figure we can see all the necessary fields to define a new deployment. At the experiment drop 
down menu we can select the desirable experiment from those provided to be deployed by a service 
administrator. The experimenter can select also the target infrastructure for all or for each individual 
constituent VxF. At the next fields we also provide the necessary information be indicated by them 
and  when  all  those  fields  are  filled  up  the  experimenter  can  submit  this  specific  deployment  by 
clicking  the  request  deployment  button  on  the  bottom  of  the  interface.  Then  this  deployment 
request is sent to the service administrator in order to be proceeded or to be rejected.
In Figure 24 we can see the content of the interface when an experimenter selects the Admin tab of 
the  menu  and  specifically  the  registered experiment  descriptors.  This  page  again  is  similar  to  the
registered VxF page which appears in Figure 17 but the difference is that some metadata fields are 
missing and also this interface lists the available experiments instead of the available VxFs.

![Fig 24](/uploads/fig-24.png "Fig 24")

By  clicking  the  first  green  button  that  is  Upload  new  Experiment  Descriptor  the  experimenter  is 
redirected exactly to same interface as in Figure 18 but without the terms of use field and apart from 
that this time the experimenter uploads an experiment package file instead of a VxF. The other green 
button follows similar logic as the corresponding button at the VxF interface but again instead of the 
creation of a new VxF a new Experiment is defined by experimenter filling the appropriate metadata 
fields.  The  interface  is  also  similar  to  the  VxF  interface  in  Figure  19 but  some  fields  are  missing 
comparing  with  it  but  the  functionality  for  the  rest  of  them  remains the  same.  The  interface 
metadata fields for a new experiment can be seen in figure below:

![Fig 25](/uploads/fig-25.png "Fig 25")

Finally, in Figure 25 we can see the interface where an experimenter lands on when clicking on the 
edit button of an experiment in Figure 24 or on the details button of an experiment in Figure 21. This 
page is also available for the VxF developer role as we can see in Figure 15. This page has similar 
fields with the VxF details interface in Figure 20 but some fields have been subtracted and the status 
metadata field has been added to it.
