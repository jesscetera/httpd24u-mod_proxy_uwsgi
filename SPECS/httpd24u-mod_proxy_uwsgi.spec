# IUS spec file for httpd24u-mod_proxy_uwsgi
#
# This package is intended to work with uwsgi from EPEL and httpd24u from IUS.
# It should remain at the same version as the EPEL uwsgi package to ensure
# compatibility.

%global httpd httpd24u
%global module mod_proxy_uwsgi

Name:           %{httpd}-%{module}
Version:        2.0.14
Release:        1.ius%{?dist}
Summary:        uWSGI - Apache2 proxy module
Group:          System Environment/Daemons
License:        GPLv2 with exceptions
URL:            https://github.com/unbit/uwsgi
Source0:        10-%{module}.conf
Source1:        %{module}.conf
BuildRequires:  uwsgi-devel, %{httpd}-devel
Requires:       uwsgi, %{httpd}, httpd-mmn = %{_httpd_mmn}

Conflicts:      %{module}

%{?filter_provides_in: %filter_provides_in %{_httpd_moddir}/.*\.so$}
%{?filter_setup}


%description
Fully Apache API compliant proxy module.  Designed to work with the uwsgi
packages in EPEL, but built against httpd24u from IUS.


%prep
%setup -q -c -T
cp %{_usrsrc}/uwsgi/%{version}/apache2/%{module}.c .


%build
%{_httpd_apxs} -Wc,-Wall -Wl -c %{module}.c


%install
install -D -p -m 0755 .libs/%{module}.so %{buildroot}%{_httpd_moddir}/%{module}.so
install -D -p -m 0644 %{SOURCE0} %{buildroot}%{_httpd_modconfdir}/10-%{module}.conf
install -D -p -m 0644 %{SOURCE1} %{buildroot}%{_httpd_confdir}/%{module}.conf


%files
%{_httpd_moddir}/%{module}.so
%config(noreplace) %{_httpd_modconfdir}/10-%{module}.conf
%config(noreplace) %{_httpd_confdir}/%{module}.conf


%changelog
* Wed Oct 12 2016 Carl George <carl.george@rackspace.com> - 2.0.14-1.ius
- Rebuild against uwsgi 2.0.14

* Wed Aug 10 2016 Carl George <carl.george@rackspace.com> - 2.0.13.1-1.ius
- Rebuild against uwsgi 2.0.13.1
- Remove Patch0

* Thu Jun 30 2016 Carl George <carl.george@rackspace.com> - 2.0.12-1.ius
- Initial package
- Add Patch0 to fix gh#1244
