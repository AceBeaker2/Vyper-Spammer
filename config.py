# ==================================================
#               MAIL SERVER SETTINGS
# ==================================================

# The domain name that you own for the mail server
domain_name = 'yourdomain.com'

# Your private ip address on your network
ipv4_address = 'a.b.c.d'

# ==================================================
#               ABUSE SCRIPT SETTINGS
# ==================================================

# The name of the python process you want to use
pyname = 'python3'

# Whether to run more than one process(Only works on
# Linux/MacOS, disable on Windows)
parallel = False

# Amount of threads to run if parallel is enabled
processes = 15

# The actual referral link to abuse
ref_link = 'https://vy.tc/example'


# Ignore
if not parallel:
    processes=1
