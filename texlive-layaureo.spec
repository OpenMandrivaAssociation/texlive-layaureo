%global tl_name layaureo
%global tl_revision 19087

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.2
Release:	%{tl_revision}.1
Summary:	A package to improve the A4 page layout
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/layaureo
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/layaureo.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/layaureo.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/layaureo.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package produces a wide page layout for documents that use A4 paper
size. Moreover, LayAureo provides both a simple hook for leaving an
empty space which is required if pages are bundled by a press binding
(use option binding=length), and an option called big which it forces
typearea to become maximum.

