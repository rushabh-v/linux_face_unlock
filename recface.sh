#!/bin/bash
function facerec(){
$1
if [ "$1" = "new" ]; then
    python /lib/Auth/RecFace/add_new.py
if [ "$1" = "enable" ]; then
    sudo pam-auth-update
if [ "$1" = "disable" ]; then
    sudo apt-get --reinstall install libpam-runtime libpam-modules

