from __future__ import annotations
from abc import ABC, abstractmethod

import hashlib


class Middleware(ABC):
	
	@abstractmethod
	def set_next(self, middleware: Middleware) -> Middleware:
		pass
	
	@abstractmethod
	def middleware(self, request: dict):
		pass


class AbstractMiddleware(Middleware):
	_next_middleware: Middleware = None
	
	def set_next(self, middleware: Middleware) -> Middleware:
		self._next_middleware = middleware
		
		return middleware
	
	@abstractmethod
	def middleware(self, request):
		if self._next_middleware:
			return self._next_middleware.middleware(request)
		
		return None


class EmailRequiredMiddleware(AbstractMiddleware):
	def middleware(self, request: dict):
		if 'email' in request and request['email'].strip():
			return super().middleware(request)
		else:
			return f'EmailRequiredMiddleware: Email is required'


class PasswordRequiredMiddleware(AbstractMiddleware):
	def middleware(self, request: dict):
		if 'password' in request and request['email'].strip():
			return super().middleware(request)
		else:
			return f'PasswordRequiredMiddleware: Password is required'


db_users = [
	{
		'email': 'admin@example.com',
		'password': '4813494d137e1631bba301d5acab6e7bb7aa74ce1185d456565ef51d737677b2',
		'role': 'admin'
	},
	{
		'email': 'user@example.com',
		'password': '65e84be33532fb784c48129675f9eff3a682b27168c0ea744b2cf58ee02337c5',
		'role': 'user'
	},
	{
		'email': 'guest@example.com',
		'password': '65e84be33532fb784c48129675f9eff3a682b27168c0ea744b2cf58ee02337c5',
		'role': 'guest'
	},
]


class UserExistsMiddleware(AbstractMiddleware):
	def middleware(self, request: dict):
		email = request['email']
		db_emails = [x['email'] for x in db_users if 'email' in x]
		if email in db_emails:
			return super().middleware(request)
		else:
			return f'UserExistsMiddleware: Email {email} does not exist in database'


class PasswordCheckMiddleware(AbstractMiddleware):
	def middleware(self, request: dict):
		password_str = request['password']
		email = request['email']
		db_passwords = [x['password'] for x in db_users if x['email'] in email]
		if hashlib.sha256(password_str.encode('utf-8')).hexdigest() in db_passwords:
			return super().middleware(request)
		else:
			return f"PasswordCheckMiddleware: The password '{password_str}' is incorrect"


class RoleCheckMiddleware(AbstractMiddleware):
	def middleware(self, request: dict):
		email = request['email']
		role = [x['role'] for x in db_users if x['email'] == email]
		role = role[0] if len(role) == 1 else None
		if role == 'admin':
			return f"RoleCheckMiddleware: Hello, Admin({email})!"
		elif role == 'user':
			return f"RoleCheckMiddleware: Hello, User({email})!"
		else:
			return 'RoleCheckMiddleware: 403 Forbidden'


def client_code(middleware: Middleware):
	requests = [
		{
			'title': '1. Lets try admin user',
			'email': 'admin@example.com',
			'password': 'root'
		},
		{
			'title': '2. Lets try simple user',
			'email': 'user@example.com',
			'password': 'qwerty'
		},
		{
			'title': '3. Lets try guest user:',
			'email': 'guest@example.com',
			'password': 'qwerty'
		},
		{
			'title': '4. Lets try wrong email user:',
			'email': 'wrong@example.com',
			'password': 'qwerty2'
		},
		{
			'title': '5. Lets try wrong password user:',
			'email': 'admin@example.com',
			'password': 'Root'
		},
		{
			'title': '6. Lets try empty email input:',
			'email': '',
			'password': 'Root'
		},
	]
	for request in requests:
		result = middleware.middleware(request)
		print(request['title'])
		if result:
			print(f'{result}')
		print('-' * 55, end='\n\n')


if __name__ == "__main__":
	pss = '4813494d137e1631bba301d5acab6e7bb7aa74ce1185d456565ef51d737677b2'
	
	email_required = EmailRequiredMiddleware()
	password_required = PasswordRequiredMiddleware()
	user_exists = UserExistsMiddleware()
	password_check = PasswordCheckMiddleware()
	role_check = RoleCheckMiddleware()
	
	email_required \
		.set_next(password_required) \
		.set_next(user_exists) \
		.set_next(password_check) \
		.set_next(role_check)
	
	print(end='\n')
	
	client_code(email_required)
