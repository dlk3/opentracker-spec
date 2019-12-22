%define  debug_package %{nil}

Name:		opentracker
Version:	2018.05.26
Release:	1%{?dist}
Summary:	Opentracker Bittorrent Tracker

License:	beerware
URL:		http://erdgeist.org/arts/software/opentracker/
Source0:	%{name}-%{version}.tar.gz
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


%files
%doc README
%doc README_v6
%{_bindir}/opentracker


%changelog
* Sat Dec 28 2019 David King <dave@daveking.com> - 2018.05.26
	Initial Version
