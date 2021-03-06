# $Id$
# Authority: dag
# Upstream: Torsten Schoenfeld <tsch@cpan.org>

%define _without_directfb 1

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Cairo

Summary: Perl interface to the cairo library
Name: perl-Cairo
Version: 1.061
Release: 2%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Cairo/

Source: http://www.cpan.org/authors/id/T/TS/TSCH/Cairo-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: cairo-devel
BuildRequires: perl >= 2:5.8.0
BuildRequires: perl(ExtUtils::Depends) >= 0.2
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(ExtUtils::PkgConfig) >= 1
BuildRequires: perl(Glib) >= 1.0.0
BuildRequires: perl(Test::Number::Delta) >= 1
BuildRequires: libpng-devel
%{!?_without_directfb:BuildRequires: directfb-devel}
Requires: perl >= 2:5.8.0
Requires: perl(ExtUtils::Depends) >= 0.2
Requires: perl(ExtUtils::PkgConfig) >= 1
Requires: cairo
Requires: libpng
%{!?_without_directfb:Requires: directfb}

%description
Perl interface to the cairo library.

%prep
%setup -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

### Clean up docs
find examples/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog LICENSE MANIFEST MANIFEST.SKIP META.yml NEWS README TODO examples/
%doc %{_mandir}/man3/Cairo.3pm*
#%doc %{_mandir}/man3/*.3pm*
%{perl_vendorarch}/auto/Cairo/
%{perl_vendorarch}/Cairo/
%{perl_vendorarch}/Cairo.pm

%changelog
* Sat Dec 04 2010 Dag Wieers <dag@wieers.com> - 1.061-2
- Disable directfb support to ease things (Red Hat does not include it either).

* Tue Jan  5 2010 Christoph Maser <cmr@financial.com> - 1.061-1
- Updated to version 1.061.

* Wed Sep 24 2008 Dag Wieers <dag@wieers.com> - 1.060-3
- Rebuild against directfb-1.2.4.

* Sat Jul 05 2008 Dag Wieers <dag@wieers.com> - 1.060-2
- Rebuild against directfb-1.0.1.

* Sat May 03 2008 Dag Wieers <dag@wieers.com> - 1.060-1
- Updated to release 1.060.

* Wed Jan 23 2008 Dag Wieers <dag@wieers.com> - 1.045-1
- Updated to release 1.045.

* Sat Nov 24 2007 Dag Wieers <dag@wieers.com> - 1.044-1
- Updated to release 1.044.

* Tue Nov 06 2007 Dag Wieers <dag@wieers.com> - 1.043-1
- Updated to release 1.043.

* Wed Aug 08 2007 Dag Wieers <dag@wieers.com> - 1.041-1
- Updated to release 1.041.

* Thu Mar 29 2007 Dag Wieers <dag@wieers.com> - 1.023-1
- Initial package. (using DAR)
