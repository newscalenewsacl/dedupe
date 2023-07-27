import json

from flask import Flask, jsonify, request
from pymongo import MongoClient
from bson import json_util


app = Flask(__name__)

myclient = MongoClient(
    "mongodb+srv://mysteriouscoder:mysteriouscoder@cluster0.agkearu.mongodb.net/?retryWrites=true&w=majority")
db = myclient["DUDP"]
Collection = db["Repo"]

def parse_json(data):
    return json.loads(json_util.dumps(data))

# Filtering the Quantities greater

@app.route('/search', methods=['GET', 'POST'])
def search():
    firstname = ""
    lastname = ""
    email = ""
    cntno = ""

    if (request.method == 'GET'):
        args = request.args
        city = args.get('city')
        cmts = args.get('cmts')

        if city != None and cmts != None:

            first = args.get('firstname')
            middlename = args.get('middlename')
            last = args.get('lastname')
            state = args.get('state')
            area = args.get('area')
            location = args.get('location')
            street = args.get('street')
            building = args.get('building')
            flatno = args.get('flatno')
            pincode = args.get('pincode')
            emails = args.get('email')
            allcontact = args.get('allcontact')

            parameters = {

                "CITY": city,
                "CMTS": cmts,
                "FIRST_NAME": first,
                "MIDDLE_NAME": middlename,
                "LAST_NAME": last,
                "EMAIL": emails,
                "STATE": state,
                "AREA": area,
                "LOCATION": location,
                "STREET": street,
                "BUILDING": building,
                "FLAT_NO": flatno,
                "PINCODE": pincode,
                "HOME_PHONE": allcontact,
                "CONTACT_NO": allcontact,
                "MOBILE_NO": allcontact,
                "WORK_PHONE": allcontact
            }

            query = {}

            for param, value in parameters.items():
                if value:
                    query[param] = value

            #if first != None:
            #    firstname = {'$regex': first, '$options': 'i'}

            #else:
            #    ns = "None"
            #    firstname = None if ns == 'None' else ns

            #if last != None:
            #    lastname = {'$regex': last, '$options': 'i'}
            #else:
            #    ns = "None"
            #    lastname = None if ns == 'None' else ns

            #if emails != None:
            #    email = {'$regex': emails, '$options': 'i'}
            #else:
            #    ns = "None"
            #    email = None if ns == 'None' else ns

            #if allcontact != None:
            #    cntno = {'$regex': allcontact, '$options': 'i'}
            #else:
            #    ns = "None"
            #    cntno = None if ns == 'None' else ns

            #cursor = Collection.find({'$and': [{'$and': [{"CITY": city}, {"CMTS": cmts}]}, {'$or': [{"FIRST_NAME": firstname}, {"LAST_NAME": lastname}, {"EMAIL": email},
            #                                  {"HOME_PHONE": cntno}, {"CONTACT_NO": cntno},
            #                                  {"MOBILE_NO": cntno}, {"WORK_PHONE": cntno}]}]})
            cursor = Collection.find(query)
            #cursor = Collection.find({'$or': [{"FIRST_NAME": firstname}, {"LAST_NAME": lastname}, {"EMAIL": email},
            #                                  {"HOME_PHONE": cntno}, {"CONTACT_NO": cntno},
            #                              {"MOBILE_NO": cntno}, {"WORK_PHONE": cntno}]})

            #return jsonify(cursor)

            First_Name = []
            Last_Name = []
            Emailss = []
            States = []
            Areas = []
            Locations = []
            Streets = []
            Buildings = []
            flatnos = []
            pincodes = []
            Home_phone = []
            Contact_No = []
            Mobile_No = []
            Work_Phone = []
            cmtss = []


            First_Namejson = []
            Last_Namejson = []
            Emailssjson = []
            Statesjson = []
            Areasjson = []
            Locationsjson = []
            Streetsjson = []
            Buildingsjson = []
            flatnosjson = []
            pincodesjson = []
            Home_phonejson = []
            Contact_Nojson = []
            Mobile_Nojson = []
            Work_Phonejson = []
            cmtssjson = []

            worth = len(list(cursor.clone()))
            print(worth)
            for record in cursor:
                print(record)

                getfirstname = record['FIRST_NAME']
                First_Name.append(getfirstname)

                if first != None:
                    First_Namejson.append(record)

                getlastname = record['LAST_NAME']
                Last_Name.append(getlastname)

                if last != None:
                    Last_Namejson.append(record)

                getemail = record['EMAIL']
                Emailss.append(getemail)

                if emails != None:
                    Emailssjson.append(record)

                gethomephone = record['HOME_PHONE']
                if gethomephone != "":
                    Home_phone.append(gethomephone)

                if allcontact != None:
                    Home_phonejson.append(record)

                getcontactno = record['CONTACT_NO']
                if getcontactno != "":
                    Contact_No.append(getcontactno)

                if allcontact != None:
                    Contact_Nojson.append(record)

                getmobileno = record['MOBILE_NO']
                if getmobileno != "":
                    Mobile_No.append(getmobileno)

                if allcontact != None:
                    Mobile_Nojson.append(record)

                getworkphone = record['WORK_PHONE']
                if getworkphone != "":
                    Work_Phone.append(getworkphone)

                if allcontact != None:
                    Work_Phonejson.append(record)

                getstate = record['STATE']
                if getstate != "":
                    States.append(getstate)

                if state != None:
                    Statesjson.append(record)

                getarea = record['AREA']
                if getarea != "":
                    Areas.append(getarea)

                if area != None:
                    Areasjson.append(record)

                getlocations = record['LOCATION']
                if getlocations != "":
                    Locations.append(getlocations)

                if location != None:
                    Locationsjson.append(record)

                getstreet = record['STREET']
                if getstreet != "":
                    Streets.append(getstreet)

                if street != None:
                    Streetsjson.append(record)

                getbuilding = record['BUILDING']
                if getbuilding != "":
                    Buildings.append(getbuilding)

                if building != None:
                    Buildingsjson.append(record)

                getflatno = record['FLAT_NO']
                if getflatno != "":
                    flatnos.append(getflatno)

                if flatno != None:
                    flatnosjson.append(record)

                getpincode = record['PINCODE']
                if getpincode != "":
                    pincodes.append(getpincode)

                if pincode != None:
                    pincodesjson.append(record)

                cmts = record['CMTS']
                if cmts != "":
                    cmtss.append(cmts)

            my_dict1 = {i: First_Name.count(i) for i in First_Name}
            print(my_dict1)
            my_dict2 = {i: Last_Name.count(i) for i in Last_Name}
            print(my_dict2)
            my_dict3 = {i: Emailss.count(i) for i in Emailss}
            print(my_dict3)
            my_dict4 = {i: Home_phone.count(i) for i in Home_phone}
            print(my_dict4)
            my_dict5 = {i: Contact_No.count(i) for i in Contact_No}
            print(my_dict5)
            my_dict6 = {i: Mobile_No.count(i) for i in Mobile_No}
            print(my_dict6)
            my_dict7 = {i: Work_Phone.count(i) for i in Work_Phone}
            print(my_dict7)
            my_dict8 = {i: States.count(i) for i in States}
            print(my_dict8)
            my_dict9 = {i: Areas.count(i) for i in Areas}
            print(my_dict9)
            my_dict10 = {i: Locations.count(i) for i in Locations}
            print(my_dict10)
            my_dict11 = {i: Streets.count(i) for i in Streets}
            print(my_dict11)
            my_dict12 = {i: Buildings.count(i) for i in Buildings}
            print(my_dict12)
            my_dict13 = {i: flatnos.count(i) for i in flatnos}
            print(my_dict13)
            my_dict14 = {i: pincodes.count(i) for i in pincodes}
            print(my_dict14)


            #my_dict8 = {i: cmtss.count(i) for i in cmtss}
            #print(my_dict8)

            if  first != None:
                try:
                    firstcount = my_dict1[first]
                    firstpercentage = firstcount / worth * 100
                    finalcount = str(firstcount) + " | " + str(firstpercentage) + "%"
                except:
                    finalcount = 0
            else:
                finalcount = 0

            if cmts != None:
                try:
                    cmtscount = my_dict1[cmts]
                    cmtspercentage = cmtscount / worth * 100
                    cmtscount = str(cmtscount) + " | " + str(cmtspercentage) + "%"
                except:
                    cmtscount = 0
            else:
                cmtscount = 0

            if last != None:
                try:
                    lastcount = my_dict2[last]
                    lastpercentage = lastcount / worth * 100
                    lastcount = str(lastcount) + " | " + str(lastpercentage) + "%"

                except:
                    lastcount = 0
            else:
                lastcount = 0

            if emails != None:
                try:
                    emailcount = my_dict3[emails]
                    emailpercentage = emailcount / worth * 100
                    emailcount = str(emailcount) + " | " + str(emailpercentage) + "%"

                except:
                    emailcount = 0
            else:
                emailcount = 0

            if allcontact != None:
                try:
                    homenocount = my_dict4[allcontact]
                    homephonepercentage = homenocount / worth * 100
                    homenocount = str(homenocount) + " | " + str(homephonepercentage) + "%"

                except:
                    homenocount = 0
            else:
                homenocount = 0

            if allcontact != None:
                try:
                    contactnocount = my_dict5[allcontact]
                    contactnopercentage = contactnocount / worth * 100
                    contactnocount = str(contactnocount) + " | " + str(contactnopercentage) + "%"

                except:
                    contactnocount = 0
            else:
                contactnocount = 0

            if allcontact != None:
                try:
                    mobilenocount = my_dict6[allcontact]
                    mobilenopercentage = mobilenocount / worth * 100
                    mobilenocount = str(mobilenocount) + " | " + str(mobilenopercentage) + "%"
                except:
                    mobilenocount = 0
            else:
                mobilenocount = 0

            if allcontact != None:
                try:
                    worknocount = my_dict7[allcontact]
                    worknopercentage = worknocount / worth * 100
                    worknocount = str(worknocount) + " | " + str(worknopercentage) + "%"

                except:
                    worknocount = 0
            else:
                worknocount = 0

            if state != None:
                try:
                    statecount = my_dict8[state]
                    statepercentage = statecount / worth * 100
                    statecount = str(statecount) + " | " + str(statepercentage) + "%"

                except:
                    statecount = 0
            else:
                statecount = 0


            if area != None:
                try:
                    areacount = my_dict9[area]
                    areapercentage = areacount / worth * 100
                    areacount = str(areacount) + " | " + str(areapercentage) + "%"

                except:
                    areacount = 0
            else:
                areacount = 0


            if location != None:
                try:
                    locationcount = my_dict10[location]
                    locationpercentage = locationcount / worth * 100
                    locationcount = str(locationcount) + " | " + str(locationpercentage) + "%"

                except:
                    locationcount = 0
            else:
                locationcount = 0


            if street != None:
                try:
                    streetcount = my_dict11[street]
                    streetpercentage = streetcount / worth * 100
                    streetcount = str(streetcount) + " | " + str(streetpercentage) + "%"

                except:
                    streetcount = 0
            else:
                streetcount = 0

            if building != None:
                try:
                    buildingcount = my_dict12[building]
                    buildingpercentage = buildingcount / worth * 100
                    buildingcount = str(buildingcount) + " | " + str(buildingpercentage) + "%"

                except:
                    buildingcount = 0
            else:
                buildingcount = 0

            if flatno != None:
                try:
                    flatnocount = my_dict13[flatno]
                    flatnopercentage = flatnocount / worth * 100
                    flatnocount = str(flatnocount) + " | " + str(flatnopercentage) + "%"

                except:
                    flatnocount = 0
            else:
                flatnocount = 0

            if pincode != None:
                try:
                    pincodecount = my_dict14[pincode]
                    pincodepercentage = pincodecount / worth * 100
                    pincodecount = str(pincodecount) + " | " + str(pincodepercentage) + "%"

                except:
                    pincodecount = 0
            else:
                pincodecount = 0






            return jsonify([{"First_Name_Match": finalcount, "FirstName": parse_json(First_Namejson)},
                            {"Last_Name_Match": lastcount, "LastName": parse_json(Last_Namejson)},
                            {"EmailID_Match": emailcount, "Emails": parse_json(Emailssjson)},
                            {"State_Match": statecount, "States": parse_json(Statesjson)},
                            {"Area_Match": areacount, "Area": parse_json(Areasjson)},
                            {"Location_Match": locationcount, "Location": parse_json(Locationsjson)},
                            {"Street_Match": streetcount, "Street": parse_json(Streetsjson)},
                            {"Building_Match": buildingcount, "Building": parse_json(Buildingsjson)},
                            {"Flatno_Match": flatnocount, "Flat": parse_json(flatnosjson)},
                            {"Pincodes_Match": pincodecount, "Pincode": parse_json(pincodesjson)},
                            {"HOME_PHONE_Match": homenocount, "HomePhone": parse_json(Home_phonejson)},
                            {"CONTACT_NO_Match": contactnocount, "ContactNo": parse_json(Contact_Nojson)},
                            {"MOBILE_NO_Match": mobilenocount, "MobileNo": parse_json(Mobile_Nojson)},
                            {"WORK_PHONE_Match": worknocount, "Workphone": parse_json(Work_Phonejson)},
                            {"Total Records Found": worth}])
        else:
            if city == None:
                return jsonify("Please Provide City Name")
            elif cmts == None:
                return jsonify("Please Provide CMTS")


# driver function
if __name__ == '__main__':
    app.run()
