# revision 33756
# category Package
# catalog-ctan /support/latexmk
# catalog-date 2013-12-03 18:34:20 +0100
# catalog-license gpl
# catalog-version 4.39
Name:		texlive-latexmk
Version:	4.39
Release:	10
Summary:	Fully automated LaTeX document generation
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/support/latexmk
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/latexmk.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/latexmk.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/latexmk.source.tar.xz
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
%{_texmfdistdir}/scripts/latexmk/latexmk.pl
%doc %{_mandir}/man1/latexmk.1*
%doc %{_texmfdistdir}/doc/man/man1/latexmk.man1.pdf
%doc %{_texmfdistdir}/doc/support/latexmk/CHANGES
%doc %{_texmfdistdir}/doc/support/latexmk/COPYING
%doc %{_texmfdistdir}/doc/support/latexmk/INSTALL
%doc %{_texmfdistdir}/doc/support/latexmk/README
%doc %{_texmfdistdir}/doc/support/latexmk/example_rcfiles/README
%doc %{_texmfdistdir}/doc/support/latexmk/example_rcfiles/asymptote_latexmkrc
%doc %{_texmfdistdir}/doc/support/latexmk/example_rcfiles/clean_pattern_latexmkrc
%doc %{_texmfdistdir}/doc/support/latexmk/example_rcfiles/exceltex_latexmkrc
%doc %{_texmfdistdir}/doc/support/latexmk/example_rcfiles/glossary_latexmkrc
%doc %{_texmfdistdir}/doc/support/latexmk/example_rcfiles/lualatex_latexmkrc
%doc %{_texmfdistdir}/doc/support/latexmk/example_rcfiles/mpost_latexmkrc
%doc %{_texmfdistdir}/doc/support/latexmk/example_rcfiles/pdflatexmkrc
%doc %{_texmfdistdir}/doc/support/latexmk/example_rcfiles/pythontex-latexmkrc
%doc %{_texmfdistdir}/doc/support/latexmk/example_rcfiles/sagetex_latexmkrc
%doc %{_texmfdistdir}/doc/support/latexmk/example_rcfiles/sweave_latexmkrc
%doc %{_texmfdistdir}/doc/support/latexmk/example_rcfiles/tex4ht-latexmkrc
%doc %{_texmfdistdir}/doc/support/latexmk/example_rcfiles/xelatex_latexmkrc
%doc %{_texmfdistdir}/doc/support/latexmk/extra-scripts/README1
%doc %{_texmfdistdir}/doc/support/latexmk/extra-scripts/dvipdfm_call
%doc %{_texmfdistdir}/doc/support/latexmk/extra-scripts/dvipdfm_call.bat
%doc %{_texmfdistdir}/doc/support/latexmk/extra-scripts/dvipdfmx_call
%doc %{_texmfdistdir}/doc/support/latexmk/extra-scripts/dvipdfmx_call.bat
%doc %{_texmfdistdir}/doc/support/latexmk/extra-scripts/htlatexonly
%doc %{_texmfdistdir}/doc/support/latexmk/extra-scripts/kickxdvi
%doc %{_texmfdistdir}/doc/support/latexmk/extra-scripts/l1
%doc %{_texmfdistdir}/doc/support/latexmk/extra-scripts/l2
%doc %{_texmfdistdir}/doc/support/latexmk/extra-scripts/myhtlatex2
%doc %{_texmfdistdir}/doc/support/latexmk/extra-scripts/pst2pdf_for_latexmk
%doc %{_texmfdistdir}/doc/support/latexmk/extra-scripts/pst2pdf_for_latexmk_README.txt
%doc %{_texmfdistdir}/doc/support/latexmk/extra-scripts/startacroread
%doc %{_texmfdistdir}/doc/support/latexmk/latexmk.pdf
%doc %{_texmfdistdir}/doc/support/latexmk/latexmk.txt
#- source
%doc %{_texmfdistdir}/source/support/latexmk/latexmk.bat

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

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
