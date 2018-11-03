# -*- coding: utf-8 -*-
"""
Created on Sat Nov  3 13:36:18 2018

@author: Yosiyoshi
DJI/Ryze Tech Tello AutoPilot sample to let it take off and fly a while, if battery is empty, it'll automatically land.
Warning: It's your responsibility to fail or make errors in executing this program code, or get any bad aftermath.
Local usage: from drone import TelloAutoPilot
(c) 2018 Yosiyoshi All Rights Reserved.
"""
import threading
import socket
import time
import sys

class TelloAutoPilot():
    def initConnection(self):
        host = ''
        port = 9002
        locaddr = (host,port)
        self.tello = ('192.168.10.1', 8889)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind(locaddr)
    
        recvThread = threading.Thread(target=self.recvSocket)
        recvThread.setDaemon(True)
        recvThread.start()
        try:
            sent = self.sock.sendto('command'.encode(encoding="utf-8"), self.tello)
        except:
            pass
        try:
            sent = self.sock.sendto('speed 50'.encode(encoding="utf-8"), self.tello)
        except:
            pass

    def end(self):
        sys.exit()

    def takeoff(self):
        try:
            sent = self.sock.sendto('takeoff'.encode(encoding="utf-8"), self.tello)
        except:
            pass
    def land(self):
        try:
            sent = self.sock.sendto('land'.encode(encoding="utf-8"), self.tello)
        except:
            pass
    def up(self):
        try:
            sent = self.sock.sendto('up 20'.encode(encoding="utf-8"), self.tello)
        except:
            pass
    def down(self):
        try:
            sent = self.sock.sendto('down 20'.encode(encoding="utf-8"), self.tello)
        except:
            pass
    def cw(self):
        try:
            sent = self.sock.sendto('cw 45'.encode(encoding="utf-8"), self.tello)
        except:
            pass
    def ccw(self):
        try:
            sent = self.sock.sendto('ccw 45'.encode(encoding="utf-8"), self.tello)
        except:
            pass
    def forward(self):
        try:
            sent = self.sock.sendto('forward 20'.encode(encoding="utf-8"), self.tello)
        except:
            pass
    def back(self):
        try:
            sent = self.sock.sendto('back 20'.encode(encoding="utf-8"), self.tello)
        except:
            pass
    def right(self):
        try:
            sent = self.sock.sendto('right 20'.encode(encoding="utf-8"), self.tello)
        except:
            pass
    def left(self):
        try:
            sent = self.sock.sendto('left 20'.encode(encoding="utf-8"), self.tello)
        except:
            pass
    def battery(self):
        try:
            sent = self.sock.sendto('battery?'.encode(encoding="utf-8"), self.tello)
        except:
            pass
    def time(self):
        try:
            sent = self.sock.sendto('time?'.encode(encoding="utf-8"), self.tello)
        except:
            pass

    def recvSocket(self):
        while True: 
            try:
                data, server = self.sock.recvfrom(1518)
                self.label.setText(data.decode(encoding="utf-8").strip())
            except:
                pass

if __name__ == '__main__':
    tap=TelloAutoPilot()
    tap.initConnection()
    tap.takeoff()
    tap.land()
    sys.exit()
