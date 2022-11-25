#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import deque


def get_fibonacci_number(index):
	# if index==0:
	# 	return 0
	# else:
	# 	if index==1:
	# 		return 1
	# else:
	# 	return get_fibonacci_number(index-1)+get_fibonacci_number(index-2)


	return 0 if index==0 else 1 if index==1 else get_fibonacci_number(index-1)+get_fibonacci_number(index-2)

def get_fibonacci_sequence(length,seq=[0,1]):

	# if length==1:
	# 	return seq[0:1]
	# else:
	# 	if length==2:
	# 		return seq[0:2]
	# else:
	# 	if len(seq)<length:
	# 		return get_fibonacci_sequence(length,seq+[seq[-1]+seq[-2]])

	return (seq[0:1] if length==1 else seq[0:2] if length==2 else get_fibonacci_sequence(length,seq+[seq[-1]+seq[-2]]) if len(seq)<length)
def get_sorted_dict_by_decimals(dict_arg):
	return dict(sorted(dict_arg.items(),key=lambda t:t[1] % 1.0))

def fibonacci_numbers(length):
	initial_numbers=[0,1]
	yield initial_numbers[0]

	if length==2:
		yield initial_numbers[1]

	last_element=deque(initial_values)
	else:
		if length>len(initial_numbers):  #est ce que c'est correct de mettre cette ligne

		for i in range(len(initial_numbers),length):
			fibonacci_number=last_element[-1]+last_element[-2]
			last_element.append(fibonacci_number)
			last_element.popleft()
			yield fibonacci_number

def build_recursive_sequence_generator(initial_numbers,recursive_def,keep_whole_sequence=False):
	def recursive_generator(length):
		# On génère les valeurs initiales en premier (comme pour Fibonacci)
		for elem in initial_numbers[0:length]:
			yield elem
		# On crée une file sous forme de deque qui contient au départ les valeurs initiales
		last_elems = deque(initial_numbers)
		# Pour chaque valeur définie récursivement demandée :
		for i in range(len(initial_numbers), length):
			# On applique la définition récursive qui est la fonction passée en paramètre pour obtenir l'élément courant
			current_element = recursive_def(last_elems)
			# On ajoute à la file (entrée de la pile = fin de la deque)
			last_elems.append(current_element)
			# Si on ne veut pas garder toute la séquence, on enlève l'élément le plus vieux soit le premier element qui apparaît
			if not keep_whole_sequence:
				last_elems.popleft()
			# On génére l'élément courant
			yield current_element
	# On retourne la fermeture lexicale qui est un objet générateur.
	return recursive_generator


if __name__ == "__main__":
	print([get_fibonacci_number(0), get_fibonacci_number(1), get_fibonacci_number(2)])
	print([get_fibonacci_number(i) for i in range(10)])
	print()

	print(get_fibonacci_sequence(1))
	print(get_fibonacci_sequence(2))
	print(get_fibonacci_sequence(10))
	print()

	spam = {
		2: 2.1,
		3: 3.3,
		1: 1.4,
		4: 4.2
	}
	eggs = {
		"foo": 42.6942,
		"bar": 42.9000,
		"qux": 69.4269,
		"yeet": 420.1337
	}
	print(get_sorted_dict_by_decimals(spam))
	print(get_sorted_dict_by_decimals(eggs))
	print()

	for fibo_num in fibonacci_numbers(10):
		print(fibo_num, end=" ")
	print("\n")

	def fibo_def(last_elems):
		return last_elems[-1] + last_elems[-2]
	fibo = build_recursive_sequence_generator([0, 1], fibo_def)
	for fi in fibo(10):
		print(fi, end=" ")
	print("\n")

	lucas = build_recursive_sequence_generator([2,1],lambda seq:seq[-1]+seq[-2])
	print(f"Lucas : {[elem for elem in lucas(10)]}")
	perrin = build_recursive_sequence_generator([3,0,2],lambda seq:seq[-2]+seq[-3])
	print(f"Perrin : {[elem for elem in perrin(10)]}")
	hofstadter_q = build_recursive_sequence_generator([1,1], lambda seq: [seq[-seq[-1]]]+[seq[-seq[-2]]])
	print(f"Hofstadter-Q : {[elem for elem in hofstadter_q(10)]}")
