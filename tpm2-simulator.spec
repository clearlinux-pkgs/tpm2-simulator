#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : tpm2-simulator
Version  : 1
Release  : 5
URL      : https://sourceforge.net/projects/ibmswtpm2/files/ibmtpm1332.tar.gz
Source0  : https://sourceforge.net/projects/ibmswtpm2/files/ibmtpm1332.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : CPL-1.0
Requires: tpm2-simulator-bin = %{version}-%{release}
BuildRequires : openssl-dev
Patch1: 0001-TPMSimulator-fix-compile-issue-for-clear-linux.patch

%description
No detailed description available

%package bin
Summary: bin components for the tpm2-simulator package.
Group: Binaries

%description bin
bin components for the tpm2-simulator package.


%prep
%setup -q -c -n ibmtpm1332.tar
cd %{_builddir}/ibmtpm1332.tar
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1576521643
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
pushd src
make  %{?_smp_mflags}
popd


%install
export SOURCE_DATE_EPOCH=1576521643
rm -rf %{buildroot}
pushd src
%make_install
popd

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/tpm_server
