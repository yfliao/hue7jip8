from django.core.management import call_command
from django.test.testcases import TestCase
from 臺灣言語服務.models import 訓練過渡格式


class 教典字詞抑是語句試驗(TestCase):

    @classmethod
    def setUpClass(cls):
        call_command('台語文語料庫蒐集及語料庫為本台語書面語音節詞頻統計')
        return super().setUpClass()

    def test數量(self):
        self.assertGreater(訓練過渡格式.資料數量(), 2000000)

    def testPOJ來源(self):
        self.assertTrue(
            訓練過渡格式.objects
            .filter('台語文語料庫蒐集及語料庫為本台語書面語音節詞頻統計-POJ')
            .exists()
        )

    def testHL來源(self):
        self.assertTrue(
            訓練過渡格式.objects
            .filter('台語文語料庫蒐集及語料庫為本台語書面語音節詞頻統計-HL')
            .exists()
        )
