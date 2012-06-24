Summary:	readline wrapper
Summary(pl):	Nak�adka na readline
Name:		rlwrap
Version:	0.21
Release:	1
License:	GPL v2
Group:		Applications/System
Source0:	http://utopia.knoware.nl/~hlub/rlwrap/%{name}-%{version}.tar.gz
# Source0-md5:	036993936a13d532a540a6714c97dc2f
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
rlwrap to 'readline wrapper' (nak�adka na readline), czyli ma�e
narz�dzie korzystaj�ce z biblioteki GNU readline do umo�liwienia
edycji wej�cia z klawiatury na standardowe wej�cie dowolnego
polecenia. rlwrap mo�e by� u�yteczny gdy potrzebujemy w�asnych
definicji (i przy okazji listy uzupe�niania s��w) oraz historii
uzupe�niania.

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
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/%{name}
%dir %{_datadir}/rlwrap
%{_datadir}/rlwrap/ftp
%{_mandir}/man?/*
