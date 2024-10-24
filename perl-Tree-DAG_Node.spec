%define modname	Tree-DAG_Node

Summary:	Class for representing nodes in an N-ary tree
Name:		perl-%{modname}
Version:	1.32
Release:	1
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/pod/Tree::DAG_Node
Source0:	http://www.cpan.org/modules/by-module/Tree/Tree-DAG_Node-%{version}.tgz
BuildArch:	noarch
BuildRequires:	perl(Test::More)
BuildRequires:	perl(File::Slurp::Tiny)
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
%autosetup -p1 -n %{modname}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build

%install
%make_install

%check
make test

%files 
%doc  README
%{perl_vendorlib}/Tree
%{_mandir}/man3/*
