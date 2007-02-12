Summary:	Program for bidirectional synchronization
Summary(pl.UTF-8):	Program do synchronizacji dwukierunkowej
Name:		unison
Version:	2.13.16
Release:	1
License:	GPL
Group:		Daemons
Source0:	http://www.cis.upenn.edu/~bcpierce/unison/download/releases/stable/%{name}-%{version}.tar.gz
# Source0-md5:	a79bf5f4ebf2a1eaf15b1ac97f827374
Source1:	%{name}.init
URL:		http://www.cis.upenn.edu/~bcpierce/unison/
BuildRequires:	ocaml
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Unison is a file-synchronization tool for Unix and Windows. It allows
two replicas of a collection of files and directories to be stored on
different hosts (or different disks on the same host), modified
separately, and then brought up to date by propagating the changes in
each replica to the other.

%description -l pl.UTF-8
Unison to narzędzie do synchronizacji plików dla uniksów i Windows.
Pozwala na przechowywanie dwóch kopii zbioru plików i katalogów na
różnych maszynach (lub różnych dyskach tej samej maszyny),
oddzielne modyfikowanie ich, a następnie uaktualnianie poprzez
propagowanie zmian z każdej z kopii do drugiej.

%package init
Summary:	Init script for system-wide unison service
Summary(pl.UTF-8):	Skrypt init dla ogólnosystemowej usługi unison
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description init
Init script for system-wide unison service. Don't run this unless you
know the security risks involved.

%description init -l pl.UTF-8
Skrypt init dla ogólnosystemowej usługi unison. Nie należy go
uruchamiać nie zdając sobie sprawy ze związanych z tym zagrożeń
bezpieczeństwa.

%prep
%setup -q

%build
%{__make} \
	UISTYLE=text

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},/etc/rc.d/init.d}

install unison $RPM_BUILD_ROOT%{_bindir}
install %{SOURCE1} $RPM_BUILD_ROOT/etc/rc.d/init.d/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README BUGS.txt CONTRIB NEWS ROADMAP.txt TODO.txt
%attr(755,root,root) %{_bindir}/*

%files init
%defattr(644,root,root,755)
%attr(754,root,root) /etc/rc.d/init.d/%{name}
