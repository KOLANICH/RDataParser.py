from .r_data import *

try:
	import numpy
	arrayCtor=numpy.array
except ImportError:
	def arrayCtor(x, *args, **kwargs):
		return x

def processItemsVec(refTable, cts):
	res=[]
	for subEl in cts.vec:
		res.append(postprocess(refTable, subEl))
	return res

def processRawVec(refTable, cts):
	return arrayCtor(cts.vec)

class ListXP:
	__slots__=("car", "cdr", "tag")
	def __init__(self, tag, car, cdr):
		self.car=car
		self.cdr=cdr
		self.tag=tag

class postprocessors:
	def symsxp(refTable, cts):
		return cts.contents.vec
	
	def listsxp(refTable, cts):
		return ListXP(postprocess(refTable, cts.tag), postprocess(refTable, cts.car), postprocess(refTable, cts.cdr))
	
	vecsxp=processItemsVec
	strsxp=processItemsVec
	exprsxp=processItemsVec
	realsxp=processRawVec
	lglsxp=processRawVec
	intsxp=processRawVec
	
	def refsxp(refTable, cts):
		#assert refTable.contents.car.flags.type == Type.vecsxp
		return d.body.ref_table.contents.car.contents.vec[cts.index - 1]

	def charsxp(refTable, cts):
		return cts.vec
	
	def nilvalue_sxp(refTable, cts):
		return None
	
	def cplxsxpel(refTable, cts):
		return [num.r+num.i*1j for num in el.contents.vec]
	
	def envsxp(refTable, cts):
		

a=None
def postprocess(refTable, el):
	global a
	if hasattr(el, "contents"):
		contents = el.contents
	else:
		contents = None
	a=el
	return getattr(postprocessors, el.flags.type.name)(refTable, contents)


#def parseRData(file="./prothro.rda"):
def parseRData(file="./datasets/semiFail/weta.rda"):
	d=RData.from_file(file)
	return postprocess(d.body.ref_table, d.body.ref_table)