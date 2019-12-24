%define  debug_package %{nil}

Name:		opentracker
Version:	2018.05.26
Release:	2%{?dist}
Summary:	Opentracker Bittorrent Tracker

License:	beerware
URL:		http://erdgeist.org/arts/software/opentracker/
Source0:	%{name}-%{version}.tar.gz
Source1:	%{name}
Source2:	%{name}.service
BuildArch:	x86_64

BuildRequires:	make
BuildRequires:	zlib-devel


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
* Mon Dec 23 2019 David King <dave@daveking.com> - 2018.05.26-2
	Added systemd control file
* Sat Dec 21 2019 David King <dave@daveking.com> - 2018.05.26-1
	Initial Version
