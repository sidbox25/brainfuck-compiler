from os import system
import os, sys
from math import *

def comove(result, x, num):
	dif = num - x
	for _ in range(abs(dif)):
		if dif < 0:
			result += '<'
		elif dif > 0:
			result += '>'	
	return (result, num)

def bestMultiply(n):
	n = int(n)

	facs = []
	currentbest = (0, 0)
	bestsum = 9999
	for i in range(-5, 6):
		for j in range(1, n + i + 1):
			if (n + i) % j == 0:
				facs.append((j, int((n + i) / j)))
				if j + (n + i) / j + abs(i) < bestsum:
					bestsum = j + (n + 1) / j + abs(i)
					currentbest = (j, int((n + i) / j))

	return currentbest

def compile(doprint):
	file = open('code.txt', 'r').read()
	varibales = {"iftemp": 0, "temp": 1} 
	nextvar = 2
	lines = file.split('\n')
	result = ''
	loops = []
	x = 0
	for line in lines:
		args = line.split(' ')
		for _ in range(10000):
			try:
				args.remove('')
			except Exception:
				pass
		if line == '' or line.startswith('//') or len(args) < 1:
			continue
		if args[0] == 'var':
			if len(args) != 2:
				print(' Error: Var accepts 2 arguments but ' + str(len(args)) + ' were taken')
				return
			if args[1] in varibales:
				print(' Error: Redeclaration of varibale: ' + args[1])
				return
			varibales[args[1]] = nextvar
			nextvar += 1
		elif args[0] == 'allocate':
			if len(args) != 2:
				print(' Error: Allocate accepts 2 arguments but ' + str(len(args)) + ' were taken')
				return
			nextvar += int(args[1])
		elif args[0] == 'copy':
			if len(args) != 3:
				print(' Error: Copy accepts 3 arguments but ' + str(len(args)) + ' were taken')
				return
			if not args[1] in varibales:
				print(' Error: ' + args[1] + ' was not declared')
				return
			if not args[2] in varibales:
				print(' Error: ' + args[2] + ' was not declared')
				return
			result, x = comove(result, x, varibales[args[1]])
			result += '['
			result, x = comove(result, x, varibales['temp'])
			result += '+'
			result, x = comove(result, x, varibales[args[2]])
			result += '+'
			result, x = comove(result, x, varibales[args[1]])
			result += '-]'
			result, x = comove(result, x, varibales['temp'])
			result += '['
			result, x = comove(result, x, varibales[args[1]])
			result += '+'
			result, x = comove(result, x, varibales['temp'])
			result += '-]'
		elif args[0] == 'multiply':
			if not len(args) in (3, 4):
				print(' Error: Multiply accepts 3 or 4 arguments but ' + str(len(args)) + ' were taken')
				return
			if not args[1] in varibales:
				print(' Error: ' + args[1] + ' was not declared')
				return
			if len(args) == 3:
				try:
					int(args[2])
				except ValueError:
					print(' Third argument in multiply must be int')
					return
				if not 'temp' in varibales:
					varibales['temp'] = nextvar
					nextvar += 1
				result, x = comove(result, x, varibales[args[1]])
				result += '['
				result, x = comove(result, x, varibales['temp'])
				result += '+'
				result, x = comove(result, x, varibales[args[1]])
				result += '-]'
				result, x = comove(result, x, varibales['temp'])
				result += '['
				result, x = comove(result, x, varibales[args[1]])
				for _ in range(int(args[2])):
					result += '+'
				result, x = comove(result, x, varibales['temp'])
				result += '-]'
			else:
				if not args[2] in varibales:
					print(' Error: ' + args[1] + ' was not declared')
					return
				try:
					int(args[3])
				except ValueError:
					print(' Fourth argument in multiply must be int')
					return
				result, x = comove(result, x, varibales[args[1]])
				result += '['
				result, x = comove(result, x, varibales[args[2]])
				for _ in range(int(args[3])):
					result += '+'
				result, x = comove(result, x, varibales[args[1]])
				result += '-]'
		elif args[0] == '#pause':
			if len(args) != 1:
				print(' Error: Pause accepts no arguments but ' + str(len(args)) + ' were taken')
				return
			result, x = comove(result, x, varibales['temp'])
			result += '[]-[]'
		elif args[0] == 'clear':
			if len(args) != 2:
				print(' Error: Clear accepts 2 arguments but ' + str(len(args)) + ' were taken')
				return
			if not args[1] in varibales:
				print(' Error: ' + args[1] + ' was not declared')
				return
			result, x = comove(result, x, varibales[args[1]])
			result += '[-]'
		elif args[0] == 'move':
			if len(args) != 3:
				print(' Error: Move accepts 3 arguments but ' + str(len(args)) + ' were taken')
				return
			if not args[1] in varibales:
				print(' Error: ' + args[1] + ' was not declared')
				return
			if not args[2] in varibales:
				print(' Error: ' + args[2] + ' was not declared')
				return
			result, x = comove(result, x, varibales[args[1]])
			result += '['
			result, x = comove(result, x, varibales[args[2]])
			result += '+'
			result, x = comove(result, x, varibales[args[1]])
			result += '-]'
		elif args[0] == '#while':
			if len(args) != 2:
				print(' Error: While accepts 2 arguments but ' + str(len(args)) + ' were taken')
				return
			if not args[1] in varibales:
				print(' Error: ' + args[1] + ' was not declared')
				return
			result, x = comove(result, x, varibales[args[1]])
			result += '['
			loops.append(varibales[args[1]])
		elif args[0] == '#endwhile':
			if len(args) != 1:
				print(' Error: Endwhile accepts no arguments but ' + str(len(args)) + ' were taken')
				return
			result, x = comove(result, x, loops[len(loops) - 1])
			del loops[len(loops) - 1]
			result += ']'
		elif args[0] == 'input':
			if not len(args) in (1, 2):
				print(' Error: Input accepts 2 or no arguments but ' + str(len(args)) + ' were taken')
				return
			if len(args) == 2:
				if not args[1] in varibales:
					print(' Error: ' + args[1] + ' was not declared')
					return
			if len(args) == 2:
				result, x = comove(result, x, varibales[args[1]])
				result += ','
			else:
				if not 'input' in varibales:
					varibales['input'] = nextvar
					nextvar += 1
				result, x = comove(result, x, varibales['input'])
				result += ','
		elif args[0] == 'print':
			if len(args) != 2:
				print(' Error: Print accepts 2 arguments but ' + str(len(args)) + ' were taken')
				return
			if not args[1] in varibales:
				print(' Error: ' + args[1] + ' was not declared')
				return
			result, x = comove(result, x, varibales[args[1]])
			result += '.'
		elif args[0] in ('#if', '#ifn'):
			if len(args) != 4:
				print(' Error: If accepts 4 arguments but ' + str(len(args)) + ' were taken')
				return
			if not args[1] in varibales:
				print(' Error: ' + args[1] + ' was not declared')
				return
			if not args[2] in ('var', 'num', 'letter'):
				print(' Error: Third argument in if must be "var" or "num"')
				return
			result, x = comove(result, x, varibales[args[1]])
			result += '['
			result, x = comove(result, x, varibales['temp'])
			result += '+'
			result, x = comove(result, x, varibales['iftemp'])
			result += '+'
			result, x = comove(result, x, varibales[args[1]])
			result += '-]'
			result, x = comove(result, x, varibales['temp'])
			result += '['
			result, x = comove(result, x, varibales[args[1]])
			result += '+'
			result, x = comove(result, x, varibales['temp'])
			result += '-]'
			if args[2] == 'var':
				result, x = comove(result, x, varibales[args[3]])
				result += '['
				result, x = comove(result, x, varibales['temp'])
				result += '+'
				result, x = comove(result, x, varibales['iftemp'])
				result += '-'
				result, x = comove(result, x, varibales[args[3]])
				result += '-]'
				result, x = comove(result, x, varibales['temp'])
				result += '['
				result, x = comove(result, x, varibales[args[3]])
				result += '+'
				result, x = comove(result, x, varibales['temp'])
				result += '-]'
			else:
				if args[2] == 'letter':
					args[3] = ord(args[3])
				fac = bestMultiply(args[3])
				result, x = comove(result, x, varibales['temp'])
				for _ in range(int(fac[0])):
					result += '+'
				result += '['
				result, x = comove(result, x, varibales['iftemp'])
				for _ in range(int(fac[1])):
					result += '-'
				result, x = comove(result, x, varibales['temp'])
				result += '-]'
				dif = int(args[3]) - int(fac[0]) * int(fac[1])
				for i in range(abs(int(dif))):
					if int(dif) > 0:
						result += '-'
					if int(dif) < 0:
						result += '+'
			if args[0] == '#if':
				result, x = comove(result, x, varibales['iftemp'])
				result += '['
				result, x = comove(result, x, varibales['temp'])
				result += '+'
				result, x = comove(result, x, varibales['iftemp'])
				result += '-]+'

				result, x = comove(result, x, varibales['temp'])
				result += '['
				result, x = comove(result, x, varibales['iftemp'])
				result += '-'
				result, x = comove(result, x, varibales['temp'])
				result += '[-]]'

			result, x = comove(result, x, varibales['iftemp'])
			result += '[[-]'
		elif args[0] == '#endif':
			result, x = comove(result, x, varibales['iftemp'])
			result += ']'
		elif args[0] == '#else':
			result, x = comove(result, x, varibales['temp'])
			result += '-'
			result, x = comove(result, x, varibales['iftemp'])
			result += ']'
			result, x = comove(result, x, varibales['temp'])
			result += '+[-'
		elif args[0] == '#endelse':
			result, x = comove(result, x, varibales['temp'])
			result += ']'
		elif args[0] == 'add' or args[0] == 'addletter':
			if len(args) != 3:
				print(' Error: Add accepts 3 arguments but ' + str(len(args)) + ' were taken')
				return
			if not args[1] in varibales:
				print(' Error: ' + args[1] + ' was not declared')
				return
			if args[0] == 'add':
				try:
					int(args[2])
				except ValueError:
					print(' Third argument in add must be int')
					return
			else:
				if len(args[2]) != 1:
					print(' Third argument in addletter must have a length of 1')
					return
				args[2] = ord(args[2])
				
			result, x = comove(result, x, varibales[args[1]])
			fac = bestMultiply(abs(int(args[2])))
			if fac[0] + fac[1] + 5 > abs(int(args[2])):
				for i in range(abs(int(args[2]))):
					if int(args[2]) > 0:
						result += '+'
					if int(args[2]) < 0:
						result += '-'
			else:
				result, x = comove(result, x, varibales['temp'])
				for _ in range(int(fac[0])):
					result += '+'
				result += '['
				result, x = comove(result, x, varibales[args[1]])
				for _ in range(int(fac[1])):
					if int(args[2]) > 0:
						result += '+'
					if int(args[2]) < 0:
						result += '-'
				result, x = comove(result, x, varibales['temp'])
				result += '-]'
				mo = 1
				if int(args[2]) < 0:
					mo *= -1
				result, x = comove(result, x, varibales[args[1]])
				dif = int(args[2]) - int(fac[0]) * int(fac[1] * mo)
				for i in range(abs(int(dif))):
					if int(dif) > 0:
						result += '+'
					if int(dif) < 0:
						result += '-'
		elif args[0] == 'printletter':
			if len(args) != 2:
				print(' Error: Printletter accepts 2 arguments but ' + str(len(args)) + ' were taken')
				return
			if len(args[1]) != 1:
				print(' Second argument in printletter must have a length of 1')
			args[1] = ord(args[1])
			fac = bestMultiply(args[1])
			result, x = comove(result, x, varibales['temp'])
			for _ in range(int(fac[0])):
				result += '+'
			result += '['
			result, x = comove(result, x, varibales['iftemp'])
			for _ in range(int(fac[1])):
				result += '+'
			result, x = comove(result, x, varibales['temp'])
			result += '-]'
			dif = int(args[1]) - int(fac[0]) * int(fac[1])
			result, x = comove(result, x, varibales['iftemp'])
			for i in range(abs(int(dif))):
				if int(dif) > 0:
					result += '+'
				if int(dif) < 0:
					result += '-'
			result, x = comove(result, x, varibales['iftemp'])
			result += '.[-]'
		else:
			print(' Error: No command called ' + args[0])
			return

	lines = []
	for i in range(0, len(result), 30):
		lines.append(result[i:i+30])
	result = '\n'.join(lines)
	if doprint:
		print(result)
	with open('compiled.bf', 'w') as wf:
		wf.write(result)

def main():
	try:
		# Command Input
		while True:
			inp = input(' >>> ')
			if inp == 'edit':
				open('code.txt', 'a').close()
				system('"%windir%\\System32\\notepad.exe" .\\code.txt')
			elif inp == 'exit':
				print(' Exiting...')
				exit()
			elif inp == 'compile':
				compile(True)
			elif inp in ('cls', 'clear'):
				system('cls')
			elif inp == 'run':
				system('".\\brainfuck-interpreter.exe" compiled.bf')
				print('\n')
			elif inp == 'cr':
				compile(False)
				system('".\\brainfuck-interpreter.exe" compiled.bf')
				print('\n')
			elif inp == 'restart':
				system('python ' + __file__)
			elif inp.split(' ')[0] == 'bm' and len(inp.split(' ')) == 2:
				print(' ' + str(bestMultiply(inp.split(' ')[1])))
			else: 
				print(' Command not found!\n')
	except KeyboardInterrupt:
		print('\n Exiting...')

main()