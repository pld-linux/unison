Summary:	Program for bidirectional synchronization
Summary(pl):	Program do synchronizacji dwukierunkowej
Name:		unison
Version:	2.9.1
Release:	2
License:	GPL
Group:		Daemons
Source0:	http://www.cis.upenn.edu/~bcpierce/unison/download/stable/%{name}-%{version}/src.tar.gz
# Source0-md5:	d8084fa87c13671de21ec1b701a4606c
Source1:	%{name}.init
BuildRequires:	ocaml
URL:		http://www.cis.upenn.edu/~bcpierce/unison/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/unisond

%description
Unison is a file-synchronization tool for Unix and Windows. It allows
two replicas of a collection of files and directories to be stored on
different hosts (or different disks on the same host), modified
separately, and then brought up to date by propagating the changes in
each replica to the other.

%description -l pl
Unison to narzêdzie do synchronizacji plików dla uniksów i Windows.
Pozwala na przechowywanie dwóch kopii zbioru plików i katalogów na
ró¿nych maszynach (lub ró¿nych dyskach tej samej maszyny),
oddzielne modyfikowanie ich, a nastêpnie uaktualnianie poprzez
propagowanie zmian z ka¿dej z kopii do drugiej.

%package init
Summary: Init script for system-wide unison service.
Group:	Daemons

%description init
Init script for system-wide unison service. Don't run this unless you know the
security risks involved.

%prep
%setup -q

%build
%{__make} \
	UISTYLE=text

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install unison $RPM_BUILD_ROOT%{_bindir}
#install %{SOURCE1} $RPM_BUILD_ROOT/etc/rc.d/init.d/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README BUGS.txt CONTRIB DEPENDENCIES.ps NEWS ROADMAP.txt TODO.txt
%attr(755,root,root) %{_bindir}/*

%files init
#%attr(744,root,root) /etc/rc.d/init.d/%{name}
