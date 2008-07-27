#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Tie
%define		pnam	Persistent
Summary:	Tie::Persistent - persistent data structures via tie made easy
Summary(pl.UTF-8):	Tie::Persistent - trwałe struktury danych oparte na Tie
Name:		perl-Tie-Persistent
Version:	1.00
Release:	6
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	4f21d393e7af0cb6eebad6b3b72a2797
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
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

%description -l pl.UTF-8
Pakiet Tie::Persistent czyni pracę z trwałymi danymi naprawdę łatwą
dzięki użyciu interfejsu tie.

Działa on poprzez zapisywanie danych zawartych w zmiennej do pliku
(podobnie jak w bazie danych). Główną zaletą jest szybkość, jako że
cała struktura danych jest trzymana w pamięci (która jest także
ograniczeniem) i oczywiście to, że można używać w zmiennej dowolnych
struktur danych (w przeciwieństwie do DB_File).

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/%{pdir}/*.pm
%{_mandir}/man3/*
