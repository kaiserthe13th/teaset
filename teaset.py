import sys, os, json, re

__version__ = "0.0.1"

def _enter(name):
	try:
		with open(name+"\\pack.json") as f:
			fr = f.read()
	except OSError as e:
		print(e)
		exit()
	j = json.loads(fr)
	n = j['name']
	while True:
		sys.stdout.write(f'{os.getcwd()} ({n}) > ')
		c = input("")
		if c == 'exit': break
		elif re.match(r'cd *', c): os.chdir(c[3:].strip())
		else: os.system(c)

def _clnpath(path):
	s = path.split('/')
	if os.name in ('nt'): s = path.split('\\')
	return s[-1]

def _create(name, desc = ""):
	nname = _clnpath( name )
	if not os.path.exists( name+'\\src' ): os.makedirs(name+'\\src')
	if not os.path.exists( name+'\\out' ): os.makedirs(name+'\\out')
	with open(name+'\\pack.json', 'w+') as pakinfo:
		w = f'\
\
	"name": "{nname}",\
\n	"version": "0.0.1",\
\n	"teaset_ver": "{__version__}",\
\n	"te_ver": "0.0.1",\
\n	"dependencies": [],\
\n	"desc": "{desc}"\
\n'
		w = "{\n" + w + "}"
		pakinfo.write(w)
	with open(name+'\\src\\main.py', 'w+') as mpy:
		mpy.write('import TerrarialEngine as te\n')

def main(argv):
	if argv[1] == 'create': _create(argv[2], " ".join(argv[3:]))
	if argv[1] == 'enter': _enter(argv[2])

if __name__ == "__main__":
	try:
		main(sys.argv)
	except IndexError:
		print ( '\nnot enough args given\n' )