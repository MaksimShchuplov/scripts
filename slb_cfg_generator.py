import sys


__author__ = 'max'
arglist = sys.argv

#arglist = "video12000", "10.40.231.41", "10.40.231.41", "1.1.177.241"
servername1 = arglist[1]
servername2 = servername1[:-1] + "1"
ip1 = arglist[2]
ip2 = arglist[3]
ip3 = arglist[4]
print
print

print "server real", servername1, ip1
print"""port http
port http url "HEAD /csm-status/" """
print
print "server real", servername2, ip2
print"""port http
port http url "HEAD /csm-status/" """
print
print
print "server virtual", servername1, ip3

print """sym-priority 15
sym-active
predictor least-conn
port default dsr
port http
port http dsr"""
print "bind http", servername1, "http", servername2, "http"
print
print
print
