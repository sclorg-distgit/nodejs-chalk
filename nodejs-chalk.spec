%{?scl:%scl_package nodejs-chalk}
%{!?scl:%global pkg_name %{name}}

%{?nodejs_find_provides_and_requires}

# Tests fail inside Koji due to terminal environment.
%global enable_tests 0

Name:       %{?scl_prefix}nodejs-chalk
Version:    1.1.1
Release:    8%{?dist}
Summary:    Terminal string styling done right
License:    MIT
Group:      System Environment/Libraries
URL:        https://github.com/sindresorhus/chalk
Source0:    http://registry.npmjs.org/chalk/-/chalk-%{version}.tgz
Source1:    https://raw.github.com/sindresorhus/chalk/0a33a270b1e00ae4dea31b8ca368056d6823a148/test.js

BuildArch:  noarch
%if 0%{?fedora} >= 19
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
%else
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
%endif

BuildRequires:  %{?scl_prefix}nodejs-devel

%if 0%{?enable_tests}
BuildRequires:  %{?scl_prefix}npm(mocha)
BuildRequires:  %{?scl_prefix}npm(ansi-styles)
BuildRequires:  %{?scl_prefix}npm(has-color)
BuildRequires:  %{?scl_prefix}npm(strip-ansi)
%endif

%description
%{summary}.

%prep
%setup -q -n package
cp -p %{SOURCE1} .

%nodejs_fixdep has-color '>=0.1'
%nodejs_fixdep supports-color '>=2.0'
%nodejs_fixdep escape-string-regexp '>=1.0'
%nodejs_fixdep ansi-styles '>=1.0'
%nodejs_fixdep strip-ansi '>=0.1'
%nodejs_fixdep has-ansi '>=2.0'

%build
#nothing to do

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/chalk
cp -pr package.json index.js \
    %{buildroot}%{nodejs_sitelib}/chalk

%nodejs_symlink_deps


%if 0%{?enable_tests}

%check
%nodejs_symlink_deps --check
/usr/bin/mocha
%endif

%files
%doc license readme.md
%{nodejs_sitelib}/chalk

%changelog
* Tue Feb 16 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.1.1-8
- Use proper macro in -runtime dependency

* Sun Feb 14 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.1.1-4
- Rebuilt with updated metapackage

* Wed Jan 06 2016 Tomas Hrcka <thrcka@redhat.com> - 1.1.1-3
- Enable scl macros

* Mon Sep 14 2015 Troy Dawson <tdawson@redhat.com> - 1.1.1-2
- Fixup dependencies

* Mon Sep 14 2015 Troy Dawson <tdawson@redhat.com> - 1.1.1-1
- Update to 1.1.1
- Remove tests until all dependencies are built

* Sun Apr 20 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.4.0-2
- fix versioned dependencies

* Thu Mar 13 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.4.0-1
- initial package
