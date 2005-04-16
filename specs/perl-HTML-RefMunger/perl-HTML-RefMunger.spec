# $Id$
# Authority: dries
# Upstream: Alligator Descartes <descarte$symbolstone,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name HTML-RefMunger

Summary: Mangle HREF links within HTML files
Name: perl-HTML-RefMunger
Version: 0.01
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/HTML-RefMunger/

Source: http://search.cpan.org/CPAN/authors/id/A/AD/ADESC/HTML-RefMunger-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
HTML::RefMunger is a module that will parse HTML files for HREF and IMG
tags and munge the links within them to suit various file naming conventions.
For example, the module was primarily written to convert large quantities
of JavaDoc-generated documentation into a format that could be mastered onto
CD-ROM for use on the Apple Macintosh. MacOS has an arbitrary filename
limit of 32 characters which made mastering impossible with long filenames.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib} %{buildroot}%{perl_vendorarch}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README
%doc %{_mandir}/man?/*
%{_bindir}/refmunger
%{perl_vendorlib}/HTML/RefMunger.pm

%changelog
* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.01-1
- Initial package.
