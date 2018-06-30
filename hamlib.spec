#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xFB2C5130D55A8819 (n0nb@n0nb.us)
#
Name     : hamlib
Version  : 3.2
Release  : 7
URL      : https://sourceforge.net/projects/hamlib/files/hamlib/3.2/hamlib-3.2.tar.gz
Source0  : https://sourceforge.net/projects/hamlib/files/hamlib/3.2/hamlib-3.2.tar.gz
Source99 : https://sourceforge.net/projects/hamlib/files/hamlib/3.2/hamlib-3.2.tar.gz.asc
Summary  : Library to control radio and rotator equipment.
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.1
Requires: hamlib-bin
Requires: hamlib-lib
Requires: hamlib-python3
Requires: hamlib-doc
Requires: hamlib-python
BuildRequires : libusb-dev
BuildRequires : ncurses-dev
BuildRequires : pkgconfig(libxml-2.0)
BuildRequires : python3-dev
BuildRequires : readline-dev
BuildRequires : swig
BuildRequires : usrbinpython

%description
Hamlib - (C) Frank Singleton 2000 (vk3fcs@ix.netcom.com)
(C) Stephane Fillod 2000-2011
(C) The Hamlib Group 2000-2012

%package bin
Summary: bin components for the hamlib package.
Group: Binaries

%description bin
bin components for the hamlib package.


%package dev
Summary: dev components for the hamlib package.
Group: Development
Requires: hamlib-lib
Requires: hamlib-bin
Provides: hamlib-devel

%description dev
dev components for the hamlib package.


%package doc
Summary: doc components for the hamlib package.
Group: Documentation

%description doc
doc components for the hamlib package.


%package lib
Summary: lib components for the hamlib package.
Group: Libraries

%description lib
lib components for the hamlib package.


%package python
Summary: python components for the hamlib package.
Group: Default
Requires: hamlib-python3

%description python
python components for the hamlib package.


%package python3
Summary: python3 components for the hamlib package.
Group: Default
Requires: python3-core

%description python3
python3 components for the hamlib package.


%prep
%setup -q -n hamlib-3.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1522596178
%configure --disable-static --with-perl-binding --with-python-binding
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1522596178
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)
/usr/lib/perl5/site_perl/5.26.1/x86_64-linux-thread-multi/Hamlib.pm
/usr/lib/perl5/site_perl/5.26.1/x86_64-linux-thread-multi/auto/Hamlib/.packlist
/usr/lib/perl5/site_perl/5.26.1/x86_64-linux-thread-multi/perltest.pl

%files bin
%defattr(-,root,root,-)
/usr/bin/rigctl
/usr/bin/rigctld
/usr/bin/rigmem
/usr/bin/rigsmtr
/usr/bin/rigswr
/usr/bin/rotctl
/usr/bin/rotctld

%files dev
%defattr(-,root,root,-)
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
%defattr(-,root,root,-)
%doc /usr/share/doc/hamlib/*
%doc /usr/share/info/*
%doc /usr/share/man/man1/*

%files lib
%defattr(-,root,root,-)
/usr/lib/perl5/site_perl/5.26.1/x86_64-linux-thread-multi/auto/Hamlib/Hamlib.so
/usr/lib64/libhamlib++.so.2
/usr/lib64/libhamlib++.so.2.1.2
/usr/lib64/libhamlib.so.2
/usr/lib64/libhamlib.so.2.1.2

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
