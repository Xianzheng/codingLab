import suds


client = suds.client.Client("http://www.webservicex.net/currencyconvertor.asmx?WSDL")


result = client.service.ConversionRate(fromCurrency='USD', toCurrency='EUR')

print("Conversion rate: ", result)