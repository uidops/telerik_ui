# Telerik UI for ASP.NET AJAX DialogHandler Dialog cracker and site vulnerability checker with reverse ip lookup

![Language](http://img.shields.io/:language-PYTHON-red.svg?style=flat-square) ![License](http://img.shields.io/:license-GPL-blue.svg?style=flat-square) ![CVE](http://img.shields.io/:CVE-2017_9248-blue.svg?style=flat-square)


NIST:       https://nvd.nist.gov/vuln/detail/CVE-2017-9248 <br />
Exploit-db: https://www.exploit-db.com/exploits/43873 <br />
Telerik:    https://www.telerik.com/support/kb/aspnet-ajax/details/cryptographic-weakness <br />
Tenable:    https://www.tenable.com/cve/CVE-2017-9248 <br />
Github:     https://github.com/bao7uo/dp_crypto <br />


Dependencies:
```
python3
```

Python3 libraries:
```
requests
```


Usage of checker:
```
python3 checker.py i http://site.com
python3 checker.py f sites.txt
```

Usage of exploit:
```
python3 exploit.py -k http://a.com/Telerik.Web.UI.DialogHandler.aspx 48 hex 9
python3 exploit.py -k http://a.com/Telerik.Web.UI.DialogHandler.aspx 48 all 12
```
