import csv
import urllib2
import json
import logging

from django.db import models
from django.conf import settings
from django.utils import timezone

logger = logging.getLogger(__name__)


class CountryManager(models.Manager):

    @staticmethod
    def initialize():
        filename = settings.COUNTRY_INFO_FILE

        logger.info('CountryManager::initialize filename=%s' % filename)

        indices = {}
        with open(filename, 'rbU') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if len(indices) == 0:
                    for i in range(len(row)):
                        indices[row[i]] = i
                else:
                    index = indices['Common Name']
                    name = row[index]
                    if len(name) == 0:
                        continue

                    index = indices['ITU-T Telephone Code']
                    telephoneCode = row[index]
                    if len(telephoneCode) == 0:
                        continue

                    pos = telephoneCode.find(' and ')
                    if pos > 0:
                        telephoneCode = telephoneCode[:pos]

                    index = indices['ISO 4217 Currency Code']
                    currencyCode = row[index][0:3]
                    if len(currencyCode) == 0:
                        continue

                    print "Adding %s,%s,%s" % (name, telephoneCode, currencyCode)

                    country = Country(name=name,
                                      telephone_code=telephoneCode,
                                      currency_code=currencyCode)
                    country.save()


class Country(models.Model):
    name = models.CharField(max_length=100, unique=True)
    telephone_code = models.CharField(max_length=10)
    currency_code = models.CharField(max_length=3)

    objects = CountryManager()

    def __unicode__(self):
        return self.name


class CurrencyManager(models.Manager):

    @staticmethod
    def initialize():

        logger.info('CurrencyManager::initialize')

        if settings.DEBUG:
            logger.info(
                'CurrencyManager::initialize NOT loading since we are in dev')
            currency = Currency(code='KES',
                                usd_conversion_rate=100.0,
                                updated=timezone.now())
            currency.save()
            currency = Currency(code='USD',
                                usd_conversion_rate=1.0,
                                updated=timezone.now())
            currency.save()
            return

        try:
            appId = '0208960ff71348379c12e1a7f8f2b1f1'
            url = "http://openexchangerates.org/api/latest.json?app_id=%s" % appId

            request = urllib2.Request(url)
            response = urllib2.urlopen(request)
            rawData = response.read()
            decoded = json.loads(rawData)

            rates = decoded['rates']

            for code, rate in rates.iteritems():
                currency = Currency(code=code,
                                    usd_conversion_rate=float(rate),
                                    updated=timezone.now())
                currency.save()

        except Exception, e:
            print "Caught exception [%s]" % e


class Currency(models.Model):
    code = models.CharField(max_length=3, unique=True)
    usd_conversion_rate = models.FloatField()
    updated = models.DateTimeField('Last Updated')

    objects = CurrencyManager()
