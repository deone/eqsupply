Summary:	Web-based equipment quote generator.
Name:		eqsupply
Version:	0.1
Release:	25
Group:		Business Solutions/Web-based
License:	GPL
Source0:	%{name}-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-build

Prereq:		mysql-server
Prereq:		mysql
Prereq:		httpd
Prereq:		python


%description
In the current use case, eqsupply is the web platform for an equipment supply business, primarily dealing in oil, gas and manufacturing. A little tweaking would make it generic.


%prep
%setup -q


%build
make


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%config /etc/httpd/conf.d/eqsupplymod_wsgi.conf
/usr/local/www/
/usr/bin/eqsupply-setup
/var/lib/eqsupply/


%post
echo "Success! To complete the installation, please run 'eqsupply-setup' on the command line"
