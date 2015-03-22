Name:		chef-gem-chef-encrypted-attributes
Version:	0.4.0
Release:	1%{?dist}
Summary:	chef-encrypted-attributes gem packaged for chef

Group:		chef-gems
License:	unknown
Source0:	https://rubygems.org/downloads/chef-encrypted-attributes-%{version}.gem
URL:		https://rubygems.org/gems/chef-encrypted-attributes/versions/%{version}
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

BuildRequires:	chef >= 11, chef < 12
Requires:	chef-gem-chef >= 11.4.0, chef-gem-chef < 13, chef-gem-ffi-yajl >= 1.0.0, chef-gem-ffi-yajl < 2.0.0

%description


%prep

%build

%install
rm -rf %{buildroot}
/opt/chef/embedded/bin/gem install -l  %{SOURCE0} --install-dir %{buildroot}/opt/chef/embedded/lib/ruby/gems/1.9.1/ --no-ri --no-rdoc -N  --ignore-dependencies

%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
/opt/chef/embedded/lib/ruby/gems/1.9.1/gems/chef-encrypted-attributes-%{version}
/opt/chef/embedded/lib/ruby/gems/1.9.1/specifications/chef-encrypted-attributes-%{version}.gemspec
/opt/chef/embedded/lib/ruby/gems/1.9.1/cache/chef-encrypted-attributes-%{version}.gem

%changelog

