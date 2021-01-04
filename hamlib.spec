#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xF72625E2EDBED598 (n0nb@n0nb.us)
#
Name     : hamlib
Version  : 4.0
Release  : 33
URL      : https://sourceforge.net/projects/hamlib/files/hamlib/4.0/hamlib-4.0.tar.gz
Source0  : https://sourceforge.net/projects/hamlib/files/hamlib/4.0/hamlib-4.0.tar.gz
Source1  : https://sourceforge.net/projects/hamlib/files/hamlib/4.0/hamlib-4.0.tar.gz.asc
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
BuildRequires : buildreq-cpan
BuildRequires : libusb-dev
BuildRequires : ncurses-dev
BuildRequires : pkgconfig(libxml-2.0)
BuildRequires : python3-dev
BuildRequires : readline-dev
BuildRequires : swig
BuildRequires : usrbinpython
Patch1: 0001-Use-vendor_install-for-Perl-bindings.patch

%description
Hamlib - (C) Frank Singleton 2000 (vk3fcs@ix.netcom.com)
(C) Stephane Fillod 2000-2011
(C) The Hamlib Group 2000-2012

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
%setup -q -n hamlib-4.0
cd %{_builddir}/hamlib-4.0
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1609798842
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
%configure --disable-static --with-perl-binding --with-python-binding
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1609798842
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/hamlib
cp %{_builddir}/hamlib-4.0/COPYING %{buildroot}/usr/share/package-licenses/hamlib/4cc77b90af91e615a64ae04893fdffa7939db84c
cp %{_builddir}/hamlib-4.0/COPYING.LIB %{buildroot}/usr/share/package-licenses/hamlib/01a6b4bf79aca9b556822601186afab86e8c4fbf
cp %{_builddir}/hamlib-4.0/LICENSE %{buildroot}/usr/share/package-licenses/hamlib/ce398a28bbe3ecfc23e5d33a446edd994121507b
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/ampctl
/usr/bin/ampctld
/usr/bin/rigctl
/usr/bin/rigctlcom
/usr/bin/rigctld
/usr/bin/rigmem
/usr/bin/rigsmtr
/usr/bin/rigswr
/usr/bin/rotctl
/usr/bin/rotctld

%files dev
%defattr(-,root,root,-)
/usr/include/hamlib/ampclass.h
/usr/include/hamlib/amplifier.h
/usr/include/hamlib/amplist.h
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
%doc /usr/share/doc/hamlib/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/libhamlib++.so.4
/usr/lib64/libhamlib++.so.4.0.0
/usr/lib64/libhamlib.so.4
/usr/lib64/libhamlib.so.4.0.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/hamlib/01a6b4bf79aca9b556822601186afab86e8c4fbf
/usr/share/package-licenses/hamlib/4cc77b90af91e615a64ae04893fdffa7939db84c
/usr/share/package-licenses/hamlib/ce398a28bbe3ecfc23e5d33a446edd994121507b

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/ampctl.1
/usr/share/man/man1/ampctld.1
/usr/share/man/man1/rigctl.1
/usr/share/man/man1/rigctlcom.1
/usr/share/man/man1/rigctld.1
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
/usr/lib/perl5/vendor_perl/5.30.3/x86_64-linux-thread-multi/Hamlib.pm
/usr/lib/perl5/vendor_perl/5.30.3/x86_64-linux-thread-multi/auto/Hamlib/.packlist
/usr/lib/perl5/vendor_perl/5.30.3/x86_64-linux-thread-multi/auto/Hamlib/Hamlib.so
/usr/lib/perl5/vendor_perl/5.30.3/x86_64-linux-thread-multi/perltest.pl

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
