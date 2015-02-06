%define format	text-en
%define format2	TEXT/en
%define	format3 text

%define version 2007
%define release 6

Summary:	HOWTO documents (%{format3} format) from the Linux Documentation Project
Name:		howto-%{format}
Version: 	%version
Release: 	%release
Group:		Books/Howtos
Source0:	Linux-HOWTOs.tar.bz2
Url:		http://www.tldp.org/docs.html#howto
License:	GPL
BuildRoot:	%{_tmppath}/howto-%{format}-root
BuildArchitectures: noarch
Requires:   locales-en howto-utils
BuildRequires:  howto-utils

%description
Linux HOWTOs are detailed documents which describe a specific aspect of 
configuring or using Linux.  Linux HOWTOs are a great source of
practical information about your system.  The latest versions of these
documents are located at http://www.linuxdoc.org/docs.html#howto

Install this package if you'd like to be able to access the Linux
HOWTO documentation from your own system.

%prep 
rm -rf $RPM_BUILD_ROOT

%install
mkdir -p $RPM_BUILD_ROOT%{_docdir}/HOWTO/%{format2}
cd $RPM_BUILD_ROOT%{_docdir}/HOWTO/%{format2}
bzcat %{SOURCE0} | tar xv

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_docdir}/HOWTO/%{format2}



%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 2007-5mdv2011.0
+ Revision: 619428
- the mass rebuild of 2010.0 packages

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 2007-4mdv2010.0
+ Revision: 429415
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 2007-3mdv2009.0
+ Revision: 246994
- rebuild

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 2007-1mdv2008.1
+ Revision: 140753
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - better description
    - kill re-definition of %%buildroot on Pixel's request
    - import howto-text-en


* Tue Apr 18 2006 Stew Benedict <sbenedict@mandriva.com> 2007-1mdk
- update 20060418, 2007

* Thu Dec 08 2005 Lenny Cartier <lenny@mandriva.com> 2006-1mdk
- update 20051208, 2006

* Fri Nov 19 2004 Stew Benedict <sbenedict@mandrakesoft.com> 10.2-1mdk
- update 20041119, 10.2

* Thu Oct 09 2003 Lenny Cartier <lenny@mandrakesoft.com> 9.2-1mdk
- updated

* Thu Jan 16 2003 Stew Benedict <sbenedict@mandrakesoft.com> 9.1-1mdk
- update 20030116

* Fri Sep 13 2002 Lenny Cartier <lenny@mandrakesoft.com> 9.0-1mdk
- Update

* Thu Sep 06 2001 Etienne FAURE <etienne@mandrakesoft.com> 8.1-1mdk
- Updated: Thu Sep 06 2001
- Add Require on locale-en

* Thu May 31 2001 Laurent Culioli <laurent@mandrakesoft.com> 8.0-1mdk
- initial specfile ( thanks me viet !)
- based on howto-text-fr specfile



