import re
import time

import urllib3
import workerpool
from bs4 import BeautifulSoup

http = urllib3.PoolManager()

class MyTask(workerpool.Job):
   def __init__(self, wep_page, q):
      self.wep_page = wep_page
      self.q = q

   def run(self):

       while True:
           print(self.wep_page['url'])
           try:
               start = time.time()
               r = http.request('GET', self.wep_page['url'])
               if r.status in (200, 401):
                   print('[{}]: '.format(self.wep_page['url']), "Alive!")
               elif r.status == 404:
                   print('[{}]: '.format(self.wep_page['url']), "URL not found!")

               soup = BeautifulSoup(r.data, "html.parser")

               matches = re.findall(self.wep_page['content'], str(soup));

               if len(matches) == 0:
                   print('Target content NOT found in  %s' % (self.wep_page['url']))
                   cont = 'not found'
               else:
                   print('Target content found in %s' % (self.wep_page['url']))
                   cont = 'found'

           except:
               print('[{}]: '.format(self.wep_page['url']), 'No Connection to URL')
           roundtrip = time.time() - start
           self.q.put('URL is %s, status is %s, content is %s, response time is %s' % (self.wep_page['url'], r.status, cont, roundtrip))

           print(roundtrip)




           time.sleep(int(self.wep_page['period']))
