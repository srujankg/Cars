# Cars
Vehicle evaluation 

# Program description
A discovery in the common law jurisdictions allows opposition parties to obtain evidence through each other's parties or third parties. This program "Cars," provides aid to file discoveries through evaluation of locating property and its value over time. He program depreciates the value of the properties by using the straight line of the depreciation method. The Accelrated  method depreciates the value of an asset over the cost of its useful life. To successfully do this method, you must have three pivotal information the assets initial cost, salvage value, and estimated lifespan of the asset. 

## Data Source
the program extracts information from the website "Public Data," which is a website that allows people to seek public records from local, state, and federal agencies.This program contacts the "Public Data" server which allows the program to get a new ID token every day because the id to login varies every day. Logging into this program is similar to logging into public data you use the same username and password. This program is straightforward to use the application as person name, and the specified property is needed to be typed in, for the results to unveil. When looking into the property details such as the model, what year the car was bought, Registration date, and VIN will show up.

## Data Format
XML is a markup language that stores and transports data by encoding documents so that humans and machines could understand. Many people get confused with HTML and XML but both have 2 differant primary goals as HTML is mainly to display data while XML is to transport data and to define the data. XML is heavily used in this program as it was used to translate the extracted infrormation from "Public Data" to the program.  The XML is extracted when you loggin into the server of "public data" and it converts the response from "public data" from byte to string which allows the data to store the XML in a cache file.

This is an Example of an XML file with data
![image](https://user-images.githubusercontent.com/52220186/62242764-7d038500-b3a1-11e9-833d-435361f82329.png)
This example of XML data contain VIN, the registartion date,model,year nought, and the name the car is on.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<pddata type="search" sitetype="xml">
   <pdheaders />
   <pdfooters />
   <notes />
   <searchdata type="ADVANCED" asiname="NAME" title="Texas - Department of Motor Vehicles [Owners]" dbcount="1" reccount="55303681" db="txdmv" ed="147">
      <userinput searchstring="AVA DALEY">
         <p1>JANE DOE</p1>
         <matchany>ALL</matchany>
      </userinput>
      <searchgroup>TXDMV</searchgroup>
      <dispfields />
      <searchpages curpage="1" ismore="false">
         <page pagenum="1" searchmoreid="0" />
      </searchpages>
   </searchdata>
   <user>
      <dlnumber>XXXXXX933</dlnumber>
      <dlstate>UID</dlstate>
      <id>D5285FA51A708AEC7B2412FB34BBA264</id>
      <identifier />
      <sessionid />
      <tacdmv>DPPATX-01</tacdmv>
   </user>
   <servers>
      <searchserver>lbsearch.publicdata.com</searchserver>
      <loginserver>login.publicdata.com</loginserver>
      <mainserver>www.publicdata.com</mainserver>
   </servers>
   <lookups>
      <charged>1</charged>
      <available>666</available>
   </lookups>
   <results numrecords="3" ismore="false">
      <record rec="30897148077" db="txdmv" ed="147">
         <disp_fld1>TEXAS A&amp;M TRANSPORTATION INSTITUTE</disp_fld1>
         <disp_fld2>Year/Make/Model: 2011 KIA MOTOR CORPORATION KIA MOTOR CORPORATION RIO</disp_fld2>
         <disp_fld3>Current License Plate:</disp_fld3>
         <disp_fld4>Previous License Plate:</disp_fld4>
         <source>Texas - Department of Motor Vehicles [Owners]</source>
      </record>
      <record rec="5020669233" db="txdmv" ed="147">
         <disp_fld1>JANE DOE</disp_fld1>
         <disp_fld2>Year/Make/Model: 2012 HYUNDAI HYUNDAI SONATA</disp_fld2>
         <disp_fld3>Current License Plate: XXXX846</disp_fld3>
         <disp_fld4>Previous License Plate: XXXX846</disp_fld4>
         <source>Texas - Department of Motor Vehicles [Owners]</source>
      </record>
      <record rec="5196261872" db="txdmv" ed="147">
         <disp_fld1>JANE BAMBI DOE</disp_fld1>
         <disp_fld2>Year/Make/Model: 2017 HYUNDAI HYUNSAN</disp_fld2>
         <disp_fld3>Current License Plate: XXXX531</disp_fld3>
         <disp_fld4>Previous License Plate:</disp_fld4>
         <source>Texas - Department of Motor Vehicles [Owners]</source>
      </record>
   </results>
</pddata>
```

## Data Cost
Charge per query ($0.026 to $0.05 depedning on vlume) 

## Cost Mitigation
Cache files are a file of data located on a local hard drive on a computer, witha goal of speeding up processes. And can only be opened as a text document which in the programs case is the XML file.  Cache files are known for keeping data that will be revisted again. In the programs case the XML data is stored in Cache files because the data that public data gives as the search results could be stored through public data which is very vital for the program to do. So if cache file is found you dont need to search up the propert or persons name because its already stored in the program for the day. But if a file not to be seen you must contact the public data servers again by logging in once again.

## Diagram
![image](https://user-images.githubusercontent.com/52220186/62165692-9eeb0200-b2e4-11e9-8920-a0a122e61357.png)

   # Advanatages
Discoveries are usually costly and are very time-consuming. However, this program lessens the stress caused by these inquiries. As this program allows making discoveries with benefits such as efficiency, less time consuming, and gain better insight. Once you login through the program with a simple search of the persons' name and specific property you are trying to inspect, the properties registered to the name you search would be showcased through the program which is very efficient and less time-consuming. Moreover, you could gain more insight into other properties the party holds on their name that no one has further knowledge about an individual property which could help around the case. You also gain information on the estimated values of the property over time.
