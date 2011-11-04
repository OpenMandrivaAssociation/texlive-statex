# revision 20306
# category Package
# catalog-ctan /macros/latex/contrib/statex
# catalog-date 2010-11-03 11:47:38 +0100
# catalog-license lppl
# catalog-version 1.6
Name:		texlive-statex
Version:	1.6
Release:	1
Summary:	Statistics style
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/statex
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/statex.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/statex.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
A package defining many macros for items of significance in
statistical presentations. An updated, but incompatible,
version of the package is available: statex2.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/statex/statex.sty
%doc %{_texmfdistdir}/doc/latex/statex/statex-example.pdf
%doc %{_texmfdistdir}/doc/latex/statex/statex-example.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
