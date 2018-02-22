import numpy as np
import matplotlib.pyplot as plt
from APMonitor import apm
import tkinter as tk
from tkinter.filedialog import asksaveasfilename,askopenfilename

#APMonitor Solver
class APMSolver(object):
	"""docstring for APMSolver"""
	def __init__(self, server='http://xps.apmonitor.com', app='default'):
		super(APMSolver, self).__init__()
		self.server = server
		self.app = app
	
	def ClearServer(self):
		'Clear the APM server dependencies for same app name'
		clear = apm.apm(self.server,self.app,'clear all')
		return clear

	def LoadAPM(self,read=False):
		'Open APM and Load to application'
		root = tk.Tk()
		root.withdraw()
		model = askopenfilename(title='Select APM File',filetypes=([('APMonitor Files','*.apm')]))
		self.LoadModel(model)
		#If read set to true then read the files
		if read == True:
			with open(model,'r') as file:
				print(file.read())
		return model

	def LoadModel(self,model):
		'Load APM Model to the server'
		try:
			model = str(model)
		except:
			print('Model Needs to defined as a string path variable')
		else:
			model = apm.apm_load(self.server,self.app,model)

	def SaveResult(self,result):
		file = asksaveasfilename(title='Save Results',defaultextension='.txt',filetypes=([('Text Files','*.txt'),('HTML','*.html'),('All Files','*.*')]))
		with open(file,'w') as f:
			f.write('Result :\n')
			f.write('-'*15 + '\n')
			for k,v in result.items():
				Line = '{} = {}\n'.format(k,v)
				f.write(Line)


	def Solve(self,web=False,verbose=False,save=False):
		self.LoadAPM(read=True)
		apm.apm(self.server,self.app,'solve')
		results = apm.apm_sol(self.server,self.app)
		#Open Web viewer when Execution Done
		if web == True:
			apm.apm_web_var(self.server,self.app)
		#Give extra explanation to the user
		if verbose == True:
			print(self.solve())
			print('-'*15)
			print('Results : ')
			print('-'*15)
			for k,v in results.items():
				print('{} = {}'.format(k,v))
		#Save File If save is True
		if save == True:
			self.SaveResult(results)
		return results

def tes():
	APMS = APMSolver(app='coba_dulu')
	APMS.ClearServer()
	APMS.Solve(save=True)


if __name__ == '__main__':
	tes()
