import sys

def search_same(*a_list):
	same = []
	for a in a_list[0]:
		for b in a_list[1]:
			if a == b:
				same.append(a)
	return(same)

def search_dif(*a_list):
	dif = []
	for a in a_list[0]:
		if not a in a_list[1]:
				dif.append(a)
	return(dif)

def marketing():
	clients = ['andrew@gmail.com', 'jessica@gmail.com', 'ted@mosby.com', 'john@snow.is', 'bill_gates@live.com', 'mark@facebook.com', 'elon@paypal.com', 'jessica@gmail.com']
	participants = ['walter@heisenberg.com', 'vasily@mail.ru', 'pinkman@yo.org', 'jessica@gmail.com', 'elon@paypal.com', 'pinkman@yo.org', 'mr@robot.gov', 'eleven@yahoo.com']
	recipients = ['andrew@gmail.com', 'jessica@gmail.com', 'john@snow.is']
	# same = search_same(clients, participants)
	# print(same)
	dif = search_dif(clients, recipients)
	print(dif)



if __name__ == '__main__':
	marketing()