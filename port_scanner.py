""" very simple program to check open ports on a given host """

import socket

if __name__ == "__main__":
  starting_port = int(raw_input('What is the starting port? '))
  ending_port = int(raw_input('What is the ending port? '))
  host = raw_input('What is the IP address of the host? ')
  hostname = socket.gethostbyname(host)
  try:
    for i in range(starting_port,ending_port + 1):
      s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
      status = s.connect_ex((host,i))
      if status == 0:
        print ('Port {0} is open on host {1} ').format(i,hostname)
      s.close()
  except socket.error:
    print ('socket error')
