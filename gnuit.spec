Summary:	A set of GNU Interactive Tools
Name: 		gnuit
Version:	4.9.5
Release:	%mkrel 1
License:	GPLv3
Group:		File tools
URL:		http://www.gnu.org/software/gnuit/
Source: 	http://ftp.gnu.org/gnu/gnuit/%{name}-%{version}.tar.gz
Patch1:		0001-Fix-string-format-errors.patch
Patch2:		0002-Fix-linking.patch
BuildRequires:	ncurses-devel
BuildRequires:	tetex
BuildRequires:	texinfo
BuildRequires:	texi2html
Obsoletes:      gnu-git
Obsoletes:	git < 4.3.20-15
Buildroot: 	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

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

%prep
%setup -q
%apply_patches

%build
#
# (fg) 20000721 FIXME - git doesn't like libtoolize, hence the handmade
# ./configure line
# Part of these commands are also in the  "gnuit.spec" present in the upstream
# tarball
#
CFLAGS="$RPM_OPT_FLAGS" LDFLAGS='-s' \
	./configure --prefix=%{_prefix} --mandir=%{_mandir} \
		    --infodir=%{_infodir} --with-terminfo --libdir=%{_libdir} \
		    --enable-smp --disable-transition
%make

# Force rebuild of info file
pushd doc
makeinfo gnuit.texinfo
popd

%install
rm -rf %{buildroot}
%makeinstall

%files
%defattr(-,root,root,0755)
%doc ChangeLog LSM NEWS PLATFORMS PROBLEMS README INSTALL doc/gnuit.html
%{_bindir}/*
%{_bindir}/.gitaction
%{_mandir}/man1/*
%{_infodir}/*
%{_datadir}/gnuit

%clean
rm -rf %{buildroot}

%post
%{_install_info gnuit.info}

%preun
%{_remove_install_info gnuit.info}

