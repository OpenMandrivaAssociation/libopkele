%define	major 3
%define libname %mklibname opkele %{major}
%define develname %mklibname opkele -d

Summary:	C++ implementation of OpenID protocol
Name:		libopkele
Version:	2.0
Release:	%mkrel 1
Group:		System/Libraries
License:	MIT
URL:		http://kin.klever.net/libopkele/
Source0:	http://kin.klever.net/dist/%{name}-%{version}.tar.gz
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	curl-devel
BuildRequires:	doxygen
BuildRequires:	e2fsprogs-devel
BuildRequires:	expat-devel
BuildRequires:	graphviz
BuildRequires:	konforka-devel
BuildRequires:	libpqxx-devel
BuildRequires:	libtool
BuildRequires:	libxslt-proc
BuildRequires:	openssl-devel
BuildRequires:	pcre-devel
BuildRequires:	pkgconfig
BuildRequires:	postgresql-devel
BuildRequires:	sqlite3-devel
BuildRequires:	tidy-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

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
Obsoletes:	%{mklibname opkele 2 -d}

%description -n	%{develname}
libopkele is a C++ implementation of an OpenID decentralized identity system.
It provides OpenID protocol handling, leaving authentication and user
interaction to the implementor.

This package contains the static libopkele library and its header files.

%prep

%setup -q -n %{name}-%{version}

perl -pi -e "s|tidy/tidy\.h|tidy\.h|g" configure*

%build
export WANT_AUTOCONF_2_5=1
rm -f configure
libtoolize --copy --force; aclocal; autoheader; automake --add-missing --copy; autoconf --force

%configure2_5x \
    --with-pkgconfigdir=%{_libdir}/pkgconfig

%make

%install
rm -rf %{buildroot}

%makeinstall_std

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%clean
rm -rf %{buildroot}

%files -n %{libname}
%defattr(-,root,root)
%doc AUTHORS COPYING NEWS
%{_libdir}/*.so.*

%files -n %{develname}
%defattr(-,root,root)
%dir %{_includedir}/opkele
%{_includedir}/opkele/*
%{_libdir}/*.so
%{_libdir}/*.a
%{_libdir}/*.la
%{_libdir}/pkgconfig/*.pc
