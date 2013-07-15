# revision 27474
# category Package
# catalog-ctan /support/latexmk
# catalog-date 2012-08-20 08:32:37 +0200
# catalog-license gpl
# catalog-version 4.33c
Name:		texlive-latexmk
Version:	4.33c
Release:	1
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
changed. Thus a previewer can have an updated display whenever
the source files change.

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
%doc %{_texmfdistdir}/doc/support/latexmk/CHANGES
%doc %{_texmfdistdir}/doc/support/latexmk/COPYING
%doc %{_texmfdistdir}/doc/support/latexmk/INSTALL
%doc %{_texmfdistdir}/doc/support/latexmk/README
%doc %{_texmfdistdir}/doc/support/latexmk/example_rcfiles/README
%doc %{_texmfdistdir}/doc/support/latexmk/example_rcfiles/Sweave_latexmkrc
%doc %{_texmfdistdir}/doc/support/latexmk/example_rcfiles/asymptote_latexmkrc
%doc %{_texmfdistdir}/doc/support/latexmk/example_rcfiles/glossary_latexmkrc
%doc %{_texmfdistdir}/doc/support/latexmk/example_rcfiles/mpost_latexmkrc
%doc %{_texmfdistdir}/doc/support/latexmk/example_rcfiles/pdflatexmkrc
%doc %{_texmfdistdir}/doc/support/latexmk/example_rcfiles/sagetex_latexmkrc
%doc %{_texmfdistdir}/doc/support/latexmk/example_rcfiles/sweave_latexmkrc
%doc %{_texmfdistdir}/doc/support/latexmk/example_rcfiles/xelatex_latexmkrc
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
%doc %{_texmfdistdir}/doc/support/latexmk/latexmk.pdf
%doc %{_texmfdistdir}/doc/support/latexmk/latexmk.txt
%doc %{_mandir}/man1/latexmk.1*
%doc %{_texmfdir}/doc/man/man1/latexmk.man1.pdf
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
cp -fpar texmf texmf-dist %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_mandir}/man1
mv %{buildroot}%{_texmfdir}/doc/man/man1/*.1 %{buildroot}%{_mandir}/man1


%changelog
* Mon Oct 29 2012 Paulo Andrade <pcpa@mandriva.com.br> 4.33c-1
+ Revision: 820613
- Update to latest release.
- Update to latest release.
- Update to latest release.

* Fri Apr 13 2012 Paulo Andrade <pcpa@mandriva.com.br> 4.31-1
+ Revision: 790645
- Update to latest release.

* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 4.30a-2
+ Revision: 753182
- Rebuild to reduce used resources

* Sat Dec 17 2011 Paulo Andrade <pcpa@mandriva.com.br> 4.30a-1
+ Revision: 743292
- texlive-latexmk

* Fri Dec 09 2011 Paulo Andrade <pcpa@mandriva.com.br> 4.28c-1
+ Revision: 739821
- texlive-latexmk

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 4.27a-1
+ Revision: 718823
- texlive-latexmk
- texlive-latexmk
- texlive-latexmk
- texlive-latexmk

