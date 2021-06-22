from typing import Type


class process:
    def __init__(self,offset,name,pid,ppid,thds,hnds,sess,wo, w64,start,exit):
        self.offset = offset
        self.name = name
        self.pid = pid
        self.ppid = ppid
        self.thds = thds
        self.hnds = hnds
        self.sess = sess
        self.wo = wo
        self.w64 = w64
        self.start = start
        self.exit = exit
        self.dic = {}
        self.dic['offset'] = self.offset
        self.dic['name'] = self.name
        self.dic['pid'] = self.pid
        self.dic['ppid'] = self.ppid
        self.dic['thds'] = self.thds
        self.dic['hnds'] = self.hnds
        self.dic['sess'] = self.sess
        self.dic['wo'] = self.wo
        self.dic['w64'] = self.w64
        self.dic['start'] = self.start
        self.dic['exit'] = self.exit

    def get_offset(self):
        return self.offset

    def get_name(self):
        return self.name

    def get_pid(self):
        return self.pid

    def get_ppid(self):
        return self.ppid

    def get_thds(self):
        return self.thds

    def get_sess(self):
        return self.sess

    def get_wo(self):
        return self.wo

    def get_w64(self):
        return self.w64

    def get_start(self):
        return self.start

    def get_exit(self):
        return self.exit

    def get_hnds(self):
        return self.hnds

    def toString(self):
        return self.dic


