import csv
from collections import Counter
from datetime import datetime as dt
from scrapy.exceptions import DropItem

from pep_parse.settings import BASE_DIR, RESULTS_DIR

TIME_FORMAT = '%Y-%m-%d_%H-%M-%S'
FILENAME = 'status_summary_{}.csv'


class PepParsePipeline:
    def __init__(self) -> None:
        self.results_dir = BASE_DIR / RESULTS_DIR
        self.results_dir.mkdir(exist_ok=True)
        self.total = Counter()

    def open_spider(self, spider):
        time = dt.now().strftime(TIME_FORMAT)
        file_path = self.results_dir / FILENAME.format(time)
        self.file = csv.writer(open(file_path, 'w'))
        self.file.writerow(['Статус', 'Количество'])

    def process_item(self, item, spider):
        self.total[item['status']] += 1
        if 'status' not in item:
            raise DropItem('Status не найден')
        return item

    def close_spider(self, spider):
        self.total['Total'] = sum(self.total.values())
        self.file.writerows(self.total.items())
