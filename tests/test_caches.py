'''
Created on Sep 12, 2013

@author: akittredge
'''


import unittest
from financial_fundamentals import sqlite_price_cache, accounting_metrics
from financial_fundamentals.caches import sqlite_fundamentals_cache
import pytz
from tests.infrastructure import turn_on_request_caching
import datetime
from financial_fundamentals.accounting_metrics import AccountingMetricGetter
import sqlite3
from financial_fundamentals.sqlite_drivers import SQLiteIntervalseries
from financial_fundamentals.time_series_cache import FinancialIntervalCache
from financial_fundamentals.edgar import HTMLEdgarDriver

QUARTERLY_EPS = accounting_metrics.EPS.quarterly()

class InitMethodTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        turn_on_request_caching()

    def test_sqlite_price_cache(self):
        cache = sqlite_price_cache(db_file_path=':memory:')
        prices = cache.get(symbol='GOOG',
                            dates=[datetime.datetime(2013, 8, 1, tzinfo=pytz.UTC),
                                   datetime.datetime(2013, 8, 28, tzinfo=pytz.UTC),
                                   datetime.datetime(2012, 8, 12, tzinfo=pytz.UTC)])
        date_prices = {date : value for date, value in prices}
        self.assertAlmostEqual(date_prices[datetime.datetime(2013, 8, 28, tzinfo=pytz.UTC)], 
                               848.55, delta=.1)
        
    def test_sqlite_fundamentals_cache(self):
        cache = sqlite_fundamentals_cache(metric=QUARTERLY_EPS, 
                                          db_file_path=':memory:')
        symbol = 'GOOG'
        dates = [datetime.datetime(2011, 12, 1, tzinfo=pytz.UTC),
                 datetime.datetime(2012, 12, 3, tzinfo=pytz.UTC), 
                 datetime.datetime(2012, 12, 4, tzinfo=pytz.UTC),
                 ]
        values = list(cache.get(symbol=symbol, dates=dates))
        self.assertEqual(values[1], 6.53)
        

class TestFundamentalsCache(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        turn_on_request_caching()
        
    def test_border_behavior(self):
        '''Fundamentals were being inserted twice because of an off by one error.'''
        metric = QUARTERLY_EPS
        symbol = 'CSCO'
        connection = sqlite3.connect(':memory:', detect_types=sqlite3.PARSE_DECLTYPES)
        driver = SQLiteIntervalseries(connection=connection,
                                     table='fundamentals',
                                     metric=metric.name)
        metric_getter = AccountingMetricGetter(metric=metric, 
                                           filing_getter=HTMLEdgarDriver)
        cache = FinancialIntervalCache(get_data=metric_getter.get_data, database=driver)
        dates = {datetime.datetime(2010, 2, 17)}
        list(cache.get(symbol, dates=dates))
        
        count_query = "SELECT COUNT(*)  AS count FROM fundamentals WHERE symbol = '{}'".format(symbol)
        count = connection.execute(count_query).next()['count']
        self.assertEqual(count, 1)
        list(cache.get(symbol, dates=dates))
        count = connection.execute(count_query).next()['count']
        self.assertEqual(count, 1)
        
class EndToEndTests(unittest.TestCase):
    def test_quarterly_eps_sqlite(self):
        turn_on_request_caching()
        start, end = (datetime.datetime(2013, 1, 1, tzinfo=pytz.UTC), 
                      datetime.datetime(2013, 1, 2, tzinfo=pytz.UTC))
        cache = sqlite_fundamentals_cache(metric=QUARTERLY_EPS, 
                                          db_file_path=':memory:')
        data = cache.load_from_cache(stocks=['GOOG', 'AAPL'],
                                     start=start, 
                                     end=end)
        self.assertEqual(data['GOOG'][0], 6.53)
    

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(EndToEndTests('test_quarterly_eps_sqlite'))
    unittest.TextTestRunner().run(suite)
    