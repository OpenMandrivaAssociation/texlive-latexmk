# revision 24722
# category Package
# catalog-ctan /support/latexmk
# catalog-date 2011-12-01 23:10:15 +0100
# catalog-license gpl
# catalog-version 4.28c
Name:		texlive-latexmk
Version:	4.28c
Release:	1
Summary:	Fully automated LaTeX document generation routine
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/support/latexmk
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/latexmk.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/latexmk.doc.tar.xz
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
changed. Thus a previewer can have an updated display whenever
the source files change.

%pre
    %{_sbindir}/texlive.post

%post
    %{_sbindir}/texlive.post

%preun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_bindir}/latexmk
%{_texmfdistdir}/scripts/latexmk/latexmk.pl
%doc %{_texmfdistdir}/doc/support/latexmk/CHANGES
%doc %{_texmfdistdir}/doc/support/latexmk/COPYING
%doc %{_texmfdistdir}/doc/support/latexmk/INSTALL
%doc %{_texmfdistdir}/doc/support/latexmk/README
%doc %{_texmfdistdir}/doc/support/latexmk/example_rcfiles/README
%doc %{_texmfdistdir}/doc/support/latexmk/example_rcfiles/asymptote_latexmkrc
%doc %{_texmfdistdir}/doc/support/latexmk/example_rcfiles/glossary_latexmkrc
%doc %{_texmfdistdir}/doc/support/latexmk/example_rcfiles/pdflatexmkrc
%doc %{_texmfdistdir}/doc/support/latexmk/example_rcfiles/sagetex_latexmkrc
%doc %{_texmfdistdir}/doc/support/latexmk/extra-scripts/README1
%doc %{_texmfdistdir}/doc/support/latexmk/extra-scripts/dvipdfm_call
%doc %{_texmfdistdir}/doc/support/latexmk/extra-scripts/dvipdfm_call.bat
%doc %{_texmfdistdir}/doc/support/latexmk/extra-scripts/dvipdfmx_call
%doc %{_texmfdistdir}/doc/support/latexmk/extra-scripts/dvipdfmx_call.bat
%doc %{_texmfdistdir}/doc/support/latexmk/extra-scripts/kickxdvi
%doc %{_texmfdistdir}/doc/support/latexmk/extra-scripts/l1
%doc %{_texmfdistdir}/doc/support/latexmk/extra-scripts/l2
%doc %{_texmfdistdir}/doc/support/latexmk/extra-scripts/pst2pdf_for_latexmk
%doc %{_texmfdistdir}/doc/support/latexmk/extra-scripts/pst2pdf_for_latexmk_README.txt
%doc %{_texmfdistdir}/doc/support/latexmk/extra-scripts/startacroread
%doc %{_texmfdistdir}/doc/support/latexmk/latexmk.bat
%doc %{_texmfdistdir}/doc/support/latexmk/latexmk.pdf
%doc %{_texmfdistdir}/doc/support/latexmk/latexmk.txt
%doc %{_mandir}/man1/latexmk.1*
%doc %{_texmfdir}/doc/man/man1/latexmk.man1.pdf
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_bindir}
pushd %{buildroot}%{_bindir}
    ln -sf %{_texmfdistdir}/scripts/latexmk/latexmk.pl latexmk
popd
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf texmf-dist %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_mandir}/man1
mv %{buildroot}%{_texmfdir}/doc/man/man1/*.1 %{buildroot}%{_mandir}/man1
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
