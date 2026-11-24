import unittest
import json
import tempfile
from pathlib import Path

from app.main import check_valid_ip, load_config


class TestIPValidation(unittest.TestCase):

    def test_valid_ip(self):
        self.assertTrue(check_valid_ip("8.8.8.8"))

    def test_invalid_ip(self):
        self.assertFalse(check_valid_ip("8.8.h.8"))
    def test_valid_ipv6(self):
        self.assertTrue(check_valid_ip("2001:db8::1"))
    def test_invalid_ipv6(self):
        self.assertFalse(check_valid_ip("2001:db8:::1"))


class TestConfig(unittest.TestCase):

    def test_valid_config(self):
        with tempfile.TemporaryDirectory() as folder:
            config_path = Path(folder) / "config.json"

            config = {
                "devices_file": "devices.txt",
                "interval": 30,
                "log_file": "test.log"
            }

            with open(config_path, "w") as file:
                json.dump(config, file)

            result = load_config(config_path)
            self.assertEqual(result["interval"],30)
    def test_invalid_interval(self):
        with tempfile.TemporaryDirectory() as folder:
            config_path = Path(folder) / "config.json"

            config = {
                "devices_file": "devices.txt",
                "interval": -30,
                "log_file": "test.log"
            }
            with open(config_path, "w") as file:
                json.dump(config, file)

            with self.assertRaises(ValueError):
                load_config(config_path)
    def test_zero_interval(self):
        with tempfile.TemporaryDirectory() as folder:
            config_path = Path(folder) / "config.json"

            config = {
                "devices_file": "devices.txt",
                "interval": 0,

                "log_file": "test.log"
            }
            with open(config_path, "w") as file:
                json.dump(config, file)

            with self.assertRaises(ValueError):
                load_config(config_path)
    def test_bool_interval(self):
        with tempfile.TemporaryDirectory() as folder:
            config_path = Path(folder) / "config.json"

            config = {
                "devices_file": "devices.txt",
                "interval": True,
                
                "log_file": "test.log"
            }
            with open(config_path, "w") as file:
                json.dump(config, file)

            with self.assertRaises(ValueError):
                load_config(config_path)
    def test_string_interval(self):
        with tempfile.TemporaryDirectory() as folder:
            config_path = Path(folder) / "config.json"

            config = {
                "devices_file": "devices.txt",
                "interval": "30",
                
                "log_file": "test.log"
            }
            with open(config_path, "w") as file:
                json.dump(config, file)

            with self.assertRaises(ValueError):
                load_config(config_path)
    def test_missing_file(self):
        with tempfile.TemporaryDirectory() as folder:
            config_path = Path(folder) / "config.json"
            with self.assertRaises(FileNotFoundError):
                load_config(config_path)
    def test_malformed_json(self):
        with tempfile.TemporaryDirectory() as folder:
            config_path = Path(folder) / "config.json"

            with open(config_path, "w") as file:
                file.write("{ ceci n'est pas du JSON valide ")   # texte cassé exprès

            with self.assertRaises(json.JSONDecodeError):
                load_config(config_path)
    def test_missing_keys(self):
        with tempfile.TemporaryDirectory() as folder:
            config_path = Path(folder) / "config.json"

            config = {
                "interval": 30
            }
            with open(config_path, "w") as file:
                json.dump(config, file)

            result = load_config(config_path)

            self.assertNotIn("devices_file", result)