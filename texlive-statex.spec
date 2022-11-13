Name:		texlive-statex
Version:	20306
Release:	1
Summary:	Statistics style
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/statex
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/statex.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/statex.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A package defining many macros for items of significance in
statistical presentations. An updated, but incompatible,
version of the package is available: statex2.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/statex/statex.sty
%doc %{_texmfdistdir}/doc/latex/statex/statex-example.pdf
%doc %{_texmfdistdir}/doc/latex/statex/statex-example.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
