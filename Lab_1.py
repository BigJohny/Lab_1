class component (object):
	def __init__(self):
		self.score = ''
		pass
		
class model (component):
	def __init__(self):
		self.model = ''
		pass

class instruction (object):
	def __init__(self):
		self.instruction = ''
		pass
		
class place (object):
	def __init__(self):
		self.place = ''
		pass
		
class fitter (object):
	def __init__(self):
		self.component = 'Enough'
		pass
		
	def go_to_place(self, place):
		self.place = '1'
		print('сборщик подощел к месту сборки')

	def explore_instruction(self, instruction):
		self.instruction = '1'
		print('сборщик прочел инструкцию')

	def assemble_model(self, model, component):
		self.model = '1'
		self.component = ' - component'
		print('сборщик собрал модель')

	def disassemble_model(self, model, component):
		self.model = '0'
		self.component = ' + component'
		print('сборщик разобрал модель')

	def get_out_from_place(self, place):
		self.place = '0'
		print('сборщик отошел от места сборки')
		
class constructor(object):
	def __init__(self):
		self.model = model()
		self.component = component()
		self.instruction = instruction()
		self.place = place()
		self.fitter = fitter()
		
	def run(self):
		self.fitter.go_to_place(self.place)
		self.fitter.explore_instruction(self.instruction)
		self.fitter.assemble_model(self.model, component)
		self.fitter.disassemble_model(self.model, component)
		self.fitter.get_out_from_place(self.place)

constructor = constructor()
constructor.run()
