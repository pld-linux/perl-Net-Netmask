%include	/usr/lib/rpm/macros.perl
Summary:	Net-Netmask perl module
Summary(pl):	Modu³ perla Net-Netmask
Name:		perl-Net-Netmask
Version:	1.8
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/Net/Net-Netmask-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	/tmp/%{name}-%{version}-root

%description
Net-Netmask perl module.

%description -l pl
Modu³ perla Net-Netmask.

%prep
%setup -q -n Net-Netmask-%{version}

%build
perl Makefile.PL
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/Net/Netmask
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        README CHANGELOG

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {README,CHANGELOG}.gz

%{perl_sitelib}/Net/Netmask.pm
%{perl_sitearch}/auto/Net/Netmask

%{_mandir}/man3/*
