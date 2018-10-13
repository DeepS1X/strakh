from pwn import *
def resolve_distro_package_mgr(s):
    if(s.run_to_end("which apt")[1]==0):
        pkg_install="apt install {}"
        pkg_upgrade="apt update && apt upgrade"
    if(s.run_to_end("which yum")[1]==0):
        pkg_install="yum install {}"
        pkg_upgrade="yum update"
    if(s.run_to_end("which pacman")[1]==0):
        pkg_install="pacman -S {}"
        pkg_upgrade="pacman -Syu"
    if(s.run_to_end("which zypper")[1]==0):
        pkg_install="zypper in {}"
        pkg_upgrade="zypper up"
    if(s.run_to_end("which dnf")[1]==0):
        pkg_install="dnf install {}"
        pkg_upgrade="dnf update"
    if(s.run_to_end("which equo")[1]==0):
        pkg_install="equo in {}"
        pkg_upgrade="equo up && equo u"
    return {"install":pkg_install,"upgrade":pkg_upgrade}
