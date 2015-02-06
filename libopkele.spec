%define	major 3
%define libname %mklibname opkele %{major}
%define develname %mklibname opkele -d

Summary:	C++ implementation of OpenID protocol
Name:		libopkele
Version:	2.0.4
Release:	6
Group:		System/Libraries
License:	MIT
URL:		http://kin.klever.net/libopkele/
Source0:	http://kin.klever.net/dist/%{name}-%{version}.tar.gz
Patch1:		libopkele-2.0.2-tidy-header.patch
Patch2:		libopkele-2.0.4-rosa-gcc47.patch
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
Provides:	opkele-devel = %{EVRD}

%description -n	%{develname}
libopkele is a C++ implementation of an OpenID decentralized identity system.
It provides OpenID protocol handling, leaving authentication and user
interaction to the implementor.

This package contains the static libopkele library and its header files.

%prep
%setup -q
%patch1 -p0
%patch2 -p1

%build
autoreconf -fi
%configure2_5x --disable-static
%make

%install
%makeinstall_std

%files -n %{libname}
%doc AUTHORS COPYING NEWS
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%dir %{_includedir}/opkele
%{_includedir}/opkele/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc


%changelog
* Sat Feb 11 2012 Oden Eriksson <oeriksson@mandriva.com> 2.0.4-4mdv2012.0
+ Revision: 773226
- various fixes
- relink against libpcre.so.1
- rebuild

* Mon Apr 19 2010 Funda Wang <fwang@mandriva.org> 2.0.4-2mdv2010.1
+ Revision: 536666
- rebuild

* Sat Dec 26 2009 Oden Eriksson <oeriksson@mandriva.com> 2.0.4-1mdv2010.1
+ Revision: 482381
- drop one redundant patch
- 2.0.4

* Thu Oct 08 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 2.0.3-2mdv2010.0
+ Revision: 455888
- rebuild for new curl SSL backend

* Wed Sep 02 2009 Oden Eriksson <oeriksson@mandriva.com> 2.0.3-1mdv2010.0
+ Revision: 424469
- 2.0.3

* Fri May 22 2009 Funda Wang <fwang@mandriva.org> 2.0.2-1mdv2010.0
+ Revision: 378648
- New version 2.0.2

* Sun Nov 23 2008 Oden Eriksson <oeriksson@mandriva.com> 2.0.1-1mdv2009.1
+ Revision: 305979
- 2.0.1

* Fri Jun 27 2008 Oden Eriksson <oeriksson@mandriva.com> 2.0-2mdv2009.0
+ Revision: 229521
- added a gcc43 patch (P0)
- %%make may not work here
- fix deps
- 2.0

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Sat Feb 02 2008 Funda Wang <fwang@mandriva.org> 0.3.2-3mdv2008.1
+ Revision: 161492
- rebuild against latest libpqxx

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

  + Oden Eriksson <oeriksson@mandriva.com>
    - fix deps
    - 0.3.2

* Wed Nov 21 2007 Oden Eriksson <oeriksson@mandriva.com> 0.3.1-1mdv2008.1
+ Revision: 110959
- 0.3.1

* Mon Oct 01 2007 Oden Eriksson <oeriksson@mandriva.com> 0.3-3mdv2008.0
+ Revision: 94141
- rebuilt due to missing packages

* Sun Sep 09 2007 Oden Eriksson <oeriksson@mandriva.com> 0.3-2mdv2008.0
+ Revision: 83688
- fix deps
- fix deps

* Wed Aug 22 2007 Oden Eriksson <oeriksson@mandriva.com> 0.3-1mdv2008.0
+ Revision: 68896
- 0.3
- new major
- conform to the 2008 specs


* Wed Jan 17 2007 Oden Eriksson <oeriksson@mandriva.com> 0.1.1-1mdv2007.0
+ Revision: 109979
- 0.1.1

* Mon Jan 15 2007 Oden Eriksson <oeriksson@mandriva.com> 0.1-1mdv2007.1
+ Revision: 109194
- fix deps
- Import libopkele

* Sun Jan 14 2007 Oden Eriksson <oeriksson@mandriva.com> 0.1-1mdv2007.1
- initial Mandriva package

