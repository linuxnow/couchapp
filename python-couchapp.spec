# sitelib for noarch packages, sitearch for others (remove the unneeded one)
%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}
%{!?python_sitearch: %global python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")}

%define srcname couchapp

Name:           python-%{srcname}
Version:        0.8.1
Release:        1%{?dist}
Summary:        Standalone CouchDB Application Development Made Simple

Group:          Development/Libraries
License:        Apache License 2
URL:            http://github.com/couchapp/couchapp/tree/master
Source0:        %{srcname}-%{version}.tar.bz2

BuildArch:      x86_64
BuildRequires:  python-devel python-setuptools
BuildRequires:  python-setuptools

%description
CouchApp is a set of helpers and a jQuery plugin that conspire to get you up
and running on CouchDB quickly and correctly. It brings clarity and order to
the freedom of CouchDB's document-based approach.

%prep
%setup -q -n %{srcname}-%{version}


%build
# Remove CFLAGS=... for noarch packages (unneeded)
CFLAGS="$RPM_OPT_FLAGS" %{__python} setup.py build


%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc LICENSE NOTICE README.rst THANKS
%{_bindir}/couchapp
# For noarch packages: sitelib
# %{python_sitelib}/*
# For arch-specific packages: sitearch
%{python_sitearch}/*

%changelog
* Mon Jul 18 2011 Pau Aliagas <linuxnow@gmail.com> 0.8.1-1
- Initial version
