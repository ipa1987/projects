import requests

class ScanHeaders:

	def __init__(self, url):
		self.url = url
		response = requests.get(self.url)
		self.headers = response.headers

	def scan_xxss(self):
		"""config failure if X-XSS-Protection header is not present"""
		try:
			if self.headers["X-XSS-Protection"]:
				print("[+]", "X-XSS-Protection", ':', "pass")
		except KeyError:
			print("[-]", "X-XSS-Protection header not present", ':', "fail!")

	def scan_nosniff(self):
		"""X-Content-Type-Options should be set to 'nosniff' """
		try:
			if self.headers["X-Content-Type-Options"].lower() == "nosniff":
				print("[+]", "X-Content-Type-Options", ':', "pass")
			else:
				print("[-]", "X-Content-Type-Options header not set correctly", ':', "fail!")
		except KeyError:
			print("[-]", "X-Content-Type-Options header not present", ':', "fail!")			

	def scan_xframe(self):
		"""X-Frame-Options should be set to DENY or SAMEORIGIN"""
		try:
			if "deny" in self.headers["X-Frame-Options"].lower():
				print("[+]", "X-Frame-Options", ':', "pass")
			elif "sameorigin" in self.headers["X-Frame-Options"].lower():
				print("[+]", "X-Frame-Options", ':', "pass")
			else:
				print("[-]", "X-Frame-Options header not set correctly", ':', "fail!")
		except KeyError:
			print("[-]", "X-Frame-Options header not present", ':', "fail!")

	def scan_hsts(self):
		"""config failure if HSTS header is not present"""
		try:
			if self.headers["Strict-Transport-Security"]:
				print("[+]", "Strict-Transport-Security", ':', "pass")
		except KeyError:
			print("[-]", "Strict-Transport-Security header not present", ':', "fail!")

	def scan_policy(self):
		"""config failure if Security Policy header is not present"""
		try:
			if self.headers["Content-Security-Policy"]:
				print("[+]", "Content-Security-Policy", ':', "pass")
		except KeyError:
			print("[-]", "Content-Security-Policy header not present", ':', "fail!")

if __name__ == "__main__":

	target = ScanHeaders("https://api.github.com")

	for key in target.headers:
		print(key, ":", target.headers[key])

	print()

	target.scan_xxss()
	target.scan_nosniff()
	target.scan_xframe()
	target.scan_hsts()
	target.scan_policy()


