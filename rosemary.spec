Name:           rosemary
Version:        0.2.0
Release:        1%{?dist}
Summary:        Compatibility layer and high level emulator hybrid for running macOS applications across operating systems and architectures

License:        GPL-3.0-only
URL:           https://github.com/microlift/rosemary
Source0:   {%url}/archive/refs/tags/v%{version}.tar.gz/%{name}-%{version}.tar.gz


BuildRequires:  SDL3-devel
BuildRequires:  cargo
BuildRequires: cargo-rpm-macros

Requires:       SDL3
Requires:       zlibrary
Requires:       curl


%description
%{summary}.

%prep
%autosetup -n %{name}-%{version}
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_build
%{cargo_license_summary -a}
%{cargo_license -a} > LICENSE.dependencies


%install
%cargo_install

%files




%changelog
* Sun Oct 11 2026 krzysiu
- Initial package
