#!/usr/bin/env python

if __name__ == "__main__":

    from utils.models import Country
    Country.objects.initialize()

    from utils.models import Currency
    Currency.objects.initialize()
