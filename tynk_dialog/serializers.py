"""
Functions used to serialize / deserialize dialog files to / from JSON
"""
from json import JSONEncoder
from typing import TypedDict, Any
from tynk_dialog.models import DialogFile, DialogPage


class SanitizedDialogFile(TypedDict):
	"""
	DialogFile ready for serialization
	"""
	title: str
	contents: list[DialogPage]


class SanitizedDialogPage(TypedDict):
	"""
	DialogPage ready for serialization
	"""
	txt: str
	speaker: str
	# TODO: Ask about these two, might be numbers?
	textbox: Any
	blip: Any
	canSkip: bool


def sanitize_df(file: DialogFile) -> SanitizedDialogFile:
	"""
	Convert DialogFile object into a SanitizedDialogFile dict
	"""
	title = file.title
	contents = file.content
	return {'title': title, 'contents': contents}


def sanitize_dp(page: DialogPage) -> SanitizedDialogPage:
	"""
	Convert DialogPage object into a SanitizedDialogPage dict
	"""
	txt = page.text
	speaker = page.speaker
	textbox = page.textbox or -1
	blip = page.blip or -1
	can_skip = page.skippable
	return {'txt': txt, 'speaker': speaker, 'textbox': textbox,
			'blip': blip, 'canSkip': can_skip}


class DialogEncoder(JSONEncoder):
	"""
	Custom JSONEncoder to comply with whatever format GameMaker is using
	"""
	def default(self, o: DialogFile | DialogPage) -> SanitizedDialogFile | SanitizedDialogPage:
		match o:
			case DialogFile():
				return sanitize_df(o)
			case DialogPage():
				return sanitize_dp(o)
		return JSONEncoder.default(self, o)
	