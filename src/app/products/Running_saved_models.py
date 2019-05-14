import pickle

locState ={0: 'AZ',
	 1: 'CA',
	 2: 'WA',
	 3: 'ME',
	 4: 'FL',
	 5: 'WV',
	 6: 'NJ',
	 7: 'AK',
	 8: 'MS',
	 9: 'NH',
	 10: 'NE',
	 11: 'NV',
	 12: 'PA',
	 13: 'DE',
	 14: 'IA',
	 15: 'MD',
	 16: 'ND',
	 17: 'MA',
	 18: 'MI',
	 19: 'IL',
	 20: 'OH',
	 21: 'MO',
	 22: 'OK',
	 23: 'CT',
	 24: 'IN',
	 25: 'UT',
	 26: 'KY',
	 27: 'LA',
	 28: 'NM',
	 29: 'MT',
	 30: 'NY',
	 31: 'TX',
	 32: 'KS',
	 33: 'WI',
	 34: 'WY',
	 35: 'MN',
	 36: 'BC',
	 37: 'TN',
	 38: 'OR',
	 39: 'GA',
	 40: 'SC',
	 41: 'RI',
	 42: 'CO',
	 43: 'VA',
	 44: 'VI',
	 45: 'HI',
	 46: 'VT',
	 47: 'NC',
	 48: 'DC',
	 49: 'ID',
	 50: 'AL',
	 51: 'SD',
	 52: 'AR'}

lstate = {0: 'OR', 1: 'KY', 2: 'CT', 3: 'KS', 4: 'DE', 5: 'OH', 6: 'SC', 7: 'MN', 8: 'CO', 9: 'DC', 10: '  ', 11: 'VT', 12: 'MD', 13: 'LA', 14: 'GA', 15: 'AR', 16: 'TX',
 17: 'NH', 18: 'WV', 19: 'VA', 20: 'ID', 21: 'MA', 22: 'TN', 23: 'NY', 24: 'WA', 25: 'CA', 26: 'MO',
 27: 'NC', 28: 'WY', 29: 'PA', 30: 'MS', 31: 'NM', 32: 'WI', 33: 'OK', 34: 'IL', 35: 'AZ', 36: 'UT', 37: 'IA', 38: 'NJ', 39: 'NV', 40: 'NE', 41: 'RI', 42: 'FL', 43: 'MI', 44: 'IN'}

gender  = {0: 'M', 1: ' ', 2: 'U', 3: 'F'}

def calc_mae(actual,pred):
    l = len(actual)
    #print(len(a),len(b))
    mae = 0
    count = 0
    for i in range(l):
        if(pred[i]!=0):
            diff = abs(actual[i] - pred[i])
            #square = diff * diff
            mae = mae + diff
            count += 1
    return(mae/l)

def analytics(input):

	gb,svm = regression( input)
	dt, knn = classification( input)
	
	input.append(int(round(svm[0])))
	input.append(int(round(gb[0])))
	input.append(dt[0])
	input.append(knn[0])
	
	return(input)

def regression(input):

	X_test = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
	
	if(input[3].lower() == 'm'):
		X_test[2] = 2
	elif(input[3].lower() == 'f'):
		X_test[2] = 1
	else:
		X_test[2] = 0
		
	if(input[7].lower() == 'yes'):
		X_test[10] = 1
	else:
		X_test[10] = 0
		
	if(input[9].lower() == 'yes'):
		X_test[15] = 1
	else:
		X_test[15] = 0	
		
	X_test[3] = get_key(input[4],locState)
	# X_test[5] = get_key(input[3],lstate)
	X_test[2] = get_key(input[3],gender)
	X_test[8] = float(input[5])
	X_test[9] = float(input[6])
	X_test[14] = float(input[8])

	loaded_model = pickle.load(open("finalized_model_regression_gb.sav", 'rb'))
	prediction_gb = loaded_model.predict([X_test])

	loaded_model = pickle.load(open("finalized_model_regression_svm.sav", 'rb'))
	prediction_svm = loaded_model.predict([X_test])

	
	return(prediction_gb, prediction_svm)

def get_key(val,my_dict): 
    for key, value in my_dict.items(): 
         if val == value: 
             return key 
  
    return 0

def run_model(model, alg_name, plot_index):
    # build the model on training data
    model.fit(X_train, y_train)

    # make predictions for test data
    y_pred = model.predict(X_test)
    # calculate the accuracy score
    accuracy =  accuracy_score(y_test, y_pred) * 100
    print(alg_name,",accuracy:",accuracy)	
	
	 

def classification(input):
# STATUS	ANATOMY	CGENDER	LOCSTATE	DIVNUM	LSTATE	DTAXID	DSTATE	VEHYEAR	DRIVERAGE	EMPLSTATUS	NCCI_NOI	NCCI_SOI	NCCI_SEV	WEEKLYWAGE	MARITAL	RECOVERIES	DaysToIssue
	X_test = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0, 0,0,0]
	
	if(input[3].lower() == 'm'):
		X_test[2] = 2
	elif(input[3].lower() == 'f'):
		X_test[2] = 1
	else:
		X_test[2] = 0
		
	if(input[7].lower() == 'yes'):
		X_test[10] = 1
	else:
		X_test[10] = 0
		
	if(input[9].lower() == 'yes'):
		X_test[15] = 1
	else:
		X_test[15] = 0	
	X_test[3] = get_key(input[4],locState)
	# X_test[5] = get_key(input[3],lstate)
	X_test[2] = get_key(input[3],gender)
	X_test[8] = float(input[5])
	X_test[9] = float(input[6])
	X_test[14] = float(input[8])


	
	loaded_model = pickle.load(open("finalized_model_classificationDecisionTree.sav", 'rb'))
	dt_pred = loaded_model.predict([X_test])

	loaded_model = pickle.load(open("finalized_model_classificationNearestNeighborsClassifier.sav", 'rb'))
	knn_pred = loaded_model.predict([X_test])

	return(dt_pred,knn_pred)
	
print(analytics(['','','','F','CA','1997','86','no','1000','no']))
