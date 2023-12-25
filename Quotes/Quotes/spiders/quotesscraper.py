import scrapy


class quotesscraperSpider(scrapy.Spider):
    name = "quotesscraper"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com/page/1/"]

    def parse(self, response):
        Quotes=response.css('div.quote')
        for Quote in Quotes:
            yield{
                'Text':Quote.css('span.text[itemprop="text"]::text').get(),
                'Author':Quote.css('small.author[itemprop="author"]::text').get(),
                'Tags':Quote.css('div.tags a::text').getall()
            }
        next_page=response.css('li.next a ::attr(href)').get()

        if next_page is not None:
            next_page_url='https://quotes.toscrape.com' + next_page
            yield response.follow(next_page_url,callback=self.parse)