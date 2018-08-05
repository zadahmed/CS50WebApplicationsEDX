import requests


def main():
	res = requests.get("https://api.fixer.io/latest?base=USD&symbols=GBP")

	base = input("First Currency: ")
	other = input("Second Currency:")
	res1 = requests.get("https://api.fixer.io/latest",params = {"base": base , "symbols" :other})
	if res.status_code != 200:
		raise Exception("Error with API")
	data = res.json()
	rate = data["rates"]["GBP"]
	print(data)
	print(f"1 USD is equal to  {rate} GBP")
	print(f"1 {base} is equal to  {rate} {other}")


if __name__ == '__main__':
	main()