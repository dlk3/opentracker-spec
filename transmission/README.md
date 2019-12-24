#  transmission RPM Packages For CentOS

This folder contains the CentOS 7 source rpms for two packages,
transmission and libnatpmp, which is a pre-req for transmission.
Neither of these are currently available for CentOS 8 but were available
for CentOS 7.  It appears to be possible to build these packages 
unchanged in CentOS 8 and the automated build script (mkrpms) in this
folder does that using a podman container image.
