#  Write a program print all running procs in a your system

import psutil

for proc in psutil.process_iter():
    print(proc.name())

"""
{
proc name : memory 
}
"""