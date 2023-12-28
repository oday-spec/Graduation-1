
import oday
from oday.common.colors import *
from oday.common.colors import colorize

# LEGAL_DISCLAIMER = "\n[!] Legal disclaimer: Usage of oday for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local,\nstate and federal laws. Developer assume no liability and is not responsible for any misuse or damage caused by this program."
# LEGAL_DISCLAIMER = colorize(string=LEGAL_DISCLAIMER, color="white", normal=True)
# I1 = colorize(string="'", color="yellow", normal=True, background="red")
# I1 = f"{I1}{BRIGHT}{yellow}"
# I2 = colorize(string='"', color="yellow", normal=True, background="red")
# I2 = f"{I2}{BRIGHT}{yellow}"
# I3 = colorize(string=")", color="yellow", normal=True, background="red")
# I3 = f"{I3}{BRIGHT}{yellow}"
# START_BRACES = colorize(string="{", color="bright_white", normal=True)
# END_BRACES = f'{colorize(string="}", color="bright_white", normal=True)}'
# END_BRACES = f"{END_BRACES}{BRIGHT}{yellow}"
# line = colorize(string="", color="green", bold=True)


banner = """


 ___  ___  _     _  _ _  _             _    _             ___                               
/ __>| . || |   | || \ |<_> ___  ___ _| |_ <_> ___ ._ _  / __> ___  ___ ._ _ ._ _  ___  _ _ 
\__ \| | || |_  | ||   || |/ ._>/ | ' | |  | |/ . \| ' | \__ \/ | '<_> || ' || ' |/ ._>| '_>
<___/`___\|___| |_||_\_|| |\___.\_|_. |_|  |_|\___/|_|_| <___/\_|_.<___||_|_||_|_|\___.|_|  
                       <__'                                                                 


""" 

BANNER = colorize(string=banner, color="blue", bold=True)
print(BANNER)
