Summary:	tools for creating ethernet-tunnels over the TCP/IP-net
Summary(pl):	narz�dzie do tworzenia ethernetowych tuneli poprzez sie� TCP/IP
Name:		taptunnel
Version:	0.31
Release:	1
Vendor:		Lennart Poettering <poettering@gmx.net>
License:	GPL
Group:		Networking/Utilities
Source0:	http://www.stud.uni-hamburg.de/users/lennart/projects/taptunnel/%{name}-%{version}-source.tar.gz
# Source0-md5:	2387595e39056142ba0b4a7286aa983c
# based on http://www.stud.uni-hamburg.de/users/lennart/projects/taptunnel/index.html
Source1:	%{name}.html
URL:		http://www.stud.uni-hamburg.de/users/lennart/projects/taptunnel/
BuildRequires:	libmcrypt
Requires:	libmcrypt
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
taptunnel, a TCP/IP-application, which allows to create
ethernet-tunnels over the Internet or any other TCP/IP-net. It uses
the new ethertap-device of the Linux kernel 2.2 and above.

%description -l pl
taptunnel, to aplikacja TCP/IP pozwalaj�ca na tworzenie ethernetowych
tuneli poprzez Internet lub innych sieci TCP/IP. taptunnel u�ywa
nowego urz�dzenia dost�pnego w j�drach 2.2.x - urz�dzenie ethertap.

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
