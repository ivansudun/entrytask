# -*- coding: utf-8 -*-

SUCCESS_CODE = 0
SYSTEM_ERRCODE = 11
PARAMS_ERRCODE = 21
CODE_MAP = {
    SUCCESS_CODE:"success",
    SYSTEM_ERRCODE:"system error",
    PARAMS_ERRCODE:"empty or wrong params"
}


def return_json(code, a=None, b=None):
    """
        功能：根据错误码返回对应的错误信息
        Param：
            code 错误码
            a request传入的参数a
            b request传入的参数b
        return：
            错误信息，包含err_code和err_msg
    """
    if code not in CODE_MAP:
        code = SYSTEM_ERRCODE

    return {
        "err_code" : code,
        "err_msg": CODE_MAP[code],
        "reference": "NO.%d is %s" % ( a, b )  if code == SUCCESS_CODE else CODE_MAP[code],
    }

