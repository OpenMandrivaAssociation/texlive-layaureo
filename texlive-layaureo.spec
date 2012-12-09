# revision 19087
# category Package
# catalog-ctan /macros/latex/contrib/layaureo
# catalog-date 2006-12-30 10:59:01 +0100
# catalog-license lppl
# catalog-version undef
Name:		texlive-layaureo
Version:	20061230
Release:	2
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

%description
This package produces a wide page layout for documents that use
A4 paper size. Moreover, LayAureo provides both a simple hook
for leaving an empty space which is required if pages are
bundled by a press binding use option binding=length), and an
option called big which it forces typearea to become maximum.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/layaureo/layaureo.sty
%doc %{_texmfdistdir}/doc/latex/layaureo/README
%doc %{_texmfdistdir}/doc/latex/layaureo/layaureo.pdf
#- source
%doc %{_texmfdistdir}/source/latex/layaureo/layaureo.dtx
%doc %{_texmfdistdir}/source/latex/layaureo/layaureo.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20061230-2
+ Revision: 753206
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20061230-1
+ Revision: 718833
- texlive-layaureo
- texlive-layaureo
- texlive-layaureo
- texlive-layaureo

