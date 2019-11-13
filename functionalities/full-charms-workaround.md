
5G Media Vertical offers a possibility for deployment of descritpors with full (native) charms. 
This feature will only be supported in OSM 6.0.4 so we use a cartain workaround for OSM 5 (see Deliverable 4.2 for the details)

## Workflow

### Preparations
You need to be an experimenter using 5G Media Vertical and contact piotr.zuraniewski.tno.nl to obtain a private key to access local instance of the OSM. This instance has charm development environment configured, as in

http://osm-download.etsi.org/ftp/osm-6.0-six/7th-hackfest/presentations/7th%20OSM%20Hackfest%20-%20Session%206.1%20-%20Introduction%20to%20Proxy%20Charms.pdf

Addtionally `builds` subfolder was created. 

Once logged in `~/charms` there is a `source-me.sh` file which needs to be sourced for the charm builder
to know the locations of the files.
```
export JUJU_REPOSITORY=~/charms
export CHARM_BUILD_DIR=$JUJU_REPOSITORY/builds
export CHARM_INTERFACES_DIR=$JUJU_REPOSITORY/interfaces
export CHARM_LAYERS_DIR=$JUJU_REPOSITORY/layers
```

