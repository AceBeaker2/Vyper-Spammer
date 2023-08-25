# ==================================================
#               MAIL SERVER SETTINGS
# ==================================================

# The domain name that you own for the mail server
domain_name = 'quackertonai.com'

# Your private ip address on your network
ipv4_address = '10.0.0.12'

# ==================================================
#               ABUSE SCRIPT SETTINGS
# ==================================================

# The name of the python process you want to use
pyname = 'python3.9'

# fakes number
fakes = 1000


# Whether to run more than one process(Only works on
# Linux/MacOS, disable and run manually on Windows)
parallel = True

# Amount of threads to run if parallel is enabled
processes = 25

# The actual referral link to abuse
ref_link = 'https://vy.tc/qZZGK74'
#contid = '444977'
#refid = '20372236'

# Ignore
if not parallel:
    processes=1
import infoscript
contid, refid = infoscript.getinfo(ref_link)
