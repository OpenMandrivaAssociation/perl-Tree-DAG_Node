%define modname	Tree-DAG_Node
%define modver 1.31

Summary:	Class for representing nodes in a tre
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	1
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}
Source0:	http://www.cpan.org/modules/by-module/Tree/Tree-DAG_Node-%{modver}.tgz
BuildArch:	noarch
BuildRequires:	perl-devel

%description
This class encapsulates/makes/manipulates objects that represent nodes in a
tree structure. The tree structure is not an object itself, but is emergent
from the linkages you create between nodes. This class provides the methods for
making linkages that can be used to build up a tree, while preventing you from
ever making any kinds of linkages which are not allowed in a tree (such as
having a node be its own mother or ancestor, or having a node have two
mothers).

%prep
%setup -qn %{modname}-%{modver}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%install
%makeinstall_std

%check
make test

%files 
%doc  README
%{perl_vendorlib}/Tree
%{_mandir}/man3/*


