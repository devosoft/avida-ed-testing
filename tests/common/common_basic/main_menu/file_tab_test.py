import pytest

from tests.base_test import BaseTest


class FileTabTest(BaseTest):
    """
    Test class that tests the File tab of the main menu bar.
    """

    @pytest.mark.run()
    def test_export_graphics(self):
        """
        Tests that the "Export Graphics" option in the File tab works as
        expected.

        :return: None.
        """
        assert not self.bp.export_graphics_dialog_displayed()
        self.bp.export_graphics()
        assert self.bp.export_graphics_dialog_displayed()
        self.bp.close_export_graphics_dialog()
        assert not self.bp.export_graphics_dialog_displayed()

