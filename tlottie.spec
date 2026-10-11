%bcond check 0

Name:           tlottie
Version:        1.0.6
Release:        1%{?dist}
Summary:        Library for rendering Lottie animations

License:        MIT
URL:            https://github.com/dkaraush/tlottie
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
# Enable cargo-c and install the upstream C header.
Patch0:         tlottie-cargo-c.patch

BuildRequires:  cargo-rpm-macros >= 26
BuildRequires:  cargo-c
BuildRequires:  gcc

%description
Tlottie is a library for rendering Lottie animations, written in Rust
and providing a C-compatible API.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Header and library files for developing applications that use %{name}.

%prep
%autosetup -p1
%cargo_prep

%build
%{cargo_cbuild} --library-type cdylib

%install
%{cargo_cinstall} --library-type cdylib

%if %{with check}
%check
%cargo_test -f capi
%endif

%files
%license LICENSE
%doc README.md
%{_libdir}/lib%{name}.so.*

%files devel
%{_includedir}/%{name}.h
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
* Sun Oct 11 2026 Ivan Romanov <drizt72@zoho.eu> - 1.0.6-1
- Initial package using cargo-c
