Name:		texlive-thubeamer
Version:	61071
Release:	2
Summary:	A beamer theme for Tsinghua University
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/thubeamer
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/thubeamer.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/thubeamer.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/thubeamer.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides a beamer theme designed for Tsinghua
University.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/thubeamer
%{_texmfdistdir}/tex/latex/thubeamer
%{_texmfdistdir}/bibtex/bst/thubeamer
%doc %{_texmfdistdir}/doc/latex/thubeamer

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
