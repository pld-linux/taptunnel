Summary:	tools for creating ethernet-tunnels over the TCP/IP-net
Summary(pl):	narzêdzie do tworzenia ethernetowych tuneli poprzez sieæ TCP/IP
Name:		taptunnel
Version:	0.211
Release:	1
Vendor:		Lennart Poettering <poettering@gmx.net>
Copyright:	GPL
Group:		Networking/Utilities
Group(pl):	Sieciowe/Serwery
Source0:	http://207.236.110.176/~poettering/lennart/projects/taptunnel/%{name}-%{version}-source.tar.gz
Source1:	http://207.236.110.176/~poettering/lennart/projects/taptunnel/index.html
URL:		http://207.236.110.176/~poettering/lennart/projects/taptunnel/
BuildRequires:	libmcrypt
Requires:	libmcrypt
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
taptunnel, a TCP/IP-application, which allows to create
ethernet-tunnels over the Internet or any other TCP/IP-net. It uses the new
ethertap-device of the Linux kernel 2.2 and above.

%description -l pl
taptunnel, to aplikacja TCP/IP pozwalaj±ca na tworzenie
ethernetowych tuneli poprzez Internet lub innych sieci
TCP/IP. taptunnel u¿ywa nowego urz±dzenia dostêpnego
w j±drach 2.2.x - urz±dzenie ethertap.

%prep
%setup -q

%build
for a in *.cc; do
	gcc $RPM_OPT_FLAGS $a -c -I.
done

gcc $RPM_OPT_FLAGS -s *.o -o %{name} -lmcrypt -L/usr/lib

%install
rm -rf $RPM_BUILD_ROOT

install -d			$RPM_BUILD_ROOT%{_sbindir}
install -s	%{name}		$RPM_BUILD_ROOT%{_sbindir}
install 	%{SOURCE1}	.

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.html
%attr(755,root,root) %{_sbindir}/%{name}
