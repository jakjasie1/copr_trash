Name:           butter
Version:        1.1.0
Release:        1%{?dist}
Summary:        A clean, sleek prefix and runtime manager for Rosemary

License:        GPL-3.0-or-later
URL:            https://github.com/microlift/butter
Source0:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cargo-rpm-macros

%description
%{summary}.

%prep
%autosetup
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_build
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies

%install
%cargo_install

%files
%{_bindir}/%{name}

%changelog
* Wed Oct 14 2026 jakjasie1
- Initial package.
