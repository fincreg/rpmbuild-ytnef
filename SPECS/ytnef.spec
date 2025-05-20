Summary:    Yerase's TNEF Stream Reader
Name:       ytnef
Epoch:      1
Version: 	%{version}
Release: 	%{release}%{?dist}
License:    GPL
Group:      Applications/Productivity
URL: 		https://github.com/Yeraze/ytnef
Source0: 	https://github.com/Yeraze/ytnef/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRoot:  %{_tmppath}/%{name}-%{version}-buildroot

%description
Yerase's TNEF Stream Reader.  Can take a TNEF Stream (winmail.dat) sent from
Microsoft Outlook (or similar products) and extract the attachments, including
construction of Contact Cards & Calendar entries.

%prep
%setup -q

%build
mkdir -p m4
autoreconf -vfi
%configure
make

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc COPYING 
%{_bindir}/*
%{_libdir}/*
%{_includedir}*

%changelog
* Fri Mar 12 2004 Patrick <rpms@puzzled.xs4all.nl>
- Initial version

