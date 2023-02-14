import json


class JsonClass():
	def __init__(self):
		pass

	def json_read(self , name_file ):
		with open( name_file + '.json', "r" , encoding="utf8") as js_file:
			return json.load(js_file)

		pass

	def json_save( self , name_file , values ):
		with open( name_file + '.json', "w" , encoding="utf8") as js_file:
			json.dump( values , js_file , sort_keys = False, indent = 4)
		
		pass
