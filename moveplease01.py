#!/usr/bin/env python3
"""A simple script to move two files into ceph_storage/
    Alta3 Research | rzfeeser@alta3.com"""

# standard library imports
import shutil # shell utilites will be used to move files
import os   # provides access to low level as operations agnostic to flavor of OS)

def main():

    """called at runtime"""

    os.chdir('/home/student/mycode/')    # move into this working directory

    shutil.move('raynor.obj', 'ceph_storage/')      # try moving the file raynor.obj into ceph_storage/ dir

    # program will pause while we accept input
    xname = input('What is the new name for kerrigan.ojb ')    # collect string input from user

    shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)   # moving kerrigan.obj into 
                                                                        #ceph_storage/ with new name


main()    # this calls our main function
