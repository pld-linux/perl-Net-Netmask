#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Net
%define	pnam	Netmask
Summary:	Net::Netmask - parse, manipulate and lookup IP network blocks
Summary(pl):	Net::Netmask - analiza, obróbka i wyszukiwanie bloków sieci IP
Name:		perl-Net-Netmask
Version:	1.9009
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	453bda8004c3b8d83e12d9d8e3d703a7
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Net::Netmask parses and understands IPv4 CIDR blocks. It's built with
an object-oriented interface. Nearly all functions are methods that
operate on a Net::Netmask object.

%description -l pl
Modu³ Net::Netmask analizuje i rozumie bloki CIDR IPv4. Ma obiektowo
zorientowany interfejs. Prawie wszystkie funkcje s± metodami
operuj±cymi na obiekcie Net::Netmask.

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
%doc README CHANGELOG
%{perl_vendorlib}/Net/Netmask.pm
%{_mandir}/man3/*
