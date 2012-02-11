%define	major 3
%define libname %mklibname opkele %{major}
%define develname %mklibname opkele -d

Summary:	C++ implementation of OpenID protocol
Name:		libopkele
Version:	2.0.4
Release:	%mkrel 4
Group:		System/Libraries
License:	MIT
URL:		http://kin.klever.net/libopkele/
Source0:	http://kin.klever.net/dist/%{name}-%{version}.tar.gz
Patch1:		libopkele-2.0.2-tidy-header.patch
BuildRequires:	autoconf automake libtool
BuildRequires:	curl-devel
BuildRequires:	doxygen
BuildRequires:	ext2fs-devel
BuildRequires:	expat-devel
BuildRequires:	graphviz
BuildRequires:	konforka-devel
BuildRequires:	libpqxx-devel
BuildRequires:	libxslt-proc
BuildRequires:	openssl-devel
BuildRequires:	pcre-devel
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
Provides:	opkele-devel = %{version}-%{release}
Provides:	%{name} = %{version}-%{release}
Obsoletes:	%{mklibname opkele 1 -d}
Conflicts:	%{mklibname opkele 2 -d}

%description -n	%{develname}
libopkele is a C++ implementation of an OpenID decentralized identity system.
It provides OpenID protocol handling, leaving authentication and user
interaction to the implementor.

This package contains the static libopkele library and its header files.

%prep
%setup -q -n %{name}-%{version}
%patch1 -p0

%build
autoreconf -fi
%configure2_5x
%make

%install
rm -rf %{buildroot}

%makeinstall_std

# cleanups
rm -f %{buildroot}%{_libdir}/*.*a

%files -n %{libname}
%doc AUTHORS COPYING NEWS
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%dir %{_includedir}/opkele
%{_includedir}/opkele/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
