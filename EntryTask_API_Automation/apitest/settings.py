# -*- coding: utf-8 -*-

SUCCESS_CODE = 0
SYSTEM_ERRCODE = 11
PARAMS_ERRCODE = 21
CODE_MAP = {
    SUCCESS_CODE:"success",
    SYSTEM_ERRCODE:"system error",
    PARAMS_ERRCODE:"empty or wrong params"
}


def return_json(code):
    """
        功能：根据错误码返回对应的错误信息
        Param：
            code 错误码
        return：
            错误信息，包含error_code和error-message
    """
    if code not in CODE_MAP:
        code = SYSTEM_ERRCODE

    return {
        "error_code" : code,
        "error_message": CODE_MAP[code],
    }

