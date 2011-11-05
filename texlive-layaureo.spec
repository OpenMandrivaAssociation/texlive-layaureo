# revision 19087
# category Package
# catalog-ctan /macros/latex/contrib/layaureo
# catalog-date 2006-12-30 10:59:01 +0100
# catalog-license lppl
# catalog-version undef
Name:		texlive-layaureo
Version:	20061230
Release:	1
Summary:	A package to improve the A4 page layout
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/layaureo
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/layaureo.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/layaureo.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/layaureo.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
This package produces a wide page layout for documents that use
A4 paper size. Moreover, LayAureo provides both a simple hook
for leaving an empty space which is required if pages are
bundled by a press binding use option binding=length), and an
option called big which it forces typearea to become maximum.

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
%{_texmfdistdir}/tex/latex/layaureo/layaureo.sty
%doc %{_texmfdistdir}/doc/latex/layaureo/README
%doc %{_texmfdistdir}/doc/latex/layaureo/layaureo.pdf
#- source
%doc %{_texmfdistdir}/source/latex/layaureo/layaureo.dtx
%doc %{_texmfdistdir}/source/latex/layaureo/layaureo.ins
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
