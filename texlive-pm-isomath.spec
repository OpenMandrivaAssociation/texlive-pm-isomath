%global tl_name pm-isomath
%global tl_revision 76924

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.2.00
Release:	%{tl_revision}.1
Summary:	Poor man ISO math for pdfLaTeX users
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/pm-isomath
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pm-isomath.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pm-isomath.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pm-isomath.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This small package realizes a poor man approximation of the ISO
regulations for physical sciences and technology. Contrary to other more
elegant solutions, it does not load any math alphabet, since pdfLaTeX
can use only a maximum of such alphabets. The necessary user macros are
defined for typesetting common math symbols that require special ISO
treatment.

