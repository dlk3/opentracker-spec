#  opentracker RPM Package For CentOS

This folder contains a SPEC file that can be used to create a RPM package
for the opentracker application.  I created this for myself as there is
no CentOS package for this application.

opentracker is a highly scalable tracker for the bittorrent protocol.
See http://erdgeist.org/arts/software/opentracker/ for details. 

I have created a Fedora COPR repository to support the installation of
the RPMs I created.  To install opentracker from this repository do:
```
$ sudo yum copr enable dlk/rpms
$ sudo yum install opentracker
```
