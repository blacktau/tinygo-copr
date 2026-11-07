# Repackage of the upstream TinyGo prebuilt Linux binary release.
# The distribution is self-contained (bundled LLVM/lld, lib, src, targets),
# so RPM must not strip, make debuginfo, or auto-scan the bundled files.
%global debug_package %{nil}
%global __brp_strip %{nil}
%global __brp_strip_static_archive %{nil}
%global __brp_strip_comment_note %{nil}
%global __brp_strip_lto %{nil}
%global __brp_check_rpaths %{nil}
%global __os_install_post %{nil}

# Do not generate Provides/Requires from the bundled binaries/libraries.
%global __provides_exclude_from ^%{_libdir}/tinygo/.*$
%global __requires_exclude_from ^%{_libdir}/tinygo/.*$

Name:           tinygo
Version:        0.44.0
Release:        1%{?dist}
Summary:        Go compiler for small places

# tinygo core is BSD-3-Clause; the binary release bundles LLVM and other
# runtime libraries under their respective licenses.
License:        BSD-3-Clause AND Apache-2.0 WITH LLVM-exception AND MIT
URL:            https://tinygo.org
Source0:        https://github.com/tinygo-org/tinygo/releases/download/v%{version}/tinygo%{version}.linux-amd64.tar.gz

ExclusiveArch:  x86_64

Provides:       tinygo = %{version}-%{release}

# TinyGo shells out to the Go toolchain at build time (standard library, go
# command); without it `tinygo build` fails with "go version <unknown>".
# golang also pulls in gcc, needed for linking native/host targets.
Requires:       golang

%description
TinyGo is a Go compiler for small places: microcontrollers, WebAssembly, and
command-line tools. This package repackages the official upstream prebuilt
Linux binary release; it is self-contained and does not use the system LLVM.

%prep
%autosetup -n tinygo

%build
# Nothing to build: this wraps prebuilt binaries.

%install
mkdir -p %{buildroot}%{_libdir}/tinygo
cp -a . %{buildroot}%{_libdir}/tinygo/
mkdir -p %{buildroot}%{_bindir}
ln -sr %{buildroot}%{_libdir}/tinygo/bin/tinygo %{buildroot}%{_bindir}/tinygo

%files
%{_libdir}/tinygo
%{_bindir}/tinygo

%changelog
* Sat Nov 07 2026 Sean Garrett <sean+claude@blacktau.com> - 0.44.0-1
- Update to upstream 0.44.0

* Mon Jul 06 2026 Sean Garrett <sean+claude@blacktau.com> - 0.41.1-1
- Initial COPR package repackaging the upstream 0.41.1 Linux binary release
