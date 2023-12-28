#  __                                                  __                       _         __                
# |/  |                /                               /  |    |                / |       /  |               
# |   | ___       ___ (  ___  ___  ___  ___  ___      (   | ___| ___           (__/      (   | _ _  ___  ___ 
# |   )|___) \  )|___)| |   )|   )|___)|   )|___      |   )|   )|   )\   )      / \)     |   )| | )|   )|   )
# |__/ |__    \/ |__  | |__/ |__/ |__  |     __/      |__/ |__/ |__/| \_/      |__/\     |__/ |  / |__/||    
#                           |                                         /                                     
# Design & Implementation SQL Inection Scanner .
# The Project for Education purpose only :).
# Final Year Software Enigeering at SPU .

from oday.common.lib import (
    re,
    time,
    html,
    chardet,
    requests,
    urlparse,
    collections,
    URLError,
    build_opener,
    Request,
    urlopen,
    HTTPError,
    quote,
    socket,
    install_opener,
)
from oday.common.utils import (
    unescape_html,
    prepare_request,
    parse_http_error,
    prepare_response,
    parse_http_response,
    SmartRedirectHandler,
)
from oday.logger.colored_logger import logger
from oday.common.config import conf


class HTTPRequestHandler:
    """
    oday requests handler
    """

    def perform(
        self,
        url,
        data="",
        proxy="",
        headers="",
        timeout=30,
        verify=False,
        use_requests=False,
        connection_test=False,
        follow_redirects=True,
        is_multipart=False,
    ):
        HTTPResponse = collections.namedtuple(
            "HTTPResponse",
            [
                "ok",
                "url",
                "data",
                "text",
                "path",
                "method",
                "reason",
                "headers",
                "error_msg",
                "redirected",
                "request_url",
                "status_code",
                "response_time",
                "content_length",
                "filtered_text",
            ],
        )
        if connection_test:
            clean_up = lambda _: _.replace("*", "") if _ and "*" in _ else _
            url = clean_up(url)
            data = clean_up(data)
            headers = clean_up(headers)

        req = prepare_request(
            url=url, data=data, custom_headers=headers, use_requests=use_requests
        )
        raw = req.raw
        endpoint = req.endpoint
        custom_headers = req.headers
        if conf.is_json:
            custom_headers.update({"Content-Type": "application/json"})
        request_url = req.request.get("url")
        logger.traffic_out(f"HTTP request [#{conf.request_counter}]:\n{raw}")
        headers = {}
        method = ""
        if proxy:
            if not use_requests:
                proxy = proxy.for_urllib
            if use_requests:
                proxy = proxy.for_requests
        else:
            proxy = None
        if not data:
            method = "GET"
            start_time = time.time()
            try:
                if not use_requests:
                    handlers = []
                    if proxy:
                        handlers.append(proxy)
                    if conf.follow_redirects == None:
                        handlers.append(SmartRedirectHandler())
                    if not conf.follow_redirects:
                        if len(handlers) == 1:
                            handlers.append(SmartRedirectHandler())
                        if not handlers:
                            handlers.append(SmartRedirectHandler())
                    opener = build_opener(*handlers)
                    request = Request(url=url, headers=custom_headers)
                    response = opener.open(request, timeout=timeout)
                else:
                    response = requests.get(
                        url,
                        headers=custom_headers,
                        proxies=proxy,
                        timeout=timeout,
                        allow_redirects=follow_redirects,
                        verify=verify,
                    )
                    response.raise_for_status()
                end_time = time.time()
                response_time = end_time - start_time
                parsed_response = parse_http_response(response)
            except (
                HTTPError,
                requests.exceptions.HTTPError,
            ) as e:
                end_time = time.time()
                response_time = end_time - start_time
                parsed_response = parse_http_error(e)
            except (socket.timeout, requests.exceptions.ReadTimeout) as e:
                logger.debug("read timeout during connection response reading..")
                conf._readtimout_counter += 1
                conf.timeout = 25
                conf.timesec = 10
                end_time = time.time()
                response_time = end_time - start_time
                parsed_response = parse_http_error(e, url=url, is_timeout=True)
            except URLError as e:
                raise e
            except TimeoutError as e:
                logger.warning(
                    f"connection timeout, target is very slow to respond, increase value to --timeout=300"
                )
                raise e
            except ConnectionAbortedError as e:
                raise e
            except ConnectionRefusedError as e:
                raise e
            except ConnectionResetError as e:
                raise e
            except KeyboardInterrupt as e:
                raise e
            except Exception as e:
                raise e
        if data:
            method = "POST"
            start_time = time.time()
            try:
                if not use_requests:
                    post_data = data.encode("utf-8")
                    handlers = []
                    if proxy:
                        handlers.append(proxy)
                    if conf.follow_redirects == None:
                        handlers.append(SmartRedirectHandler())
                    if not conf.follow_redirects:
                        if len(handlers) == 1:
                            handlers.append(SmartRedirectHandler())
                        if not handlers:
                            handlers.append(SmartRedirectHandler())
                    opener = build_opener(*handlers)
                    request = Request(url=url, data=post_data, headers=custom_headers)
                    response = opener.open(request, timeout=timeout)
                else:
                    response = requests.post(
                        url,
                        data=data,
                        headers=custom_headers,
                        proxies=proxy,
                        timeout=timeout,
                        allow_redirects=follow_redirects,
                        verify=verify,
                    )
                    response.raise_for_status()
                end_time = time.time()
                response_time = end_time - start_time
                parsed_response = parse_http_response(response)
            except (
                HTTPError,
                requests.exceptions.HTTPError,
            ) as e:
                end_time = time.time()
                response_time = end_time - start_time
                parsed_response = parse_http_error(e)
            except (socket.timeout, requests.exceptions.ReadTimeout) as e:
                logger.debug("read timeout during connection response reading.")
                conf._readtimout_counter += 1
                conf.timeout = 25
                conf.timesec = 10
                end_time = time.time()
                response_time = end_time - start_time
                parsed_response = parse_http_error(e, url=url, is_timeout=True)
            except URLError as e:
                raise e
            except TimeoutError as e:
                logger.warning(
                    f"connection timeout, target is very slow to respond, increase value to --timeout=300"
                )
                raise e
            except ConnectionAbortedError as e:
                logger.critical(
                    f"connection attempt to the target URL was aborted by the peer."
                )
                raise e
            except ConnectionRefusedError as e:
                logger.critical(
                    f"connection attempt to the target URL was refused by the peer."
                )
                raise e
            except ConnectionResetError as e:
                logger.critical(
                    f"connection attempt to the target URL was reset by the peer."
                )
                raise e
            except KeyboardInterrupt as e:
                raise e
            except Exception as e:
                raise e
        redirected = bool(parsed_response.status_code in [301, 302, 303, 307])
        http_response = HTTPResponse(
            ok=parsed_response.ok,
            url=parsed_response.url,
            data=data,
            text=parsed_response.text,
            path=endpoint,
            method=method,
            reason=parsed_response.reason,
            headers=parsed_response.headers,
            error_msg=parsed_response.error,
            redirected=redirected,
            request_url=request_url,
            status_code=parsed_response.status_code,
            response_time=response_time,
            content_length=parsed_response.content_length,
            filtered_text=parsed_response.filtered_text,
        )
        raw_response = prepare_response(http_response)
        logger.traffic_in(f"HTTP response {raw_response}\n")
        conf.request_counter += 1
        return http_response


request = HTTPRequestHandler()
