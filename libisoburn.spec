Summary:	Multi-session filesystem extension to libisofs, libburn
Summary(pl.UTF-8):	Wielosesyjne rozszerzenie systemu plików do libisofs i libburn
Name:		libisoburn
Version:	1.4.0
Release:	1
License:	GPL v2+
Group:		Libraries
Source0:	http://files.libburnia-project.org/releases/%{name}-%{version}.tar.gz
# Source0-md5:	77bc6bcbe023ccd0fb210e341606dfbf
Patch0:		%{name}-link.patch
Patch1:		%{name}-info.patch
URL:		http://libburnia-project.org/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	libburn-devel >= %{version}
BuildRequires:	libisofs-devel >= %{version}
BuildRequires:	libjte-devel >= 1.0.0
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.9.0
BuildRequires:	readline-devel
BuildRequires:	texinfo
Requires:	libburn >= %{version}
Requires:	libisofs >= %{version}
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
Requires:	libburn-devel >= %{version}
Requires:	libisofs-devel >= %{version}
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

%package -n xorriso
Summary:	ISO 9660 Rock Ridge Filesystem Manipulator
Summary(pl.UTF-8):	Program do operacji na systemach plików ISO 9660 Rock Ridge
License:	GPL v3+
Group:		Applications
URL:		http://libburnia-project.org/wiki/Xorriso
Requires:	%{name} = %{version}-%{release}

%description -n xorriso
xorriso copies file objects from POSIX compliant filesystems into Rock
Ridge enhanced ISO 9660 filesystems and allows session-wise
manipulation of such filesystems. It can load the management
information of existing ISO images and it writes the session results
to optical media or to filesystem objects.

Vice versa xorriso is able to copy file objects out of ISO 9660
filesystems.

%description -n xorriso -l pl.UTF-8
xorriso kopiuje obiekty plików z systemów plików zgodnych z POSIX na
systemy plików ISO 9660 z rozszerzeniem Rock Ridge oraz pozwala na
operacje na tych systemach plików w ramach sesji. Potrafi wczytywać
informacje zarządzające z istniejących obrazów ISO i zapisuje wyniki
sesji na nośnik optyczny lub do obiektów systemu plików.

W drugą stronę xorriso potrafi kopiować obiekty plików z systemów
plików ISO 9660.

%package -n xorriso-gui
Summary:	Tcl/Tk based frontend that operates xorriso in dialog mode
Summary(pl.UTF-8):	Oparty na Tcl/Tk interfejs do obsługi xorriso w formie okien dialogowych
License:	BSD
Group:		X11/Applications
URL:		http://libburnia-project.org/wiki/Xorriso
Requires:	tk
Requires:	xorriso = %{version}-%{release}
Suggests:	tk-BWidget
Obsoletes:	libisoburn-gui
Obsoletes:	xorriso-tcltk

%description -n xorriso-gui
Tcl/Tk based frontend that operates xorriso in dialog mode.

%description -n xorriso-gui -l pl.UTF-8
Oparty na Tcl/Tk interfejs do obsługi xorriso w formie okien
dialogowych.

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

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post	xorriso -p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	xorriso -p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYRIGHT ChangeLog README TODO
%attr(755,root,root) %{_libdir}/libisoburn.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libisoburn.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libisoburn.so
%{_libdir}/libisoburn.la
%{_includedir}/libisoburn
%{_pkgconfigdir}/libisoburn-1.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libisoburn.a

%files -n xorriso
%defattr(644,root,root,755)
%doc xorriso/README_gnu_xorriso xorriso/changelog.txt
%attr(755,root,root) %{_bindir}/osirrox
%attr(755,root,root) %{_bindir}/xorrecord
%attr(755,root,root) %{_bindir}/xorriso
%attr(755,root,root) %{_bindir}/xorrisofs
%{_mandir}/man1/xorrecord.1*
%{_mandir}/man1/xorriso.1*
%{_mandir}/man1/xorrisofs.1*
%{_infodir}/xorrecord.info*
%{_infodir}/xorriso.info*
%{_infodir}/xorrisofs.info*

%files -n xorriso-gui
%defattr(644,root,root,755)
%doc frontend/README-tcltk
%attr(755,root,root) %{_bindir}/xorriso-tcltk
