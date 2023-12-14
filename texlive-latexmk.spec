Name:		texlive-latexmk
Version:	68950
Release:	1
Summary:	Fully automated LaTeX document generation
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/support/latexmk
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/latexmk.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/latexmk.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Provides:	texlive-latexmk.bin = %{EVRD}

%description
Latexmk completely automates the process of generating a LaTeX
document. Given the source files for a document, latexmk issues
the appropriate sequence of commands to generate a .dvi, .ps,
.pdf or hardcopy version of the document. An important feature
is the "preview continuous mode", where the script watches all
of the source files (primary file and included TeX and graphics
files), and reruns LaTeX, etc., whenever a source file has
changed. Thus a previewer can offer a display of the document's
latest state.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_bindir}/latexmk
%{_texmfdistdir}/scripts/latexmk
%doc %{_mandir}/man1/*.1*
%doc %{_texmfdistdir}/doc/man/man1/*
%doc %{_texmfdistdir}/doc/support/latexmk

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_bindir}
pushd %{buildroot}%{_bindir}
ln -sf %{_texmfdistdir}/scripts/latexmk/latexmk.pl latexmk
popd
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf-dist %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_mandir}/man1
mv %{buildroot}%{_texmfdistdir}/doc/man/man1/*.1 %{buildroot}%{_mandir}/man1
