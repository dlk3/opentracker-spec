#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.

%define  debug_package %{nil}

Name:		opentracker
Version:	2018.05.26
Release:	3%{?dist}
Summary:	Opentracker Bittorrent Tracker

License:	MPLv2.0
URL:		http://erdgeist.org/arts/software/opentracker/
Source0:	%{name}-%{version}.tar.gz
Source1:	%{name}
Source2:	%{name}.service
BuildArch:	x86_64

BuildRequires:	make
BuildRequires:	zlib-devel
BuildRequires:	clang


%description
opentracker is a open and free bittorrent tracker project. It aims for
minimal resource usage and is intended to run at your wlan router.
Currently it is deployed as an open and free tracker instance.


%prep
%setup
cp opentracker/README* .


%build
cd libowfat
make
cd ../opentracker
make


%install
mkdir -p %{buildroot}%{_bindir}
install -m 755 -t %{buildroot}%{_bindir} opentracker/opentracker
mkdir -p %{buildroot}/etc/sysconfig
install -m 644 -t %{buildroot}/etc/sysconfig %{SOURCE1}
mkdir -p %{buildroot}/usr/lib/systemd/system
install -m 644 -t %{buildroot}/usr/lib/systemd/system %{SOURCE2}


%files
%doc README
%doc README_v6
/etc/sysconfig/opentracker
%{_bindir}/opentracker
/usr/lib/systemd/system/opentracker.service


%changelog
* Sun Apr 26 2020 David King <dave@daveking.com> - 2018.05.26-3
	Added clang to build requirements
	Switch to libowfat 0.32 to correct compile errors
* Mon Dec 23 2019 David King <dave@daveking.com> - 2018.05.26-2
	Added systemd control file
* Sat Dec 21 2019 David King <dave@daveking.com> - 2018.05.26-1
	Initial Version
