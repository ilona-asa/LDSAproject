import os
import email.parser
import re
from email.parser import Parser
# from email.Utils import parseaddr
from email.Header import decode_header


# In[38]:

atom_rfc2822 = r"[a-zA-Z0-9_!#\$\%&'*+/=?\^`{}~|\-]+"
atom_posfix_restricted = r"[a-zA-Z0-9_#\$&'*+/=?\^`{}~|\-]+"  # without '!' and '%'
atom = atom_rfc2822
dot_atom = atom + r"(?:\." + atom + ")*"
quoted = r'"(?:\\[^\r\n]|[^\\"])*"'
local = "(?:" + dot_atom + "|" + quoted + ")"
domain_lit = r"\[(?:\\\S|[\x21-\x5a\x5e-\x7e])*\]"
domain = "(?:" + dot_atom + "|" + domain_lit + ")"
addr_spec = local + "\@" + domain

email_address_re = re.compile('^' + addr_spec + '$')


def getmailaddresses(msg, name):
    """retrieve From:, To: and Cc: addresses"""
    addrs = email.utils.getaddresses(msg.get_all(name, []))
    for i, (name, addr) in enumerate(addrs):
        if not name and addr:
            # only one string! Is it the address or is it the name ?
            # use the same for both and see later
            name = addr

        try:
            # address must be ascii only
            addr = addr.encode('ascii')
        except UnicodeError:
            addr = ''
        else:
            # address must match adress regex
            if not email_address_re.match(addr):
                addr = ''
        addrs[i] = (getmailheader(name), addr)
    return addrs


def getmailheader(header_text, default="ascii"):
    """Decode header_text if needed"""
    try:
        headers = decode_header(header_text)
    except email.Errors.HeaderParseError:
        # This already append in email.base64mime.decode()
        # instead return a sanitized ascii string
        return header_text.encode('ascii', 'replace').decode('ascii')
    else:
        for i, (text, charset) in enumerate(headers):
            try:
                headers[i] = unicode(text, charset or default, errors='replace')
            except LookupError:
                # if the charset is unknown, force default
                headers[i] = unicode(text, default, errors='replace')
        return u"".join(headers)


# read file into pandas using a relative path
# path = 'data/sms.tsv'
# path = 'data/0006.2003-12-18.GP.spam.txt'
parser = Parser()
rootdir = '/root/Desktop/Machine_Learning/Project-SpamDetection/'
# rootdir = '/root/Desktop/Machine_Learning/Project-SpamDetection/'
listtexts = []
for subdirs, dir, files in os.walk(rootdir):
    for file in files:
        path = os.path.join(subdirs, file)
        if '.idea' in path:
            continue
        elif 'py' in path:
            continue
        else:
            f = open(path, 'r').read()
            msg = email.message_from_string(f)

            subject = getmailheader(msg.get('Subject', ''))
            # print(subject)
            from_ = getmailaddresses(msg, 'from')
            from_ = ('', '') if not from_ else from_[0]
            print(from_)
            if msg.is_multipart():
                for payload in msg.get_payload():
                    Text = str(payload.get_payload())
                    Text = re.sub(r'[^\x00-\x7F]+',' ', Text)
            else:
                Text = str(msg.get_payload())
                Text = re.sub(r'[^\x00-\x7F]+', ' ', Text)

            cleanbr = re.compile('<br>|<BR>')
            cleanr = re.compile('<.*?>')
            # cleannline = re.compile('\n')
            Text = re.sub('\s+', ' ', Text)
            # Text = Text.translate("  ", '\t\n ')
            Text = re.sub(cleanbr, ' ', Text)
            Text = re.sub(cleanr, '', Text)

        listtexts.append(Text)
