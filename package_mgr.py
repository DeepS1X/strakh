from pwn import *
def resolve_distro_package_mgr(distro):
    if(distro="some sort of debian"):                                                                                                                                                 pkg_install="apt install {}"
        pkg_upgrade="apt update && apt upgrade"
    if(distro="redhat/fedora/centos"):
        pkg_install="yum install {}"                                                                                                                                                  pkg_upgrade="yum update"
    if(distro="OpenSUSE"):
        pkg_install="zypper in {}"                                                                                                                                                    pkg_upgrade="zypper up"
    if(distro="fedora 22+"):                                                                                                                                                          pkg_install="install {}"                                                                                                                                                      pkg_upgrade="dnf update"
    if(distro="sabayon or whatever its called"):
        pkg_install="equo in {}"
        pkg_upgrade="equo up && equo u"
    if(distro="arch linux"):                                                                                                                                                          pkg_install="pacman -S {}"
        pkg_upgrade="pacman -Syu"
