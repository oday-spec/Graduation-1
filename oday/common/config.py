#  __                                                  __                       _         __                
# |/  |                /                               /  |    |                / |       /  |               
# |   | ___       ___ (  ___  ___  ___  ___  ___      (   | ___| ___           (__/      (   | _ _  ___  ___ 
# |   )|___) \  )|___)| |   )|   )|___)|   )|___      |   )|   )|   )\   )      / \)     |   )| | )|   )|   )
# |__/ |__    \/ |__  | |__/ |__/ |__  |     __/      |__/ |__/ |__/| \_/      |__/\     |__/ |  / |__/||    
#                           |                                         /                                     
# Design & Implementation SQL Inection Scanner .
# The Project for Education purpose only :).
# Final Year Software Enigeering at SPU .

from oday.common.lib import Lock

class OdayConfigs:
    """
    This class will be used for configruations
    """

    def __init__(
        self,
        vectors="",
        is_string=False,
        is_json=False,
        is_multipart=False,
        skip_urlencoding=False,
        filepaths=None,
        proxy=None,
        text_only=False,
        string=None,
        not_string=None,
        code=None,
        match_ratio=None,
        retry=3,
        base=None,
        attack01=None,
        delay=0,
        timesec=5,
        timeout=None,
        backend=None,
        batch=False,
        continue_on_http_error=False,
        follow_redirects=None,
        threads=None,
    ):
        self.vectors = vectors
        self.is_string = is_string
        self.is_json = is_json
        self.is_multipart = is_multipart
        self.skip_urlencoding = skip_urlencoding
        self.filepaths = filepaths
        self._session_filepath = None
        self.proxy = proxy
        self.text_only = text_only
        self.string = string
        self.not_string = not_string
        self.code = code
        self.match_ratio = match_ratio
        self.retry = retry
        self.base = base
        self.attack01 = attack01
        self.backend = backend
        self.batch = batch
        self.http_codes = {}
        self.timeout = timeout
        self.delay = delay
        self.timesec = timesec
        self.continue_on_http_error = continue_on_http_error
        self.follow_redirects = follow_redirects
        self.threads = threads
        self._max_threads = 10
        self._thread_chars_query = {}
        self.lock = Lock()
        self.thread_warning = False
        self.max_threads_warning = False
        self._readtimout_counter = 0
        self._json_post_data = []
        self.request_counter = 1
        self.req_counter_injected = 0
        self.params_count = 0
        self.confirm_payloads = False
        self.safe_chars = None
        self.rto_warning = False
        self.fetch_using = None
        self.rtom_warning = False
        self.test_filter = None
        self.prioritize = False
        self._is_asked_for_priority = False
        self._bool_check_on_ct = True
        self._bool_ctb = None
        self._bool_ctt = None
        self._bool_ctf = None
        self._match_ratio_check = False
        self.fresh_queries = False

    @property
    def session_filepath(self):
        if self.filepaths:
            self._session_filepath = self.filepaths.session
        return self._session_filepath


conf = OdayConfigs()
