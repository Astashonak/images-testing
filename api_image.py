import requests
import unittest

BASE_URL =  "https://picsum.photos"
class testlyric(unittest.TestCase):
	def test_correct_check(self):
		a = requests.get(BASE_URL+"/400/600?image=50")
		assert(a.status_code == 200)
		print(a.status_code)

	def test_correct_changesize_check(self):
		b = requests.get(BASE_URL+"/200/300?image=50")
		assert(b.status_code == 200)
		print(b.status_code)

	def test_nocorrect_nonpicture_check(self):
		c = requests.get(BASE_URL+"/200/300?image=1085")
		assert(c.status_code == 404)
		print(c.status_code)


if __name__ == '__main__':
	unittest.main()
