Summary:	readline wrapper
Summary(pl.UTF-8):	Nakładka na readline
Name:		rlwrap
Version:	0.46.1
Release:	1
License:	GPL v2
Group:		Applications/System
Source0:	https://github.com/hanslub42/rlwrap/releases/download/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	8f11986a2969ca00ac4240185cbfc7c3
URL:		https://github.com/hanslub42/rlwrap
BuildRequires:	autoconf >= 2.69
BuildRequires:	automake
BuildRequires:	readline-devel >= 4.2
BuildRequires:	sed >= 4.0
Requires:	readline >= 4.2
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

%{__sed} -i -e '1s,#! */usr/bin/env perl,#!%{__perl},' \
	test/testclient \
	filters/*

grep -l -r '#!.*env python3' filters | xargs %{__sed} -i -e '1 s,#!.*env python3.*,#!%{__python3},'

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_datadir}/rlwrap/filters/{README,RlwrapFilter.3pm}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS BUGS ChangeLog NEWS README.md
%attr(755,root,root) %{_bindir}/%{name}
%dir %{_datadir}/rlwrap
%dir %{_datadir}/rlwrap/completions
%{_datadir}/rlwrap/completions/coqtop
%{_datadir}/rlwrap/completions/testclient
%dir %{_datadir}/rlwrap/filters
%{_datadir}/rlwrap/filters/RlwrapFilter.pm
%attr(755,root,root) %{_datadir}/rlwrap/filters/censor_passwords
%attr(755,root,root) %{_datadir}/rlwrap/filters/censor_passwords.py
%attr(755,root,root) %{_datadir}/rlwrap/filters/count_in_prompt
%attr(755,root,root) %{_datadir}/rlwrap/filters/count_in_prompt.py
%attr(755,root,root) %{_datadir}/rlwrap/filters/debug_null
%attr(755,root,root) %{_datadir}/rlwrap/filters/dissect_prompt
%attr(755,root,root) %{_datadir}/rlwrap/filters/edit_history
%attr(755,root,root) %{_datadir}/rlwrap/filters/ftp_filter
%attr(755,root,root) %{_datadir}/rlwrap/filters/ftp_filter.py
%attr(755,root,root) %{_datadir}/rlwrap/filters/handle_hotkeys
%attr(755,root,root) %{_datadir}/rlwrap/filters/handle_hotkeys.py
%attr(755,root,root) %{_datadir}/rlwrap/filters/handle_sigwinch
%attr(755,root,root) %{_datadir}/rlwrap/filters/history_format
%attr(755,root,root) %{_datadir}/rlwrap/filters/listing
%attr(755,root,root) %{_datadir}/rlwrap/filters/logger
%attr(755,root,root) %{_datadir}/rlwrap/filters/logger.py
%attr(755,root,root) %{_datadir}/rlwrap/filters/makefilter
%attr(755,root,root) %{_datadir}/rlwrap/filters/null
%attr(755,root,root) %{_datadir}/rlwrap/filters/null.py
%attr(755,root,root) %{_datadir}/rlwrap/filters/outfilter
%attr(755,root,root) %{_datadir}/rlwrap/filters/paint_prompt
%attr(755,root,root) %{_datadir}/rlwrap/filters/paint_prompt.py
%attr(755,root,root) %{_datadir}/rlwrap/filters/pipeline
%attr(755,root,root) %{_datadir}/rlwrap/filters/pipeto
%attr(755,root,root) %{_datadir}/rlwrap/filters/pipeto.py
%attr(755,root,root) %{_datadir}/rlwrap/filters/rlwrapfilter.py
%attr(755,root,root) %{_datadir}/rlwrap/filters/scrub_prompt
%attr(755,root,root) %{_datadir}/rlwrap/filters/simple_macro
%attr(755,root,root) %{_datadir}/rlwrap/filters/template
%attr(755,root,root) %{_datadir}/rlwrap/filters/unbackspace
%{_mandir}/man1/rlwrap.1*
%{_mandir}/man3/RlwrapFilter.3pm*
