import freecurrencyapi
client = freecurrencyapi.Client('fca_live_q3f19H5W4sNXKQKanPQG16G5LGV3Hiv5z7QJiOKa')

# result = client.latest()

result = {
   "data":{
      "AUD":1.5411702677,
      "BGN":1.7828601961,
      "BRL":4.9626605413,
      "CAD":1.3458801487,
      "CHF":0.8780001068,
      "CNY":7.2573908022,
      "CZK":22.0372124758,
      "DKK":6.8310109818,
      "EUR":0.9165901128,
      "GBP":0.7883601082,
      "HKD":7.8183514827,
      "HRK":7.0424210702,
      "HUF":351.6899240132,
      "IDR":15293.470138326,
      "ILS":3.7501304499,
      "INR":83.144795678,
      "ISK":132.0690798785,
      "JPY":145.4113457532,
      "KRW":1333.304586854,
      "MXN":17.0521527184,
      "MYR":4.6157007022,
      "NOK":10.474911679,
      "NZD":1.673770203,
      "PHP":56.644889649,
      "PLN":4.0778006949,
      "RON":4.529400702,
      "RUB":95.9903962843,
      "SEK":10.7963311111,
      "SGD":1.3554901375,
      "THB":35.2024154183,
      "TRY":27.0453750663,
      "USD":1,
      "ZAR":19.0749325839
   }
}
print(result["data"])
for x in result["data"]:

  print(result["data"][x])
 