# https://tools.tracemyip.org/search--ip/list
import re

# ip주소 1~3자리 숫자가 특수기호.을 기준으로 4번 반복된다.
ip_string = \
"""72.188.50.15	SPECTRUM.COM	United States	Florida	Clermont
37.59.121.162	IP-37-59-121.EU	France	- - -	- - -
2003:fa:2f04:676f:d1d1:6927:b245:3749	T-IPCONNECT.DE	Germany	Baden-Wurttemberg	Elzach
93.121.128.169	MEDIASERV.NET	Guadeloupe	- - -	Basse-Terre
37.59.121.54	IP-37-59-121.EU	France	- - -	- - -
37.59.121.244	IP-37-59-121.EU	France	- - -	- - -
37.59.121.86	IP-37-59-121.EU	France	- - -	- - -
37.59.121.216	IP-37-59-121.EU	France"""

re.findall( 
'[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}',
ip_string)