Name: perl-Pod-Plainer
Version: 1.04
Release: 7%{?dist}
Summary: Perl extension for converting Pod to old-style Pod

License: GPL+ or Artistic
URL: http://search.cpan.org/dist/Pod-Plainer/

Source0: http://search.cpan.org/CPAN/authors/id/R/RM/RMBARKER/Pod-Plainer-%{version}.tar.gz

BuildArch: noarch
BuildRequires: coreutils
BuildRequires: findutils
BuildRequires: make
BuildRequires: perl-interpreter
BuildRequires: perl-generators
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(strict)
# Run-time:
BuildRequires: perl(Pod::Parser)
BuildRequires: perl(warnings)
# Tests:
BuildRequires: perl(Test::More)
# Optional tests:
BuildRequires: perl(Test::Pod) >= 1.00
BuildRequires: perl(Test::Pod::Coverage) >= 1.00
Requires: perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
Pod::Plainer uses Pod::Parser which takes Pod with the (new) 'C<< .. >>'
constructs and returns the old(er) style with just 'C<>'; '<' and '>' are
replaced by 'E<lt>' and 'E<gt>'.
This can be used to pre-process Pod before using tools which do not
recognize the new style Pods.

%prep
%setup -q -n Pod-Plainer-%{version}

%build
# Remove OPTIMIZE=... from noarch packages (unneeded)
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
#rm -rf $RPM_BUILD_ROOT
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
# Remove the next line from noarch packages (unneeded)
find $RPM_BUILD_ROOT -type f -name '*.bs' -a -size 0 -exec rm -f {} ';'
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null ';'
ls -lZ $RPM_BUILD_ROOT/*
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc README Changes
# For noarch packages: vendorlib
%{perl_vendorlib}/Pod/Plainer.pm
%{_mandir}/man3/Pod::Plainer.3pm*

%changelog
* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.04-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.04-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.04-5
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.04-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.04-3
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.04-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Petr Pisar <ppisar@redhat.com> - 1.04-1
- 1.04 bump

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.03-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 05 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.03-9
- Perl 5.22 rebuild

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.03-8
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.03-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.03-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jul 20 2013 Petr Pisar <ppisar@redhat.com> - 1.03-5
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.03-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.03-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jun 12 2012 Petr Pisar <ppisar@redhat.com> - 1.03-2
- Perl 5.16 rebuild

* Mon Mar 26 2012 xning <xning AT redhat DOT com> - 1.03-1
- modified as Petr Šabata's advice
* Fri Mar 02 2012 xning <xning AT redhat DOT com> - 1.03-1
- create for support LSB 4.1
