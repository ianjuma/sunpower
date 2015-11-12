import urllib
import urllib2
import json

from django.conf import settings


class CrunchGatewayException(Exception):
    pass


class CrunchGateway:

    def __init__(self):
        self.CrunchInterface = settings.CRUNCH_INTERFACE

    def get_product_stats(self, product_id, start_date, end_date,
                          granularity='day', metric='count', category='sent'):

        values = {
            'productId': product_id,
            'metric': metric,
            'granularity': granularity,
            'startDate': start_date,
            'endDate': end_date
        }

        headers = {
            'Accept': 'application/json',
            'apikey': settings.API_KEY
        }

        try:
            url = '%s%s/%s?%s' % (self.CrunchInterface,
                                   'pinless-airtime',
                                   category,
                                   urllib.urlencode(values))
            print 'Sending request to ' + url
            request = urllib2.Request(url=url, headers=headers)
            response = urllib2.urlopen(request)
            the_page = response.read()

        except urllib2.HTTPError as e:
            the_page = e.read()
            raise CrunchGatewayException(the_page)

        else:
            decoded = json.loads(the_page)
            dates = []
            agents = []
            for datum in decoded['responses']['agentCostStats']:
                dates.append(datum['date'])
                agents.append(datum['elements'])

            print agents
            print dates
            return decoded['responses']['agentCostStats']

    def get_agent_stats(self, category, agent_id, start_date,
                        end_date, granularity='day', metric='cost'):

        values = {
            'agentId': agent_id,
            'metric': metric,
            'granularity': granularity,
            'startDate': start_date,
            'endDate': end_date
        }

        headers = {
            'Accept': 'application/json',
            'apikey': settings.API_KEY
        }
        stats = []

        try:
            url = '%s%s/%s?%s' % (self.CrunchInterface,
                                   'pinless-airtime',
                                   category,
                                   urllib.urlencode(values))
            print 'Sending request to ' + url
            request = urllib2.Request(url=url, headers=headers)
            response = urllib2.urlopen(request)
            the_page = response.read()

        except urllib2.HTTPError as e:
            the_page = e.read()
            raise CrunchGatewayException(the_page)
        else:
            decoded = json.loads(the_page)
            for data in decoded['responses']['productStats']:
                stats.append(data)

            return stats