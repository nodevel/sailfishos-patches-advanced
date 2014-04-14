# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.27
# 

Name:       pandora-box

# >> macros
BuildArch: noarch
# << macros

Summary:    pandora-box
Version:    0.1
Release:    1
Group:      Qt/Qt
License:    TODO
URL:        http://example.org/
Source0:    %{name}-%{version}.tar.bz2
Source100:  pandora-box.yaml
Requires:   patchmanager

%description
The pandora box contains Sailfish OS 
homescreen. Opening it allows patching
it and features tweaking. 

This package contains some tweaks for
lipstick-pandora, that can be used by 
patchmanager.

%prep
%setup -q -n %{name}-%{version}

# >> setup
# << setup

%build
# >> build pre
# << build pre



# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
mkdir -p %{buildroot}/usr/share/patchmanager/patches/
mv src/pandora-5x6-launcher %{buildroot}/usr/share/patchmanager/patches/
mv src/pandora-control-center %{buildroot}/usr/share/patchmanager/patches/
mv src/pandora-editmode-title %{buildroot}/usr/share/patchmanager/patches/
mv src/pandora-force-3x3-multitask %{buildroot}/usr/share/patchmanager/patches/
mv src/pandora-lockscreen-date %{buildroot}/usr/share/patchmanager/patches/
mv src/pandora-unlimited-multitask %{buildroot}/usr/share/patchmanager/patches/
mv src/pandora-swipe-feedback %{buildroot}/usr/share/patchmanager/patches/
# << install pre

# >> install post
# << install post

%files
%defattr(-,root,root,-)
%{_datadir}/patchmanager/patches
# >> files
# << files
