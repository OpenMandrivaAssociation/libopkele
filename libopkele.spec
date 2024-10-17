%define	major 3
%define libname %mklibname opkele %{major}
%define develname %mklibname opkele -d

Summary:	C++ implementation of OpenID protocol
Name:		libopkele
Version:	2.0.4
Release:	7
Group:		System/Libraries
License:	MIT
URL:		https://kin.klever.net/libopkele/
Source0:	http://kin.klever.net/dist/%{name}-%{version}.tar.gz
Patch1:		libopkele-2.0.2-tidy-header.patch
Patch2:		libopkele-2.0.4-rosa-gcc47.patch
Patch3:		libopkele-openssl-3.0.patch
BuildRequires:	autoconf automake libtool
BuildRequires:	curl-devel
BuildRequires:	doxygen
BuildRequires:	ext2fs-devel
BuildRequires:	expat-devel
BuildRequires:	graphviz
BuildRequires:	konforka-devel
BuildRequires:	pkgconfig(libpqxx)
BuildRequires:	libxslt-proc
BuildRequires:	pkgconfig(openssl)
BuildRequires:	pkgconfig(libpcre)
BuildRequires:	pkgconfig
BuildRequires:	postgresql-devel
BuildRequires:	sqlite3-devel
BuildRequires:	tidy-devel

%description
libopkele is a C++ implementation of an OpenID decentralized identity system.
It provides OpenID protocol handling, leaving authentication and user
interaction to the implementor.

%package -n	%{libname}
Summary:	C++ implementation of OpenID protocol
Group:          System/Libraries

%description -n	%{libname}
libopkele is a C++ implementation of an OpenID decentralized identity system.
It provides OpenID protocol handling, leaving authentication and user
interaction to the implementor.

%package -n	%{develname}
Summary:	Static library and header files for the libopkele library
Group:		Development/C++
Requires:	%{libname} = %{version}
Provides:	opkele-devel = %{EVRD}

%description -n	%{develname}
libopkele is a C++ implementation of an OpenID decentralized identity system.
It provides OpenID protocol handling, leaving authentication and user
interaction to the implementor.

This package contains the static libopkele library and its header files.

%prep
%autosetup -p1
autoreconf -fi
%configure

%build
%make_build

%install
%make_install

%files -n %{libname}
%doc AUTHORS COPYING NEWS
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%dir %{_includedir}/opkele
%{_includedir}/opkele/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
