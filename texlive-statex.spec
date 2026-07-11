%global tl_name statex
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.6
Release:	%{tl_revision}.1
Summary:	Statistics style
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/statex
License:	lppl1.2
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/statex.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/statex.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
A package defining many macros for items of significance in statistical
presentations. An updated, but incompatible, version of the package is
available: statex2.

