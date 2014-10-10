%define	upstream_name	 Readonly-XS
%define upstream_version 1.05

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:	5

Summary:	Companion module for Readonly.pm, to speed up read-only scalar variables
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Readonly/%{upstream_name}-%{upstream_version}.tar.gz

Buildrequires:	perl-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
The Readonly module (q.v.) is an effective way to create non-modifiable
variables. However, it's relatively slow.

The reason it's slow is that is implements the read-only-ness of variables via
tied objects. This mechanism is inherently slow. Perl simply has to do a lot of
work under the hood to make tied variables work.

This module corrects the speed problem, at least with respect to scalar
variables. When Readonly::XS is installed, Readonly uses it to access the
internals of scalar variables. Instead of creating a scalar variable object and
tying it, Readonly simply flips the SvREADONLY bit in the scalar's FLAGS
structure.

Readonly arrays and hashes are not sped up by this, since the SvREADONLY flag
only works for scalars. Arrays and hashes always use the tie interface.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make CFLAGS="%{optflags}"

%check
%{__make} test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc Changes README
%{perl_vendorarch}/Readonly
%{perl_vendorarch}/auto/Readonly
%{_mandir}/*/*


%changelog
* Wed Jan 25 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 1.50.0-4
+ Revision: 768358
- svn commit -m mass rebuild of perl extension against perl 5.14.2

* Tue Jul 20 2010 Jérôme Quelin <jquelin@mandriva.org> 1.50.0-3mdv2011.0
+ Revision: 556138
- rebuild for perl 5.12
- rebuild for perl 5.12

* Wed Jul 29 2009 Jérôme Quelin <jquelin@mandriva.org> 1.50.0-1mdv2010.0
+ Revision: 404353
- rebuild using %%perl_convert_version

* Wed Feb 25 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.05-1mdv2009.1
+ Revision: 344647
- new version

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 1.04-9mdv2009.0
+ Revision: 258281
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 1.04-8mdv2009.0
+ Revision: 246345
- rebuild

* Thu Feb 28 2008 Jérôme Quelin <jquelin@mandriva.org> 1.04-6mdv2008.1
+ Revision: 176251
- applying patch to build against perl 5.10

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Sat Sep 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.04-3mdv2008.0
+ Revision: 86821
- rebuild


* Thu Aug 31 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.04-2mdv2007.0
- Rebuild

* Sun Apr 23 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.04-1mdk
- first mdk release

