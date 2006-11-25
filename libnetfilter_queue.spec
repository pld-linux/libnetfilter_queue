Summary:	netfilter userspace packet queueing library
Summary(pl):	Biblioteka kolejkowania pakietów w przestrzeni u¿ytkownika dla netfiltra
Name:		libnetfilter_queue
Version:	0.0.12
Release:	1
License:	GPL v2
Group:		Libraries
Source0:	ftp://ftp.netfilter.org/pub/libnetfilter_queue/%{name}-%{version}.tar.bz2
# Source0-md5:	873749d8a51928d971bb5eab1e204aec
URL:		http://www.netfilter.org/projects/libnetfilter_queue/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libnfnetlink-devel >= 0.0.16
BuildRequires:	libtool
Requires:	libnfnetlink >= 0.0.16
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libnetfilter_queue is a userspace library providing an API to packets
that have been queued by the kernel packet filter. It is is part of a
system that deprecates the old ip_queue/libipq mechanism.

%description -l pl
libnetfilter_queue to biblioteka przestrzeni u¿ytkownika
udostêpniaj±ca API do pakietów kolejkowanych przez filtr pakietów w
j±drze. Jest czê¶ci± systemu zastêpuj±cego stary mechanizm
ip_queue/libipq.

%package devel
Summary:	Header files for libnetfilter_queue library
Summary(pl):	Pliki nag³ówkowe biblioteki libnetfilter_queue
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libnfnetlink-devel >= 0.0.16

%description devel
Header files for libnetfilter_queue library.

%description devel -l pl
Pliki nag³ówkowe biblioteki libnetfilter_queue.

%package static
Summary:	Static libnetfilter_queue library
Summary(pl):	Statyczna biblioteka libnetfilter_queue
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libnetfilter_queue library.

%description static -l pl
Statyczna biblioteka libnetfilter_queue.

%prep
%setup -q

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

%files
%defattr(644,root,root,755)
%doc ChangeLog
%attr(755,root,root) %{_libdir}/libnetfilter_queue.so.*.*.*
%attr(755,root,root) %{_libdir}/libnetfilter_queue_libipq.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libnetfilter_queue.so
%attr(755,root,root) %{_libdir}/libnetfilter_queue_libipq.so
%{_libdir}/libnetfilter_queue.la
%{_libdir}/libnetfilter_queue_libipq.la
%{_includedir}/libnetfilter_queue
%{_pkgconfigdir}/libnetfilter_queue.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libnetfilter_queue.a
%{_libdir}/libnetfilter_queue_libipq.a
