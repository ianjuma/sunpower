import urllib
import urllib2
import json

from django.conf import settings


class SleuthGatewayException(Exception):
    pass


class SleuthGateway:

    def __init__(self):
        self.SleuthInterface = settings.SLEUTH_INTERFACE

    def top_up_user(self, user_id, amount, source, ref_id, user_category='Agent', currency_code='KES'):
        values = {
            'agentId': user_id,
            'userCategory': user_category,
            'currencyCode': currency_code,
            'source': source,
            'refId': ref_id,
            'amount': amount
        }

        headers = {'Accept': 'application/json', 'apikey': settings.SLEUTH_API_KEY}

        try:
            url = '{}billing/add-transaction'.format(self.SleuthInterface)
            print url
            data = urllib.urlencode(values)
            request = urllib2.Request(url, data, headers=headers)
            response = urllib2.urlopen(request)
            the_page = response.read()

        except urllib2.HTTPError as e:
            the_page = e.read()
            raise SleuthGatewayException(the_page)

        else:
            decoded = json.loads(the_page)
            if decoded['status']:
                return decoded['status']
            else:
                raise SleuthGatewayException(decoded['errorMessage'])

    def get_user_balance(self, user_id, user_category='Agent'):
        values = {
            'userId': user_id,
            'userCategory': user_category
        }

        headers = {'Accept': 'application/json'}

        try:
            url = '%s/billing/user-balance' % self.SleuthInterface
            data = urllib.urlencode(values)
            request = urllib2.Request(url, data, headers=headers)
            response = urllib2.urlopen(request)
            the_page = response.read()

        except urllib2.HTTPError as e:
            the_page = e.read()
            raise SleuthGatewayException(the_page)

        decoded = json.loads(the_page)

        if decoded['status']:
            return {
                'currencyCode': decoded['currencyCode'],
                'amount': decoded['amount']
            }
        else:
            raise SleuthGatewayException('Error while fetching balance')
