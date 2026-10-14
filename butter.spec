%define app_id io.github.microlift.butter

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
	install -Dm644 data/%{app_id}.desktop %{_datadir}/applications/%{app_id}.desktop
	install -Dm644 data/%{app_id}.metainfo.xml %{_datadir}/metainfo/%{app_id}.metainfo.xml
	install -Dm644 data/icons/hicolor/scalable/apps/%{app_id}.svg \
		%{_datadir}/icons/hicolor/scalable/apps/%{app_id}.svg
	install -Dm644 data/icons/hicolor/symbolic/apps/%{app_id}-symbolic.svg \
		%{_datadir}/icons/hicolor/symbolic/apps/%{app_id}-symbolic.svg

%files
%{_bindir}/%{name}
%{_datadir}/applications/%{app_id}.desktop
%{_datadir}/metainfo/%{app_id}.metainfo.xml
%{_datadir}/icons/hicolor/scalable/apps/%{app_id}.svg
%{_datadir}/icons/hicolor/symbolic/apps/%{app_id}-symbolic.svg
  
%changelog
* Wed Oct 14 2026 jakjasie1
- Initial package.
