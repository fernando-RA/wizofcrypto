from django.test import TestCase

from otc_twitter.models import GuruAccount, Ticker

class GurusTestCase(TestCase):
    def setUp(self):
        GuruAccount.objects.create(
            uid="", handle="mn_goat_trader", score="10.4k")
        GuruAccount.objects.create(
            uid="", handle="GeniusTrader777", score="14.9k")

    def test_models_being_saved(self):
        """GURUS ARE SAVED AND IDENTIFIED"""
        gurus = GuruAccount.objects.all()
        self.assertEqual(gurus[0].score, '10.4k')
        self.assertEqual(gurus[1].score, '14.9k')

    def tearDown(self):
        gurus = GuruAccount.objects.all()
        for guru in gurus:
            guru.delete()

        return super().tearDown()


class TickerTestCase(TestCase):
    def setUp(self):
        Ticker.objects.create(name="$CGAC", score="?")

    def test_models_being_saved(self):
        """GURUS ARE SAVED AND IDENTIFIED"""
        tickers = Ticker.objects.all()
        self.assertEqual(tickers[0].score, '?')

    def tearDown(self):
        tickers = GuruAccount.objects.all()
        for ticker in tickers:
            ticker.delete()

        return super().tearDown()
