from flask import Flask, render_template, request
app = Flask(__name__)
import InsuranceAnalytics
import Running_saved_models

@app.route('/')
def student():
   return render_template('latest.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      print(type(str(result)))
      print(str(result))
      result_str = str(result)
      l=[]
      res_array = []
      final_res=[]
      for i in result_str.split():
         l.append(i)
      k=1
      while(k<len(l)):
         res_array.append(l[k][1:])
         k=k+2
      for j in res_array:
         print(j)
         print(type(j))
         final_res.append(j[0:j.find("'")])
      #print(final_res)
      #modi = InsuranceAnalytics.analytics(final_res)
      modi = Running_saved_models.analytics(final_res)
      print(modi)
      text_file = open("C:/Users/320053936/Downloads/frontEnd-duplicate/src/assets/myFile.txt", "w")
      for item in modi:
         text_file.write("%s\n" % item)
      text_file.close()

      return render_template("result1.html",result = result)

if __name__ == '__main__':
   app.run(debug = True)
