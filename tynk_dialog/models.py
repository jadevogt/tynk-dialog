"""
Model objects
"""


class TextBox:
	"""
	Styled textbox
	"""


class BlipNoise:
	"""
	Blip noise class
	"""
	def __init__(self, name: str) -> None:
		self.name = name
		return


class DialogFile:
	"""
	Dialog "file" class
	"""
	def __init__(self, title: str, content: list['DialogPage'] = None) -> None:
		self.title = title
		self.content = content or []
		return


class DialogPage:
	"""
	Dialog page class
	"""
	def __init__(self, text: str, speaker: str,
				 textbox: TextBox | None = None,
				 blip: BlipNoise | None = None,
				 skippable: bool = True) -> None:
		self.text = text
		self.speaker = speaker
		self.textbox = textbox
		self.blip = blip
		self.skippable = skippable
		return

