# -*- coding: utf-8 -*-

__author__ = 'haiwei'

import binascii
import re

class Convertor:

    decode_function_suffix  = '2ascii'
    encode_function_preffix = 'ascii2'

    black_separators = "[\s+\.\!\/_,$%^*(+\"\']+|[+——！，。？、~@#￥%……&*（）]+".decode("utf8")

    @staticmethod
    def hex2ascii(enstr, res, path=None):
        #res    = ['']
        name_error = ''
        if path is None:
            if enstr is "" or enstr is None:
                return res
            else:
                strlen = len(enstr)
                if strlen >= 2 and enstr[0] == '0' and enstr[1] == 'x':
                    enstr  = enstr[2:]
                    strlen -= 2

                if strlen % 2 != 0:
                    enstr  += '0'
                    strlen += 1
                    name_error = '输入位数不足，默认使用0补全'

                res[0] = binascii.a2b_hex(str(enstr))

                if name_error is not "":
                    raise NameError(name_error)

    @staticmethod
    def ascii2hex(enstr, res, path=None):
        #res    = ['']
        if path is None:
            if str(enstr) is "" or enstr is None:
                return res
            else:
                res[0] = '0x'
                res[0] += binascii.b2a_hex(str(enstr))


    @staticmethod
    def dec2ascii(enstr, res, path=None):
        #res    = ['']
        name_error = ''
        if path is None:
            if enstr is "" or enstr is None:
                return res
            else:
                str_t = re.split(Convertor.black_separators, enstr)
                res[0] = map(int, str_t)
                res[0] = map(chr, res[0])
                res[0] = ''.join(res[0])

    @staticmethod
    def ascii2dec(enstr, res, path=None):
        #res    = ['']
        if path is None:
            if str(enstr) is "" or enstr is None:
                return res
            else:
                res[0] = map(ord,str(enstr))
                res[0] = map(str,res[0])
                res[0] = ",".join(res[0])