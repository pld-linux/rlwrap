Summary:	readline wrapper
Summary(pl):	Nak³adka na readline
Name:		rlwrap
Version:	0.18
Release:	1
License:	GPL
Group:		Applications/System
Source0:	http://utopia.knoware.nl/~hlub/rlwrap/%{name}-%{version}.tar.gz
# Source0-md5:	0a1b449aab79376c659684196763de52
URL:		http://utopia.knoware.nl/~hlub/rlwrap/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	readline-devel >= 4.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
rlwrap is a 'readline wrapper', i.e. a small utility that uses the GNU
readline library to allow the editing of keyboard input to any
command's stdin. rlwrap should be especially useful when you need
user-defined (by way of completion word lists) and history completion.

%description -l pl
rlwrap to 'readline wrapper' (nak³adka na readline), czyli ma³e
narzêdzie korzystaj±ce z biblioteki GNU readline do umo¿liwienia
edycji wej¶cia z klawiatury na standardowe wej¶cie dowolnego
polecenia. rlwrap mo¿e byæ u¿yteczny gdy potrzebujemy w³asnych
definicji (i przy okazji listy uzupe³niania s³ów) oraz historii
uzupe³niania.

%prep
%setup -q

%build
rm -f missing
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

%files
%defattr(644,root,root,755)
%doc README NEWS ChangeLog
%attr(755,root,root) %{_bindir}/%{name}
%dir %{_datadir}/rlwrap
%{_datadir}/rlwrap/ftp
%{_mandir}/man?/*
