%define	upstream_name	 Readonly-XS
%define upstream_version 1.05

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

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
