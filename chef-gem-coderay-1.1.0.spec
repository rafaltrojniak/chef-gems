Name:		chef-gem-coderay
Version:	1.1.0
Release:	1%{?dist}
Summary:	Wrapper for chef package to propagate coderay gem installed to yum

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

