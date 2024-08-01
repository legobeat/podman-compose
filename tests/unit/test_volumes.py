# SPDX-License-Identifier: GPL-2.0
# pylint: disable=redefined-outer-name
import unittest

from podman_compose import PodmanCompose, parse_short_mount


class ParseShortMountTests(unittest.TestCase):
    def test_multi_propagation(self):
        compose = PodmanCompose()
        compose.dirname = "/"
        self.assertEqual(
            parse_short_mount(compose, "/foo/bar:/baz:U,Z"),
            {
                "type": "bind",
                "source": "/foo/bar",
                "target": "/baz",
                "bind": {
                    "propagation": "U,Z",
                },
            },
        )
