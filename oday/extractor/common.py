  #__                                                  __                       _         __                
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
from oday.common.session import session
from oday.core.extract import oday_extractor
from oday.logger.colored_logger import logger
from oday.common.payloads import (
    PAYLOADS_BANNER,
    PAYLOADS_CURRENT_USER,
    PAYLOADS_CURRENT_DATABASE,
    PAYLOADS_DBS_COUNT,
    PAYLOADS_TBLS_COUNT,
    PAYLOADS_COLS_COUNT,
    PAYLOADS_RECS_COUNT,
    PAYLOADS_HOSTNAME,
)

from oday.common.lib import collections


class OdayCommon:
    """This class will be used to fetch common thing like database, user, version"""

    def fetch_banner(
        self,
        url,
        data,
        vector,
        parameter,
        headers,
        base,
        injection_type,
        backend="",
        proxy=None,
        is_multipart=False,
        timeout=30,
        delay=0,
        timesec=5,
        attack=None,
        match_string=None,
        not_match_string=None,
        code=None,
        text_only=False,
    ):
        logger.info("fetching banner")
        Response = collections.namedtuple(
            "Response",
            ["ok", "error", "result", "payload"],
        )
        guess = oday_extractor.fetch_characters(
            url=url,
            data=data,
            vector=vector,
            parameter=parameter,
            headers=headers,
            base=base,
            injection_type=injection_type,
            payloads=PAYLOADS_BANNER.get(backend),
            backend=backend,
            proxy=proxy,
            is_multipart=is_multipart,
            timeout=timeout,
            delay=delay,
            timesec=timesec,
            attack01=attack,
            match_string=match_string,
            not_match_string=not_match_string,
            code=code,
            query_check=True,
            text_only=text_only,
        )
        if guess.ok:
            logger.debug(f"working payload found: '{guess.payload}'")
            retval = oday_extractor.fetch_characters(
                url=url,
                data=data,
                vector=vector,
                parameter=parameter,
                headers=headers,
                base=base,
                injection_type=injection_type,
                payloads=[guess.payload],
                backend=backend,
                proxy=proxy,
                is_multipart=is_multipart,
                timeout=timeout,
                delay=delay,
                timesec=timesec,
                attack01=attack,
                match_string=match_string,
                not_match_string=not_match_string,
                code=code,
                text_only=text_only,
                dump_type="banner",
            )
            if retval.ok:
                if retval.resumed:
                    logger.info("resumed: '%s'" % (retval.result))
                else:
                    logger.info("retrieved: '%s'" % (retval.result))
                logger.success(f"banner: '{retval.result}'")
            else:
                error = retval.error
                if error:
                    message = (
                        f"oday detected an error during banner extraction ({error})"
                    )
                    logger.warning(f"{message}")
                logger.end("ending")
                exit(0)
        else:
            retval = guess
        return retval

    def fetch_current_user(
        self,
        url,
        data,
        vector,
        parameter,
        headers,
        base,
        injection_type,
        backend="",
        proxy=None,
        is_multipart=False,
        timeout=30,
        delay=0,
        timesec=5,
        attack=None,
        match_string=None,
        not_match_string=None,
        code=None,
        text_only=False,
    ):
        logger.info("fetching current user")
        Response = collections.namedtuple(
            "Response",
            ["ok", "error", "result", "payload"],
        )
        guess = oday_extractor.fetch_characters(
            url=url,
            data=data,
            vector=vector,
            parameter=parameter,
            headers=headers,
            base=base,
            injection_type=injection_type,
            payloads=PAYLOADS_CURRENT_USER.get(backend),
            backend=backend,
            proxy=proxy,
            is_multipart=is_multipart,
            timeout=timeout,
            delay=delay,
            timesec=timesec,
            attack01=attack,
            match_string=match_string,
            not_match_string=not_match_string,
            code=code,
            query_check=True,
            text_only=text_only,
        )
        if guess.ok:
            logger.debug(f"working payload found: '{guess.payload}'")
            retval = oday_extractor.fetch_characters(
                url=url,
                data=data,
                vector=vector,
                parameter=parameter,
                headers=headers,
                base=base,
                injection_type=injection_type,
                payloads=[guess.payload],
                backend=backend,
                proxy=proxy,
                is_multipart=is_multipart,
                timeout=timeout,
                delay=delay,
                timesec=timesec,
                attack01=attack,
                match_string=match_string,
                not_match_string=not_match_string,
                code=code,
                text_only=text_only,
                dump_type="current_user",
            )
            if retval.ok:
                if retval.resumed:
                    logger.info("resumed: '%s'" % (retval.result))
                else:
                    logger.info("retrieved: '%s'" % (retval.result))
                logger.success(f"current user: '{retval.result}'")
            else:
                error = retval.error
                if error:
                    message = f"oday detected an error during current user extraction ({error})"
                    logger.warning(f"{message}")
                logger.end("ending")
                exit(0)
        else:
            retval = guess
        return retval

    def fetch_hostname(
        self,
        url,
        data,
        vector,
        parameter,
        headers,
        base,
        injection_type,
        backend="",
        proxy=None,
        is_multipart=False,
        timeout=30,
        delay=0,
        timesec=5,
        attack=None,
        match_string=None,
        not_match_string=None,
        code=None,
        text_only=False,
    ):
        logger.info("fetching hostname")
        Response = collections.namedtuple(
            "Response",
            ["ok", "error", "result", "payload"],
        )
        guess = oday_extractor.fetch_characters(
            url=url,
            data=data,
            vector=vector,
            parameter=parameter,
            headers=headers,
            base=base,
            injection_type=injection_type,
            payloads=PAYLOADS_HOSTNAME.get(backend),
            backend=backend,
            proxy=proxy,
            is_multipart=is_multipart,
            timeout=timeout,
            delay=delay,
            timesec=timesec,
            attack01=attack,
            match_string=match_string,
            not_match_string=not_match_string,
            code=code,
            query_check=True,
            text_only=text_only,
        )
        if guess.ok:
            logger.debug(f"working payload found: '{guess.payload}'")
            retval = oday_extractor.fetch_characters(
                url=url,
                data=data,
                vector=vector,
                parameter=parameter,
                headers=headers,
                base=base,
                injection_type=injection_type,
                payloads=[guess.payload],
                backend=backend,
                proxy=proxy,
                is_multipart=is_multipart,
                timeout=timeout,
                delay=delay,
                timesec=timesec,
                attack01=attack,
                match_string=match_string,
                not_match_string=not_match_string,
                code=code,
                text_only=text_only,
                dump_type="hostname",
            )
            if retval.ok:
                if retval.resumed:
                    logger.info("resumed: '%s'" % (retval.result))
                else:
                    logger.info("retrieved: '%s'" % (retval.result))
                logger.success(f"hostname: '{retval.result}'")
            else:
                error = retval.error
                if error:
                    message = f"oday detected an error during current user extraction ({error})"
                    logger.warning(f"{message}")
                logger.end("ending")
                exit(0)
        else:
            retval = guess
        return retval

    def fetch_current_database(
        self,
        url,
        data,
        vector,
        parameter,
        headers,
        base,
        injection_type,
        backend="",
        proxy=None,
        is_multipart=False,
        timeout=30,
        delay=0,
        timesec=5,
        attack=None,
        match_string=None,
        not_match_string=None,
        code=None,
        text_only=False,
    ):
        logger.info("fetching current database")
        Response = collections.namedtuple(
            "Response",
            ["ok", "error", "result", "payload"],
        )
        guess = oday_extractor.fetch_characters(
            url=url,
            data=data,
            vector=vector,
            parameter=parameter,
            headers=headers,
            base=base,
            injection_type=injection_type,
            payloads=PAYLOADS_CURRENT_DATABASE.get(backend),
            backend=backend,
            proxy=proxy,
            is_multipart=is_multipart,
            timeout=timeout,
            delay=delay,
            timesec=timesec,
            attack01=attack,
            match_string=match_string,
            not_match_string=not_match_string,
            code=code,
            text_only=text_only,
            query_check=True,
        )
        if guess.ok:
            logger.debug(f"working payload found: '{guess.payload}'")
            retval = oday_extractor.fetch_characters(
                url=url,
                data=data,
                vector=vector,
                parameter=parameter,
                headers=headers,
                base=base,
                injection_type=injection_type,
                payloads=[guess.payload],
                backend=backend,
                proxy=proxy,
                is_multipart=is_multipart,
                timeout=timeout,
                delay=delay,
                timesec=timesec,
                attack01=attack,
                match_string=match_string,
                not_match_string=not_match_string,
                code=code,
                text_only=text_only,
                dump_type="current_db",
            )
            if retval.ok:
                if retval.resumed:
                    logger.info("resumed: '%s'" % (retval.result))
                else:
                    logger.info("retrieved: '%s'" % (retval.result))
                logger.success(f"current database: '{retval.result}'")
            else:
                error = retval.error
                if error:
                    message = f"oday detected an error during current database extraction ({error})"
                    logger.warning(f"{message}")
                logger.end("ending")
                exit(0)
        else:
            retval = guess
        return retval


target = OdayCommon()
