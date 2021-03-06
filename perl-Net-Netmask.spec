#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%define		pdir	Net
%define		pnam	Netmask
Summary:	Net::Netmask - parse, manipulate and lookup IP network blocks
Summary(pl.UTF-8):	Net::Netmask - analiza, obróbka i wyszukiwanie bloków sieci IP
Name:		perl-Net-Netmask
Version:	1.9016
Release:	1
# "License hereby granted for anyone to use, modify or redistribute this module at their own risk."
License:	Free
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Net/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	174606b568f8545b8968aecf50ba7a37
URL:		http://search.cpan.org/dist/Net-Netmask/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Net::Netmask parses and understands IPv4 CIDR blocks. It's built with
an object-oriented interface. Nearly all functions are methods that
operate on a Net::Netmask object.

%description -l pl.UTF-8
Moduł Net::Netmask analizuje i rozumie bloki CIDR IPv4. Ma obiektowo
zorientowany interfejs. Prawie wszystkie funkcje są metodami
operującymi na obiekcie Net::Netmask.

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
