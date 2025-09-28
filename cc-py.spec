Name:           cc-py
Version:        1.10
Release:        1%{?dist}
Summary:        Convert Windows cursors to Linux-compatible formats.

License:        CC0-1.0
URL:            https://github.com/keiaa-75/cc.py
Source:         %{url}/archive/v%{version}/cc.py-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
Requires: python3-certifi

%description %_description


%prep
%autosetup -p1 -n cc.py-%{version}


%generate_buildrequires
%pyproject_buildrequires -t


%build
%pyproject_wheel


%install
%pyproject_install


%check
%tox


# Note that there is no %%files section for
# the unversioned python module, python-pello.

# For python3-pello, %%{pyproject_files} handles code files and %%license,
# but executables and documentation must be listed in the spec file:

%files -n ccpy -f %{pyproject_files}
%doc README.md
%{_bindir}/ccpy


%changelog
* Sun 28 Sep 2025 jakjasie1
- Initial rpm 
