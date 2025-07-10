import unittest
from unittest.mock import MagicMock, patch
import sys

class TestMonoFont(unittest.TestCase):
    def setUp(self):
        self.patcher_tk = patch('tkinter.Tk', return_value=MagicMock(after=lambda *a, **k: None, mainloop=lambda: None))
        self.patcher_frame = patch('tkinter.Frame', return_value=MagicMock())
        self.patcher_label = patch('tkinter.Label', return_value=MagicMock())
        self.patcher_button = patch('tkinter.Button', return_value=MagicMock())
        self.mock_tk = self.patcher_tk.start()
        self.mock_frame = self.patcher_frame.start()
        self.mock_label = self.patcher_label.start()
        self.mock_button = self.patcher_button.start()

    def tearDown(self):
        self.patcher_tk.stop()
        self.patcher_frame.stop()
        self.patcher_label.stop()
        self.patcher_button.stop()
        if 'main' in sys.modules:
            del sys.modules['main']

    def test_mono_font_used_in_numeric_labels(self):
        import main
        fonts = []
        for call in self.mock_label.call_args_list:
            kwargs = call.kwargs
            text = kwargs.get('text', '')
            if 'Score:' in text or 'High Score' in text or 'Days' in text:
                fonts.append(kwargs.get('font'))
        self.assertTrue(fonts)
        for font in fonts:
            self.assertEqual(font[0], main.mono_font)

if __name__ == '__main__':
    unittest.main()
