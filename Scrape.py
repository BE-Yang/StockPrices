import urllib2, time, random, datetime
from bs4 import BeautifulSoup as bs
pages = [
		# 'https://web.tmxmoney.com/quote.php?qm_symbol=WMD',
		# 'https://web.tmxmoney.com/quote.php?qm_symbol=ACB',
		 # 'https://web.tmxmoney.com/quote.php?qm_symbol=APH',
		'https://web.tmxmoney.com/quote.php?qm_symbol=HMMJ',
		'https://web.tmxmoney.com/quote.php?qm_symbol=APH',
		'https://web.tmxmoney.com/quote.php?qm_symbol=FNSR:US',
		'https://web.tmxmoney.com/quote.php?qm_symbol=AMD:US',
		'https://web.tmxmoney.com/quote.php?qm_symbol=ADOM:US',
		]
proxyAddress= 'ID:PW@oproxy.global.com:8080'

proxy = urllib2.ProxyHandler({'http':proxyAddress,
							  'https':proxyAddress
							  })

opener = urllib2.build_opener(proxy)

urllib2.install_opener(opener)
for i in range(100):
	for page in pages:
		sock = urllib2.urlopen(page)
		extractPage = bs(sock.read(), 'html.parser')
		sock.close()
		priceContainer = extractPage.find('div', class_ = 'quote-price priceLarge')
		price = priceContainer.span.text
		print '%s: %s - %s' %(page.rsplit('=', 1)[1], price, datetime.datetime.today().strftime('%H:%M:%S'))
		randomtime = round(random.randrange(2, 5) + random.random(), 2)
		time.sleep(randomtime)

	print '%d left\n' %(99-i)
	randomtime = round(random.randrange(20, 30) + random.random(), 2)
	time.sleep(randomtime)































