Summary:	A set of GNU Interactive Tools
Name: 		gnuit
Version:	4.9.5
Release:	%mkrel 2
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





%changelog
* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 4.9.5-2mdv2011.0
+ Revision: 610953
- rebuild

* Thu Apr 01 2010 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 4.9.5-1mdv2010.1
+ Revision: 530734
- Upstream renamed project to gnuit
- Upstream renamed the package to "gnuit"
- New version: 4.9.5
- Spec and patches adapted to new name

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Thu Aug 07 2008 Thierry Vignaud <tv@mandriva.org> 4.3.20-20mdv2009.0
+ Revision: 266925
- rebuild early 2009.0 package (before pixel changes)

* Wed Jun 11 2008 Anssi Hannula <anssi@mandriva.org> 4.3.20-19mdv2009.0
+ Revision: 218151
- remove now unneeded conflicts with linus-git (Paulo prefixed the
  programs)
- simplify obsoletes versioning

* Wed Jun 11 2008 Paulo Andrade <pcpa@mandriva.com.br> 4.3.20-18mdv2009.0
+ Revision: 218119
- Rename git directory to gnu-git, to match new package name.
- Fix some typos in documentation patch.
  Add a conflicts with older versions of linus-git package.
- Rename spec file.
- Modify the git package so that it can be renamed to gnu-git, and not
  conflict with linus-git package, that should be renamed to just git.
  This should address #34692 (Installing git isn't easy...)

  + Andreas Hasenack <andreas@mandriva.com>
    - rebuild for 2008.1

  + Oden Eriksson <oeriksson@mandriva.com>
    - rebuild

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Thu Sep 20 2007 Adam Williamson <awilliamson@mandriva.org> 4.3.20-14mdv2008.0
+ Revision: 91265
- rebuild for 2008

