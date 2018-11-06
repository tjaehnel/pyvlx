"""Unit tests for PyVLX Frames."""
import unittest
from pyvlx.frame_get_scene_list import FrameGetSceneListNotification
from pyvlx.frame_creation import frame_from_raw


class TestFrameGetSceneListNotification(unittest.TestCase):
    """Test class for PyVLX Frames."""

    # pylint: disable=too-many-public-methods,invalid-name

    def test_discover_node_request(self):
        """Test FrameGetSceneListNotification."""
        frame = FrameGetSceneListNotification()
        frame.scenes = [(0, 'All Windows Closed'), (1, 'Sleeping Wide Open'), (2, 'Bath Open')]
        frame.remaining_scenes = 3
        self.assertEqual(
            bytes(frame),
            b'\x00\xc8\x04\x0e\x03\x00All Window'
            + b's Closed\x00\x00\x00\x00\x00\x00\x00\x00'
            + b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
            + b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
            + b'\x00\x00\x00\x00\x00\x00\x01Sleeping '
            + b'Wide Open\x00\x00\x00\x00\x00\x00\x00'
            + b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
            + b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
            + b'\x00\x00\x00\x00\x00\x00\x00\x02Bath Ope'
            + b'n\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
            + b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
            + b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
            + b'\x00\x00\x00\x00\x00\x00\x00\x00\x03\xe2')

    def test_discover_node_request_from_raw(self):
        """Test parse FrameGetSceneListNotification from raw."""
        frame = frame_from_raw(
            b'\x00\xc8\x04\x0e\x03\x00All Window'
            + b's Closed\x00\x00\x00\x00\x00\x00\x00\x00'
            + b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
            + b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
            + b'\x00\x00\x00\x00\x00\x00\x01Sleeping '
            + b'Wide Open\x00\x00\x00\x00\x00\x00\x00'
            + b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
            + b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
            + b'\x00\x00\x00\x00\x00\x00\x00\x02Bath Ope'
            + b'n\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
            + b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
            + b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
            + b'\x00\x00\x00\x00\x00\x00\x00\x00\x03\xe2')
        self.assertTrue(isinstance(frame, FrameGetSceneListNotification))
        self.assertEqual(frame.scenes, [(0, 'All Windows Closed'), (1, 'Sleeping Wide Open'), (2, 'Bath Open')])
        self.assertEqual(frame.remaining_scenes, 3)
