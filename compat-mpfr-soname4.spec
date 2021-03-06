#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x980C197698C3739D (vincent@vinc17.net)
#
Name     : compat-mpfr-soname4
Version  : 3.1.6
Release  : 28
URL      : https://ftp.gnu.org/gnu/mpfr/mpfr-3.1.6.tar.xz
Source0  : https://ftp.gnu.org/gnu/mpfr/mpfr-3.1.6.tar.xz
Source1 : https://ftp.gnu.org/gnu/mpfr/mpfr-3.1.6.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-3.0 LGPL-3.0
Requires: compat-mpfr-soname4-lib = %{version}-%{release}
Requires: compat-mpfr-soname4-license = %{version}-%{release}
BuildRequires : gmp-dev
BuildRequires : sed
# Suppress generation of debuginfo
%global debug_package %{nil}

%description
Contributed by the AriC and Caramba projects, INRIA.
This file is part of the GNU MPFR Library.

%package lib
Summary: lib components for the compat-mpfr-soname4 package.
Group: Libraries
Requires: compat-mpfr-soname4-license = %{version}-%{release}

%description lib
lib components for the compat-mpfr-soname4 package.


%package license
Summary: license components for the compat-mpfr-soname4 package.
Group: Default

%description license
license components for the compat-mpfr-soname4 package.


%prep
%setup -q -n mpfr-3.1.6

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1568224490
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-lto -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export FCFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-lto -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export FFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-lto -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export CXXFLAGS="$CXXFLAGS -O3 -falign-functions=32 -fno-lto -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1568224490
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/compat-mpfr-soname4
cp COPYING %{buildroot}/usr/share/package-licenses/compat-mpfr-soname4/COPYING
cp COPYING.LESSER %{buildroot}/usr/share/package-licenses/compat-mpfr-soname4/COPYING.LESSER
%make_install
## Remove excluded files
rm -f %{buildroot}/usr/share/doc/mpfr/AUTHORS
rm -f %{buildroot}/usr/share/doc/mpfr/BUGS
rm -f %{buildroot}/usr/share/doc/mpfr/COPYING
rm -f %{buildroot}/usr/share/doc/mpfr/COPYING.LESSER
rm -f %{buildroot}/usr/share/doc/mpfr/FAQ.html
rm -f %{buildroot}/usr/share/doc/mpfr/NEWS
rm -f %{buildroot}/usr/share/doc/mpfr/TODO
rm -f %{buildroot}/usr/share/doc/mpfr/examples/ReadMe
rm -f %{buildroot}/usr/share/doc/mpfr/examples/divworst.c
rm -f %{buildroot}/usr/share/doc/mpfr/examples/rndo-add.c
rm -f %{buildroot}/usr/share/doc/mpfr/examples/sample.c
rm -f %{buildroot}/usr/share/doc/mpfr/examples/version.c
rm -f %{buildroot}/usr/include/mpf2mpfr.h
rm -f %{buildroot}/usr/include/mpfr.h
rm -f %{buildroot}/usr/lib64/libmpfr.so
rm -f %{buildroot}/usr/share/info/mpfr.info

%files
%defattr(-,root,root,-)

%files lib
%defattr(-,root,root,-)
/usr/lib64/libmpfr.so.4
/usr/lib64/libmpfr.so.4.1.6

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/compat-mpfr-soname4/COPYING
/usr/share/package-licenses/compat-mpfr-soname4/COPYING.LESSER
