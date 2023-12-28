#  __                                                  __                       _         __                
# |/  |                /                               /  |    |                / |       /  |               
# |   | ___       ___ (  ___  ___  ___  ___  ___      (   | ___| ___           (__/      (   | _ _  ___  ___ 
# |   )|___) \  )|___)| |   )|   )|___)|   )|___      |   )|   )|   )\   )      / \)     |   )| | )|   )|   )
# |__/ |__    \/ |__  | |__/ |__/ |__  |     __/      |__/ |__/ |__/| \_/      |__/\     |__/ |  / |__/||    
#                           |                                         /                                     
# Design & Implementation SQL Inection Scanner .
# The Project for Education purpose only :).
# Final Year Software Enigeering at SPU .

import random
from oday.common.config import conf
from oday.core.request import request
from oday.logger.colored_logger import logger
from oday.common.lib import re, time, collections, quote, unquote, URLError
from oday.common.utils import (
    prepare_attack_request,
)


def inject_expression(
    url,
    data,
    proxy,
    delay=0,
    timesec=5,
    timeout=30,
    headers=None,
    parameter=None,
    expression=None,
    is_multipart=False,
    injection_type=None,
    connection_test=False,
):
    attack = None
    attack_url = url
    attack_data = data
    attack_headers = headers
    # expression = (
    #     urlencode(value=expression)
    #     if injection_type.upper() not in ["HEADER"]
    #     else expression
    # )
    if conf.timeout and conf.timeout > 30:
        timeout = conf.timeout
    if not connection_test:
        if injection_type in ["HEADER", "COOKIE"]:
            attack_headers = prepare_attack_request(
                headers,
                expression,
                param=parameter,
                injection_type=injection_type,
            )
        if injection_type == "GET":
            attack_url = prepare_attack_request(
                url,
                expression,
                param=parameter,
                encode=True,
                injection_type=injection_type,
            )

        if injection_type == "POST":
            attack_data = prepare_attack_request(
                data,
                expression,
                param=parameter,
                encode=True,
                injection_type=injection_type,
            )
    try:
        attack = request.perform(
            url=attack_url,
            data=attack_data,
            proxy=conf.proxy,
            headers=attack_headers,
            connection_test=connection_test,
            is_multipart=conf.is_multipart,
            timeout=timeout,
        )
        if attack.status_code == 401:
            logger.warning(
                "It seems the session got expired, update the session and re-run"
            )
            logger.end("ending")
            exit(0)
    except URLError as e:
        tried = 1
        logger.critical(f"{e.reason}. oday is going to retry..")
        response_ok = False
        while tried <= conf.retry:
            attack = inject_expression(
                url,
                data,
                proxy,
                delay=delay,
                timesec=timesec,
                timeout=timeout,
                headers=headers,
                parameter=parameter,
                expression=expression,
                is_multipart=is_multipart,
                injection_type=injection_type,
            )
            tried += 1
            if attack.ok:
                response_ok = True
                break
        if response_ok:
            return attack
        else:
            logger.end("ending")
            exit(0)
    except ConnectionAbortedError as e:
        raise e
    except ConnectionRefusedError as e:
        raise e
    except ConnectionResetError as e:
        raise e
    except KeyboardInterrupt as e:
        raise e
    except TimeoutError as e:
        raise e
    except Exception as e:
        tried = 1
        logger.critical(f"{e.reason}. oday is going to retry..")
        response_ok = False
        while tried <= conf.retry:
            attack = inject_expression(
                url,
                data,
                proxy,
                delay=delay,
                timesec=timesec,
                timeout=timeout,
                headers=headers,
                parameter=parameter,
                expression=expression,
                is_multipart=is_multipart,
                injection_type=injection_type,
            )
            tried += 1
            if attack.ok:
                response_ok = True
                break
        if response_ok:
            return attack
        raise e
    return attack
