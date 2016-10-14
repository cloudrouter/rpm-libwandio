#
# spec file for package libwandio
#
# Copyright (c) 2016, Martin Hauke <mardnh@gmx.de>
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           libwandio
Version:        1.0.4
Release:        1%{?dist}
Summary:        Multi-threaded file compression and decompression library
License:        GPL-2.0
Group:          System/Libraries
Url:            http://research.wand.net.nz/software/libwandio.php
Source:         http://research.wand.net.nz/software/wandio/wandio-%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  bzip2-devel
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  libcurl-devel
BuildRequires:  lzo-devel
BuildRequires:  make
BuildRequires:  xz-devel
BuildRequires:  zlib-devel
#BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
File I/O library that will read and write both compressed and uncompressed
files. All compression-related operations are performed in a separate thread
where possible resulting in significant performance gains for tasks where I/O
is the limiting factor (most simple trace analysis tasks are I/O-limited).

Libwandio is developed by the WAND Network Research Group at Waikato
University, New Zealand.

%package -n libwandio-devel
Summary: Development headers for the libwandio library
Group: Development/Libraries/Other
Requires: libwandio = %{version}-%{release}

%description -n libwandio-devel
This package contains development headers and other ancillary files for
the libwandio library.

Libwandio is a file I/O library that will read and write both compressed and
uncompressed files. All compression-related operations are performed in a
separate thread where possible resulting in significant performance gains for
tasks where I/O is the limiting factor (most simple trace analysis tasks are
I/O-limited).

Libwandio is developed by the WAND Network Research Group at Waikato
University, New Zealand.

%prep
%setup -q -n wandio-%{version}

%build
%configure --disable-static --disable-rpath

# https://fedoraproject.org/wiki/RPath_Packaging_Draft
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

make %{?_smp_mflags}

%install
make %{?_smp_mflags} DESTDIR=%{buildroot} install
find %{buildroot} -type f -name "*.la" -delete -print

%files
%defattr(-,root,root)
%doc AUTHORS COPYING COPYING.LESSER README
%{_bindir}/wandiocat
%{_libdir}/libwandio.so.*

%files -n libwandio-devel
%defattr(-,root,root)
%{_libdir}/libwandio.so
%{_includedir}/wandio.h

%changelog
* Fri Oct 14 2016 John Siegrist <john@complects.com> - 1.0.4-1
- Modifications for Fedora 24 and CentOS 7 packages.

* Sat Oct  8 2016 mardnh@gmx.de
- initial package, version 1.0.4
