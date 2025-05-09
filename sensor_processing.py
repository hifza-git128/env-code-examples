#calculator_average:
def calculator_average(data):
   return sum(data)/len(data)

values = [72, 55, 101, 90]
average = calculator_average(values)

#stations list and display code:
print("Averae pm2.5:", average)
stations = [["A1", 62], ["B5", 97], ["C3", 155]]

#status_report:
for station in stations:
   print(f"{stations[0]} → {station[1]}")
  def report_status(stations, threshold):
   for station in stations:
     name, pm25 = station
     status = "OK" if pm25 < threshold else "High"
     print(f"{name}: {pm25} → {status}")

report_status(stations, 100)
