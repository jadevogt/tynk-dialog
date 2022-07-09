"""
Test suite for tynk dialog tool
"""
import json
from json import JSONDecodeError
from importlib import resources
from tynk_dialog import __version__
from tynk_dialog.models import DialogPage, DialogFile
from tynk_dialog.serializers import DialogEncoder


def test_version() -> None:
	"""
	Double check the version number
	"""
	assert __version__ == '0.1.0'

def test_file_parsing() -> None:
	"""
	Check the module's ability to read dialog files
	"""
	with resources.open_text("tests.data", "example_dialog.json", "utf8") as example_file:
		example_data = json.load(example_file)
	
def test_serializer() -> None:
	"""
	Check that dialog objects can be serialized to JSON
	"""
	page = DialogPage('text content', 'someone', None, None, False)
	file = DialogFile("test", [page])
	print(json.dumps(file, cls=DialogEncoder))
	try:
		print(json.dumps(ModuleNotFoundError, cls=DialogEncoder))
	except TypeError as e:
		assert "not JSON serializable" in e.__str__()	