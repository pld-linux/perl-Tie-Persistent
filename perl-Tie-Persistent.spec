#
# Conditional build:
# _without_tests - do not perform "make test"
%include	/usr/lib/rpm/macros.perl
%define	pdir	Tie
%define	pnam	Persistent
Summary:	Tie::Persistent - persistent data structures via tie made easy
Summary(pl):	Tie::Persistent - trwa³e struktury danych oparte na Tie
Name:		perl-Tie-Persistent
Version:	1.00
Release:	3
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	4f21d393e7af0cb6eebad6b3b72a2797
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	perl-Storable >= 0.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Tie::Persistent package makes working with persistent data real
easy by using the tie interface.

It works by storing data contained in a variable into a file (not
unlike a database). The primary advantage is speed, as the whole
datastructure is kept in memory (which is also a limitation), and, of
course, that you can use arbitrary data structures inside the variable
(unlike DB_File).

%description -l pl
Pakiet Tie::Persistent czyni pracê z trwa³ymi danymi naprawdê ³atw±
dziêki u¿yciu interfejsu tie.

Dzia³a on poprzez zapisywanie danych zawartych w zmiennej do pliku
(podobnie jak w bazie danych). G³ówn± zalet± jest szybko¶æ, jako ¿e
ca³a struktura danych jest trzymana w pamiêci (która jest tak¿e
ograniczeniem) i oczywi¶cie to, ¿e mo¿na u¿ywaæ w zmiennej dowolnych
struktur danych (w przeciwieñstwie do DB_File).

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make}

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/%{pdir}/*.pm
%{_mandir}/man3/*
