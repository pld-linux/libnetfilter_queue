Summary:	netfilter userspace packet queueing library
Summary(pl.UTF-8):	Biblioteka kolejkowania pakietów w przestrzeni użytkownika dla netfiltra
Name:		libnetfilter_queue
Version:	0.0.13
Release:	1
License:	GPL v2
Group:		Libraries
Source0:	http://www.netfilter.org/projects/libnetfilter_queue/files/%{name}-%{version}.tar.bz2
# Source0-md5:	660cbfd3dc8c10bf9b1803cd2b688256
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

%description -l pl.UTF-8
libnetfilter_queue to biblioteka przestrzeni użytkownika
udostępniająca API do pakietów kolejkowanych przez filtr pakietów w
jądrze. Jest częścią systemu zastępującego stary mechanizm
ip_queue/libipq.

%package devel
Summary:	Header files for libnetfilter_queue library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libnetfilter_queue
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libnfnetlink-devel >= 0.0.16

%description devel
Header files for libnetfilter_queue library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libnetfilter_queue.

%package static
Summary:	Static libnetfilter_queue library
Summary(pl.UTF-8):	Statyczna biblioteka libnetfilter_queue
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libnetfilter_queue library.

%description static -l pl.UTF-8
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
