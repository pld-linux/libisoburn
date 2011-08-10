Summary:	Multi-session filesystem extension to libisofs, libburn
Summary(pl.UTF-8):	Wielosesyjne rozszerzenie systemu plików do libisofs i libburn
Name:		libisoburn
Version:	1.1.4
Release:	1
License:	GPL v2+
Group:		Libraries
Source0:	http://files.libburnia-project.org/releases/%{name}-%{version}.tar.gz
# Source0-md5:	db79a0f0622077bb1a901f57cc1e2b67
Patch0:		%{name}-link.patch
Patch1:		%{name}-info.patch
URL:		http://libburnia-project.org/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	libburn-devel >= 1.1.4
BuildRequires:	libisofs-devel >= 1.1.4
BuildRequires:	libjte-devel >= 1.0.0
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.9.0
BuildRequires:	readline-devel
BuildRequires:	texinfo
Requires:	libburn >= 1.1.4
Requires:	libisofs >= 1.1.4
Requires:	libjte >= 1.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libisoburn is a frontend for libraries libburn and libisofs which
enables creation and expansion of ISO-9660 filesystems on all CD/DVD
media supported by libburn. This includes media like DVD+RW, which do
not support multi-session management on media level and even plain
disk files or block devices.

The price for that is thorough specialization on data files in
ISO-9660 filesystem images. So libisoburn is not suitable for audio
(CD-DA) or any other CD layout which does not entirely consist of
ISO-9660 sessions.

%description -l pl.UTF-8
libisoburn to frontend do bibliotek libburn i libisofs umożliwiający
tworzenie i rozszerzanie systemów plików ISO-9660 na wszystkich
nośnikach CD/DVD obsługiwanych przez libburn. Obejmuje to nośniki
takie jak DVD+RW, które nie mają zarządzania wieloma sesjami na
poziomie nośnika, a nawet zwykłe pliki dyskowe czy urządzenia blokowe.

Ceną za to jest całkowite skupienie na plikach danych na obrazach
systemu plików ISO-9660. Przez to libisoburn nie nadaje się do płyt
muzycznych (CD-DA) ani żadnego innego układu CD nie składającego się w
całości z sesji ISO-9660.

%package devel
Summary:	Header files for libisoburn library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libisoburn
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libburn-devel >= 1.1.4
Requires:	libisofs-devel >= 1.1.4
Requires:	libjte-devel >= 1.0.0

%description devel
Header files for libisoburn library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libisoburn.

%package static
Summary:	Static libisoburn library
Summary(pl.UTF-8):	Statyczna biblioteka libisoburn
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libisoburn library.

%description static -l pl.UTF-8
Statyczna biblioteka libisoburn.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/postshell
/sbin/ldconfig
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun -p /sbin/postshell
/sbin/ldconfig
-/usr/sbin/fix-info-dir -c %{_infodir}

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYRIGHT ChangeLog README TODO
%attr(755,root,root) %{_bindir}/osirrox
%attr(755,root,root) %{_bindir}/xorrecord
%attr(755,root,root) %{_bindir}/xorriso
%attr(755,root,root) %{_bindir}/xorrisofs
%attr(755,root,root) %{_libdir}/libisoburn.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libisoburn.so.1
%{_mandir}/man1/xorriso.1*
%{_mandir}/man1/xorrisofs.1*
%{_infodir}/xorriso.info*
%{_infodir}/xorrisofs.info*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libisoburn.so
%{_libdir}/libisoburn.la
%{_includedir}/libisoburn
%{_pkgconfigdir}/libisoburn-1.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libisoburn.a
