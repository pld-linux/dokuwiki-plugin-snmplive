Summary:	DokuWiki SNMPlive Plugin
Summary(pl.UTF-8):	Wtyczka SNMPlive dla DokuWiki
Name:		dokuwiki-plugin-snmplive
Version:	0.1
Release:	0.1
License:	GPL v2
Group:		Applications/WWW
Source0:	http://glen.alkohol.ee/pld/snmplive.tar.gz
# Source0-md5:	8fb23b7858d2cba87021e5a56e39297f
URL:		http://wiki.splitbrain.org/plugin:snmplive
Requires:	dokuwiki
Requires:	php(pcre)
Requires:	php(snmp)
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_dokudir	/usr/share/dokuwiki
%define		_plugin		snmplive
%define		_plugindir	%{_dokudir}/lib/plugins/%{_plugin}

%description
It gets the actual SNMP values out of any by the server reachable
device (e.g. servers, printers, temp. sensors).

%description -l pl.UTF-8
Ta wtyczka pobiera odpowiednie wartości SNMP z dowolnych urządzeń
osiągalnych z serwera (np. serwerów, drukarek, czujników temperatury).

%prep
%setup -q -n %{_plugin}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_plugindir}
