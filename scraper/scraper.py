import re,urlparse
from selenium import webdriver
from bs4 import BeautifulSoup
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = 'https://l3com.taleo.net/careersection/l3_ext_us/jobsearch.ftl'


class TaleoJobScraper(object):

	def __init__(self):
		self.driver=webdriver.PhantomJS(service_args=['--ssl-protocol=any'])
		self.driver.set_window_size(2000,1500)
		#self.driver.maximise_window()
		#self.driver.implicitly_wait(10)
		
	def scrape(self):
		self.driver.window_handles
		jobs=self.scrape_job_links()
		for job in jobs:
			print job
		self.driver.quit()
	
	def scrape_job_links(self):
		
		self.driver.get(link)
		jobs=[]
		pageno=2
		while True:
			s=BeautifulSoup(self.driver.page_source,"html.parser")
			#print(s)
			r=re.compile(r'jobdetail\.ftl\?job=\d+$')

			for a in s.findAll('a',href=r):
				tr=a.findParent('tr')
				td=tr.findAll('td')

				job={}
				job['title']=a.text
				job['url']=urlparse.urljoin(link,a['href'])
				job['location']=td[2].text
				jobs.append(job)
	
			wait = WebDriverWait(self.driver, 10)
			search = wait.until(EC.presence_of_element_located((By.ID, "next")))
			search.send_keys("realpython")
			#self.driver.find_element_by_id("search_button_homepage").click()
			next_page_elem=self.driver.find_element_by_id("next")
			next_page_link=s.find('a',text='%d' % pageno)
			
			if next_page_link:
				next_page_elem.click()
				pageno=pageno+1
				sleep(0.75)
			else:
				break
		return jobs

if __name__=='__main__':
	scraper=TaleoJobScraper()
	scraper.scrape()


