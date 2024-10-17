Name:		texlive-pm-isomath
Version:	60368
Release:	2
Summary:	Poor man ISO math for pdfLaTeX users
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/pm-isomath
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pm-isomath.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pm-isomath.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pm-isomath.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This small package realizes a poor man approximation of the ISO
regulations for physical sciences and technology. Contrary to
other more elegant solutions, it does not load any math
alphabet, since pdfLaTeX can use only a maximum of such
alphabets. The necessary user macros are defined for typsetting
common math symbols that require special ISO treatment.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/pm-isomath
%{_texmfdistdir}/tex/latex/pm-isomath
%doc %{_texmfdistdir}/doc/latex/pm-isomath

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
