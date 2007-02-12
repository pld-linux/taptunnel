# NOTE: obsolete, for Linux 2.2.x ONLY
Summary:	Tools for creating ethernet-tunnels over the TCP/IP-net
Summary(pl.UTF-8):	Narzędzie do tworzenia ethernetowych tuneli poprzez sieć TCP/IP
Name:		taptunnel
Version:	0.31
Release:	1
Epoch:		1
License:	GPL
Group:		Networking/Utilities
Source0:	http://0pointer.de/lennart/projects/taptunnel/%{name}-%{version}-source.tar.gz
# Source0-md5:	2387595e39056142ba0b4a7286aa983c
Source1:	%{name}.html
URL:		http://0pointer.de/lennart/projects/taptunnel/
BuildRequires:	libmcrypt-devel
Requires:	libmcrypt
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
taptunnel, a TCP/IP-application, which allows to create
ethernet-tunnels over the Internet or any other TCP/IP-net. It uses
the ethertap-device specific to Linux kernel 2.2.x (doesn't work with
2.4.x and newer).

%description -l pl.UTF-8
taptunnel, to aplikacja TCP/IP pozwalająca na tworzenie ethernetowych
tuneli poprzez Internet lub innych sieci TCP/IP. taptunnel używa
urządzenia ethertap specyficznego dla jąder Linuksa 2.2.x (nie działa
z 2.4.x i nowszymi).

%prep
%setup -q

%build
for a in *.cc; do
	%{__cc} %{rpmcflags} $a -c -I.
done

%{__cc} %{rpmcflags} %{rpmldflags} *.o -o %{name} -lmcrypt -L%{_libdir}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sbindir}

install %{name} $RPM_BUILD_ROOT%{_sbindir}
install %{SOURCE1} .

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.html
%attr(755,root,root) %{_sbindir}/%{name}
