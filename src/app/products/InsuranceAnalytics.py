import pickle


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
		
	X_test[8] = float(input[5])
	X_test[9] = float(input[6])
	X_test[14] = float(input[8])

	loaded_model = pickle.load(open("finalized_model_regression_gb.sav", 'rb'))
	prediction_gb = loaded_model.predict([X_test])

	loaded_model = pickle.load(open("finalized_model_regression_svm.sav", 'rb'))
	prediction_svm = loaded_model.predict([X_test])

	
	return(prediction_gb, prediction_svm)
	
def run_model(model, alg_name, plot_index):
    # build the model on training data
    model.fit(X_train, y_train)

    # make predictions for test data
    y_pred = model.predict(X_test)
    # calculate the accuracy score
    accuracy =  accuracy_score(y_test, y_pred) * 100
    print(alg_name,",accuracy:",accuracy)	
	
def classification(input):

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
		
	X_test[8] = float(input[5])
	X_test[9] = float(input[6])
	X_test[14] = float(input[8])


	loaded_model = pickle.load(open("finalized_model_classificationDecisionTree.sav", 'rb'))
	dt_pred = loaded_model.predict([X_test])

	loaded_model = pickle.load(open("finalized_model_classificationNearestNeighborsClassifier.sav", 'rb'))
	knn_pred = loaded_model.predict([X_test])

	return(dt_pred,knn_pred)
	
print(analytics(['','','','M','','2010','24','yes','200','yes']))