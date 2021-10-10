from icrawler.builtin import BingImageCrawler

positives = [
    'motorcycles', 'suvs', 'sedans', 'coupe cars', 'pickup trucks', 'buses', 'convertable cars', 'hypercars', 'supercars', 'sports cars', 'classic cars', 'hatchbacks cars']

negatives = ['trees', 'roads', 'Humans',
             'buildings', 'chairs', 'faces', 'grass', 'food']

max_positives = 100
max_negatives = 200

for c in positives:
    bing_crawler = BingImageCrawler(
        storage={'root_dir': f'data/positives/{c.replace(" ","")}'})
    bing_crawler.crawl(keyword=c, filters=None, max_num=max_positives, offset=0)

for c in negatives:
    bing_crawler = BingImageCrawler(
        storage={'root_dir': f'data/negatives/{c.replace(" ","")}'})
    bing_crawler.crawl(keyword=c, filters=None, max_num=max_negatives, offset=0)
