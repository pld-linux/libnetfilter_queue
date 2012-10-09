Summary:	netfilter userspace packet queueing library
Summary(pl.UTF-8):	Biblioteka kolejkowania pakietów w przestrzeni użytkownika dla netfiltra
Name:		libnetfilter_queue
Version:	1.0.2
Release:	1
License:	GPL v2
Group:		Libraries
Source0:	http://www.netfilter.org/projects/libnetfilter_queue/files/%{name}-%{version}.tar.bz2
# Source0-md5:	df09befac35cb215865b39a36c96a3fa
URL:		http://www.netfilter.org/projects/libnetfilter_queue/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake >= 1.6
BuildRequires:	libmnl-devel >= 1.0.3
BuildRequires:	libnfnetlink-devel >= 0.0.41
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.9.0
Requires:	libmnl >= 1.0.3
Requires:	libnfnetlink >= 0.0.41
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
Requires:	libmnl-devel >= 1.0.3
Requires:	libnfnetlink-devel >= 0.0.41

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
%{__aclocal} -I m4
%{__autoconf}
%{__automake}
%configure \
	--disable-silent-rules \
	--enable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# this shouldn't be installed (and not in this place)
%{__rm} $RPM_BUILD_ROOT%{_includedir}/internal.h

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libnetfilter_queue.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libnetfilter_queue.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libnetfilter_queue.so
%{_libdir}/libnetfilter_queue.la
%{_includedir}/libnetfilter_queue
%{_pkgconfigdir}/libnetfilter_queue.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libnetfilter_queue.a
