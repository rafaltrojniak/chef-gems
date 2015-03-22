Name:		chef-gem-mixlib-authentication
Version:	1.3.0
Release:	1%{?dist}
Summary:	Wrapper for chef package to propagate mixlib-authentication gem installed to yum

Group:		chef-gem
License:	unknown
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

Requires:	chef == 11.18.6

%description

%prep

%build

%install

%clean

%files

%changelog

