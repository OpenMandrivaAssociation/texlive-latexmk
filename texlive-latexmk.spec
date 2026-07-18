%global tl_name latexmk
%global tl_revision 78335
%global tl_bin_links latexmk:%{_texmfdistdir}/scripts/latexmk/latexmk.pl

Name:		texlive-%{tl_name}
Epoch:		1
Version:	4.88
Release:	%{tl_revision}.1
Summary:	Fully automated LaTeX document generation
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/support/latexmk
License:	gpl2
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/latexmk.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/latexmk.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(latexmk.bin)
Provides:	texlive(%{tl_name}) = %{tl_revision}
Provides:	texlive(%{tl_name}.bin) = %{tl_revision}
Provides:	texlive-%{tl_name}.bin = %{EVRD}

%description
Latexmk completely automates the process of generating a LaTeX document.
Given the source files for a document, latexmk issues the appropriate
sequence of commands to generate a .dvi, .ps, .pdf or hardcopy version
of the document. An important feature is the "preview continuous mode",
where the script watches all of the source files (primary file and
included TeX and graphics files), and reruns LaTeX, etc., whenever a
source file has changed. Thus a previewer can offer a display of the
document's latest state.

