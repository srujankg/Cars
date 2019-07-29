import requests
import argparse
import datetime
import os
import xml.etree.ElementTree as ET
# Get command line arguments
parser = argparse.ArgumentParser() # (decription="DMV Test Program")
parser.add_argument("--username", "-u", required=True, help="Username for logging in to PublicData service.")
parser.add_argument("--password", "-p", required=True, help="Password for logging in to PublicData service.")
parser.add_argument("--search", "-s", help="Terms to search for. Enclose in quotes if more than one word.")
args = parser.parse_args()
def get_cars(args:dict):
  # Save search results to this file
  cache_filename = "search-results-{}.xml".format(args.search.lower())

  # If the file already exists, read XML from our local file without asking PublicData
  if os.path.exists(cache_filename):
    tree = ET.parse(cache_filename)
    return tree

  # File does not exist..go ask PublicData
  url = "http://lbsearch.publicdata.com/pdsearch.php?disp=XML&p1={}&matchany=all&input=txdmv%7Cname&tacDMV=DPPATX-01&type=advanced&dlnumber={}&id={}&o=grp_dmv_tx_advanced_name" \
        .format(args.search, login_id, day_key)         
  result = requests.get(url)
  content = result.content.decode()
  print(content)
  # Save results for a future search of the same terms.
  open("search-results-{}.xml".format(args.search.lower()),"w").write(content)
  tree = ET.ElementTree(ET.fromstring(content))
  return tree

def get_car_details(rec:str, db:str, ed:str):
  # Save search results to this file
      cache_filename = "search-details-{}-{}-{}.xml".format(rec, db, ed)

  # If the file already exists, read XML from our local file without asking PublicData
      if os.path.exists(cache_filename):
            tree = ET.parse(cache_filename)
            return tree

  # File does not exist..go ask PublicData
      url = "http://lbsearch.publicdata.com/pddetails.php?disp=XML&db={}&rec={}&ed={}&dlnumber={}&tacdmv=DPPATX-01&id={}" \
            .format(db, rec, ed, login_id, day_key)

      # Request login from the server
      response = requests.get(url)                                        

      # Convert the response from stream of Bytes to string
      content = response.content.decode()

      # Save it to a file for use in our next search.           
      open(cache_filename, "w").write(content)

      # Convert the response to an XML tree instance.
      tree = ET.ElementTree(ET.fromstring(content))      
      return tree

def login(args:dict):
      # Filename for today's login
      today_yyymmdd = datetime.datetime.now().strftime("%Y%m%d")
      cache_filename = "{}-login.xml".format(today_yyymmdd)

      # If we already logged in once today, it will be in this XML file. Read it instead
      # of contacting the server.
      if os.path.exists(cache_filename):
            tree = ET.parse(cache_filename)
            return tree

      # If the file does not exist, we need to contact the PublicData server to start a new day.
      # Format Login URL
      url = "https://login.publicdata.com/pdmain.php/logon/checkAccess?disp=XML&login_id={}&password={}"
      url = url.format(args.username, args.password)

      # Request login from the server
      response = requests.get(url)                                        

      # Convert the response from stream of Bytes to string
      content = response.content.decode()

      # Save it to a file for use in our next search.           
      open(cache_filename, "w").write(content)

      # Convert the response to an XML tree instance.
      tree = ET.ElementTree(ET.fromstring(content))      
      return tree
     
def FixedRateDepreciationTable(salvage, cost, life):
      rate = 1 - ((salvage / cost) ** (1 / life))

      for year in range(1, life + 1):
            dv = cost * rate
            cost -= dv
            yield year, round(dv, 2), cost

###cars = root.findall("data/cars/iton")
###for car in cars:
"""
    {
import pandas as pd
get_cars, = pd.read_html("http://lbsearch.publicdata.com/pdsearch.php?db=txdmv|main&dlnumber={}}&id={}&tacdmv=DPPATX-01&p1={}", header=0, parse_dates=["Call Date"])
get_cars.to_csv("calls.csv", index=False)
###}    
"""
# Try to login
tree = login(args) 
# If successful, extract the daily ID PublicData assigns to us.
if not tree:
      print("Error logging in.")
      exit()
root = tree.getroot()
day_key = root.find("./user/id").text

# Login ID should be the same as the driver's license we typed in, but PublicData might
# transform it somehow so just use whatever version of it they sent back to use when we
# logged in.
login_id = root.find("./user/dlnumber").text

# If the user did not specify --search or -s, then we are done.
if not args.search:
      exit()

# Now try to get a list of motor vehicles
tree = get_cars(args)

# Go through list of cars and display them
root = tree.getroot()
cars = root.findall("./results/record")
for car in cars:
      rec = car.get("rec")
      db = car.get("db")
      ed = car.get("ed")
      print(car.find("disp_fld1").text)
      print("\tDetails at rec: {} db: {} ed: {}".format(rec, db, ed))
      detail_tree = get_car_details(rec, db, ed)
      car_root = detail_tree.getroot()
      details = car_root.findall("./dataset/dataitem/textdata/field")

      sales_date = None
      title_date = None
      reg_date = None
      model_year = None

      for detail in details:
            label = detail.get("label")
            if label.lower() == "vehicle sales price":
                  sales_price = float(detail.text)/100
            if label.lower() == "vehicle sold date":
                  sales_date = detail.text
            if label.lower() == "title date":
                  title_date = detail.get("formatteddate")
            if label.lower() == "registration effective":
                  reg_date = detail.get("formatteddate")
            if label.lower() == "model year":
                  model_year = detail.text
            if label.lower() == "vin number":
                 vin_number = detail.text
      print("\tTitle date",title_date,"sales date", sales_date, "Sales Price", sales_price, "Reg Date:", reg_date, "Model", model_year)
      print("Year\tDepreciation\tNew Value")

      if sales_price > 0:
            try:
                  model_year = int(model_year)
                  sales_year = int(sales_date[:4])
                  title_year = int(title_date[:4])
            except Exception as e:
                  print("Error converting year: {}".format(str(e)))
                  break

            if model_year == 0:
                  print("Cannot depreciate vehicle with no model year.")
                  break

            if sales_year == 0 and title_year == 0:
                  print("No title year, using model year")
                  life = 15
            else:
                  purchase_year = max([sales_year, title_year])
                  diff = purchase_year - model_year
                  if diff <= 1:
                        life = 15
                  else:
                        life = 15 - abs(diff)

            for year, depreciation, new_value in FixedRateDepreciationTable(1, sales_price, life):
                  print("{}\t{}\t{}".format(year, depreciation, new_value))
#if __name__ == '__main__':
      #print("year\t depreciation\t car Value ")
      #for year, depreciation, new_value in FixedRateDepreciationTable(1000, 100000, 10):
      #      print("{0:4}\t{1:>18}\t{2:26}".format(year, depreciation, new_value))
