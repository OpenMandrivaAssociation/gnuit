Summary:	A set of GNU Interactive Tools
Name: 		gnuit
Version:	4.9.5
Release:	5
License:	GPLv3+
Group:		File tools
Url:		http://www.gnu.org/software/gnuit/
Source0:	http://ftp.gnu.org/gnu/gnuit/%{name}-%{version}.tar.gz
Patch1:		0001-Fix-string-format-errors.patch
Patch2:		0002-Fix-linking.patch
BuildRequires:	pkgconfig(ncurses)
BuildRequires:	tetex
BuildRequires:	texinfo
BuildRequires:	texi2html
Conflicts:	git

%description
gnuit (GNU Interactive Tools) provides an extensible file
system browser, an ASCII/hexadecimal file viewer, a process viewer/killer
and other related utilities and shell scripts.  gnuit can be used to increase
the speed and efficiency of copying and moving files and directories,
invoking editors, compressing and uncompressing files, creating and expanding
archives, compiling programs, sending mail and more. gnuit uses standard
ANSI color sequences, if they are available.

You should install the gnuit package if you are interested in using its file
management capabilities.

%files
%doc ChangeLog LSM NEWS PLATFORMS PROBLEMS README INSTALL doc/gnuit.html
%{_bindir}/*
%{_bindir}/.gitaction
%{_mandir}/man1/*
%{_infodir}/*
%{_datadir}/gnuit

#----------------------------------------------------------------------------

%prep
%setup -q
%apply_patches

%build
%configure2_5x
%make

# Force rebuild of info file
pushd doc
makeinfo gnuit.texinfo
popd

%install
%makeinstall_std

