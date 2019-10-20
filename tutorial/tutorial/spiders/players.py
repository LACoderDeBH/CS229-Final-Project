import scrapy
from scrapy.crawler import CrawlerProcess

class PlayerStats(scrapy.Spider):
    name = "PlayerStats"
    start_urls = ['https://www.baseball-reference.com/players/b/bernato01.shtml', 'https://www.baseball-reference.com/players/m/mariomi01.shtml']
    def parse(self, response):
        table = response.xpath('//*[@class="row_summable sortable stats_table"]')
        return table
