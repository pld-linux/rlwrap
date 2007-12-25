Summary:	readline wrapper
Summary(pl.UTF-8):	Nakładka na readline
Name:		rlwrap
Version:	0.29
Release:	1
License:	GPL v2
Group:		Applications/System
Source0:	http://utopia.knoware.nl/~hlub/rlwrap/%{name}-%{version}.tar.gz
# Source0-md5:	03787a8dfdd8c0ad9c8f459cde11a2c1
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

%description -l pl.UTF-8
rlwrap to 'readline wrapper' (nakładka na readline), czyli małe
narzędzie korzystające z biblioteki GNU readline do umożliwienia
edycji wejścia z klawiatury na standardowe wejście dowolnego
polecenia. rlwrap może być użyteczny gdy potrzebujemy własnych
definicji (i przy okazji listy uzupełniania słów) oraz historii
uzupełniania.

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
%doc AUTHORS BUGS NEWS README
%attr(755,root,root) %{_bindir}/%{name}
%dir %{_datadir}/rlwrap
%{_datadir}/rlwrap/ftp
%{_mandir}/man?/*
