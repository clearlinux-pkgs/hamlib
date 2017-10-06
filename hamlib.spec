#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : hamlib
Version  : 3.1
Release  : 1
URL      : https://downloads.sourceforge.net/project/hamlib/hamlib/3.1/hamlib-3.1.tar.gz
Source0  : https://downloads.sourceforge.net/project/hamlib/hamlib/3.1/hamlib-3.1.tar.gz
Summary  : Library to control radio and rotator equipment.
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.1
Requires: hamlib-bin
Requires: hamlib-lib
Requires: hamlib-doc
BuildRequires : pkgconfig(libxml-2.0)

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


%prep
%setup -q -n hamlib-3.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1507305576
%configure --disable-static
make V=1  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1507305576
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

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
/usr/lib64/libhamlib++.so.2
/usr/lib64/libhamlib++.so.2.1.1
/usr/lib64/libhamlib.so.2
/usr/lib64/libhamlib.so.2.1.1
