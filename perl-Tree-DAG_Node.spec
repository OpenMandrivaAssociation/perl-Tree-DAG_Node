%define upstream_name	 Tree-DAG_Node
%define upstream_version 1.06

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	7

Summary:	Class for representing nodes in a tre
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Tree/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildArch:	noarch

%description
This class encapsulates/makes/manipulates objects that represent nodes in a
tree structure. The tree structure is not an object itself, but is emergent
from the linkages you create between nodes. This class provides the methods for
making linkages that can be used to build up a tree, while preventing you from
ever making any kinds of linkages which are not allowed in a tree (such as
having a node be its own mother or ancestor, or having a node have two
mothers).

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%install
%makeinstall_std

%check
make test

%files 
%doc ChangeLog README
%{perl_vendorlib}/Tree
%{_mandir}/*/*


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 1.60.0-4mdv2012.0
+ Revision: 765794
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 1.60.0-3
+ Revision: 764299
- rebuilt for perl-5.14.x

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 1.60.0-2
+ Revision: 667404
- mass rebuild

* Sat Aug 01 2009 Jérôme Quelin <jquelin@mandriva.org> 1.60.0-1mdv2011.0
+ Revision: 405767
- rebuild using %%perl_convert_version

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 1.06-2mdv2009.0
+ Revision: 224582
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Mon Dec 10 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.06-1mdv2008.1
+ Revision: 116897
- new version

* Sat May 05 2007 Olivier Thauvin <nanardon@mandriva.org> 1.05-4mdv2008.0
+ Revision: 23299
- rebuild


* Mon Apr 03 2006 Buchan Milne <bgmilne@mandriva.org> 1.05-3mdk
- Rebuild
- use mkrel

* Tue Jun 07 2005 Guillaume Rousse <guillomovitch@mandriva.org> 1.05-2mdk 
- don't ship useless empty directories
- make test in %%check

* Mon Apr 25 2005 Guillaume Rousse <guillomovitch@mandriva.org> 1.05-1mdk
- new release
- spec cleanup
- better url

* Mon Dec 20 2004 Guillaume Rousse <guillomovitch@mandrake.org> 1.04-3mdk
- fix buildrequires in a backward compatible way

* Fri Jul 23 2004 Guillaume Rousse <guillomovitch@mandrake.org> 1.04-2mdk 
- rpmbuildupdate aware

* Mon Jan 05 2004 Guillaume Rousse <guillomovitch@mandrake.org> 1.04-1mdk
- first mdk release

