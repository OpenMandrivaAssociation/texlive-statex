# revision 20306
# category Package
# catalog-ctan /macros/latex/contrib/statex
# catalog-date 2010-11-03 11:47:38 +0100
# catalog-license lppl
# catalog-version 1.6
Name:		texlive-statex
Version:	1.6
Release:	10
Summary:	Statistics style
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/statex
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/statex.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/statex.doc.tar.xz
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.6-2
+ Revision: 756191
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.6-1
+ Revision: 719580
- texlive-statex
- texlive-statex
- texlive-statex
- texlive-statex

