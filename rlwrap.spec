Summary:	readline wrapper
Summary(pl):	Nak³adka na readline
Name:		rlwrap
Version:	0.16
Release:	1
URL:		http://utopia.knoware.nl/~hlub/rlwrap/
Source0:	http://utopia.knoware.nl/~hlub/rlwrap/%{name}-%{version}.tar.gz
# Source0-md5:	1b303883d78f279a36bb35e8094e1490
License:	GPL
Group:		Applications/System
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
rlwrap jest 'readline wrapper'(nak³adka na readline), to znaczy ma³ym
narzêdziem korzystaj±cym z GNU readline do umo¿liwienia edycji wej¶cia
z klawiatury na ka¿de wej¶cie poleceñ. rlwrap mo¿e byæ u¿yteczny gdy
potrzebujesz w³asnych definicji (i przy okazji listy uzupe³niania
s³ów) oraz historii uzupe³niania.

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
	DESTDIR=${RPM_BUILD_ROOT}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README NEWS ChangeLog
%dir %{_datadir}/rlwrap
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/rlwrap/ftp
%{_mandir}/man?/*
