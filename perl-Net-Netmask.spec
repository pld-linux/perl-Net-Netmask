%include	/usr/lib/rpm/macros.perl
%define	pdir	Net
%define	pnam	Netmask
Summary:	Net::Netmask perl module
Summary(pl):	Modu³ perla Net::Netmask
Name:		perl-Net-Netmask
Version:	1.9002
Release:	5
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl-devel >= 5.6.1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Net::Netmask perl module.

%description -l pl
Modu³ perla Net::Netmask.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README CHANGELOG t/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz t/*.gz
%{perl_sitelib}/Net/Netmask.pm
%{_mandir}/man3/*
