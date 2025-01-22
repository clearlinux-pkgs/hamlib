#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: configure_ac
# autospec version: v21
# autospec commit: 94c6be0
#
# Source0 file verified with key 0xFB2C5130D55A8819 (n0nb@n0nb.us)
#
Name     : hamlib
Version  : 4.6.1
Release  : 76
URL      : https://sourceforge.net/projects/hamlib/files/hamlib/4.6.1/hamlib-4.6.1.tar.gz
Source0  : https://sourceforge.net/projects/hamlib/files/hamlib/4.6.1/hamlib-4.6.1.tar.gz
Source1  : https://sourceforge.net/projects/hamlib/files/hamlib/4.6.1/hamlib-4.6.1.tar.gz.asc
Source2  : FB2C5130D55A8819.pkey
Summary  : Library to control radio and rotator equipment.
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.1
Requires: hamlib-bin = %{version}-%{release}
Requires: hamlib-lib = %{version}-%{release}
Requires: hamlib-license = %{version}-%{release}
Requires: hamlib-man = %{version}-%{release}
Requires: hamlib-perl = %{version}-%{release}
Requires: hamlib-python = %{version}-%{release}
Requires: hamlib-python3 = %{version}-%{release}
BuildRequires : file
BuildRequires : gnupg
BuildRequires : ncurses-dev
BuildRequires : pkgconfig(libusb-1.0)
BuildRequires : pkgconfig(libxml-2.0)
BuildRequires : pkgconfig(tcl)
BuildRequires : python3-dev
BuildRequires : readline-dev
BuildRequires : swig
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
Patch1: 0001-Use-vendor_install-for-Perl-bindings.patch

%description


%package bin
Summary: bin components for the hamlib package.
Group: Binaries
Requires: hamlib-license = %{version}-%{release}

%description bin
bin components for the hamlib package.


%package dev
Summary: dev components for the hamlib package.
Group: Development
Requires: hamlib-lib = %{version}-%{release}
Requires: hamlib-bin = %{version}-%{release}
Provides: hamlib-devel = %{version}-%{release}
Requires: hamlib = %{version}-%{release}

%description dev
dev components for the hamlib package.


%package doc
Summary: doc components for the hamlib package.
Group: Documentation
Requires: hamlib-man = %{version}-%{release}

%description doc
doc components for the hamlib package.


%package lib
Summary: lib components for the hamlib package.
Group: Libraries
Requires: hamlib-license = %{version}-%{release}

%description lib
lib components for the hamlib package.


%package license
Summary: license components for the hamlib package.
Group: Default

%description license
license components for the hamlib package.


%package man
Summary: man components for the hamlib package.
Group: Default

%description man
man components for the hamlib package.


%package perl
Summary: perl components for the hamlib package.
Group: Default
Requires: hamlib = %{version}-%{release}

%description perl
perl components for the hamlib package.


%package python
Summary: python components for the hamlib package.
Group: Default
Requires: hamlib-python3 = %{version}-%{release}

%description python
python components for the hamlib package.


%package python3
Summary: python3 components for the hamlib package.
Group: Default
Requires: python3-core

%description python3
python3 components for the hamlib package.


%prep
mkdir .gnupg
chmod 700 .gnupg
gpg --homedir .gnupg --import %{SOURCE2}
gpg --homedir .gnupg --status-fd 1 --verify %{SOURCE1} %{SOURCE0} > gpg.status
grep -E '^\[GNUPG:\] (GOODSIG|EXPKEYSIG) FB2C5130D55A8819' gpg.status
%setup -q -n hamlib-4.6.1
cd %{_builddir}/hamlib-4.6.1
%patch -P 1 -p1
pushd ..
cp -a hamlib-4.6.1 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1737562149
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%reconfigure --disable-static --with-perl-binding --with-python-binding
make  %{?_smp_mflags}
unset PKG_CONFIG_PATH
pushd ../buildavx2/
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
%reconfigure --disable-static --with-perl-binding --with-python-binding
make  %{?_smp_mflags}
popd

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check
cd ../buildavx2;
make %{?_smp_mflags} check || :

%install
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1737562149
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/hamlib
cp %{_builddir}/hamlib-%{version}/COPYING %{buildroot}/usr/share/package-licenses/hamlib/4cc77b90af91e615a64ae04893fdffa7939db84c || :
cp %{_builddir}/hamlib-%{version}/COPYING.LIB %{buildroot}/usr/share/package-licenses/hamlib/01a6b4bf79aca9b556822601186afab86e8c4fbf || :
export GOAMD64=v2
GOAMD64=v3
pushd ../buildavx2/
%make_install_v3
popd
GOAMD64=v2
%make_install
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/ampctl
/V3/usr/bin/ampctld
/V3/usr/bin/rigctl
/V3/usr/bin/rigctlcom
/V3/usr/bin/rigctld
/V3/usr/bin/rigctlsync
/V3/usr/bin/rigctltcp
/V3/usr/bin/rigfreqwalk
/V3/usr/bin/rigmem
/V3/usr/bin/rigsmtr
/V3/usr/bin/rigswr
/V3/usr/bin/rigtestlibusb
/V3/usr/bin/rigtestmcast
/V3/usr/bin/rigtestmcastrx
/V3/usr/bin/rotctl
/V3/usr/bin/rotctld
/usr/bin/ampctl
/usr/bin/ampctld
/usr/bin/rigctl
/usr/bin/rigctlcom
/usr/bin/rigctld
/usr/bin/rigctlsync
/usr/bin/rigctltcp
/usr/bin/rigfreqwalk
/usr/bin/rigmem
/usr/bin/rigsmtr
/usr/bin/rigswr
/usr/bin/rigtestlibusb
/usr/bin/rigtestmcast
/usr/bin/rigtestmcastrx
/usr/bin/rotctl
/usr/bin/rotctld

%files dev
%defattr(-,root,root,-)
/usr/include/hamlib/ampclass.h
/usr/include/hamlib/amplifier.h
/usr/include/hamlib/amplist.h
/usr/include/hamlib/multicast.h
/usr/include/hamlib/rig.h
/usr/include/hamlib/rig_dll.h
/usr/include/hamlib/rigclass.h
/usr/include/hamlib/riglist.h
/usr/include/hamlib/rotator.h
/usr/include/hamlib/rotclass.h
/usr/include/hamlib/rotlist.h
/usr/lib64/libhamlib++.so
/usr/lib64/libhamlib.so
/usr/lib64/pkgconfig/hamlib.pc
/usr/share/aclocal/*.m4

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/hamlib/*

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libhamlib++.so.4.0.6
/V3/usr/lib64/libhamlib.so.4.0.6
/usr/lib64/libhamlib++.so.4
/usr/lib64/libhamlib++.so.4.0.6
/usr/lib64/libhamlib.so.4
/usr/lib64/libhamlib.so.4.0.6

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/hamlib/01a6b4bf79aca9b556822601186afab86e8c4fbf
/usr/share/package-licenses/hamlib/4cc77b90af91e615a64ae04893fdffa7939db84c

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/ampctl.1
/usr/share/man/man1/ampctld.1
/usr/share/man/man1/rigctl.1
/usr/share/man/man1/rigctlcom.1
/usr/share/man/man1/rigctld.1
/usr/share/man/man1/rigctlsync.1
/usr/share/man/man1/rigmem.1
/usr/share/man/man1/rigsmtr.1
/usr/share/man/man1/rigswr.1
/usr/share/man/man1/rotctl.1
/usr/share/man/man1/rotctld.1
/usr/share/man/man7/hamlib-primer.7
/usr/share/man/man7/hamlib-utilities.7
/usr/share/man/man7/hamlib.7

%files perl
%defattr(-,root,root,-)
/V3/usr/lib/perl5/*
/usr/lib/perl5/*

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/V3/usr/lib/python3*/*
/usr/lib/python3*/*
