from flask import Flask, render_template, request
import pandas as pd

app=Flask(__name__)

@app.route('/',methods=['GET','POST'])
def run_app():
    if request.method=='GET':
        return render_template('index.html')
    elif request.method=='POST':
        text = request.form['text']
        if '.com' in text:
            result="SAFE"
        elif '.net' in text:
            result="SAFE"
        elif '.org' in text:
            result="SAFE"
        else:
            result="MALICIOUS"
        return render_template('index.html',text=text,result=result)
    
@app.route('/Dash')
def run_dash():
    #plot 3 (plotting by types of attacks)

    url="https://raw.githubusercontent.com/MarcelinoCodes/CSP/main/malicious_phish.csv"

    df_phish=pd.read_csv(url)
    phishing=0
    defacement=0
    malware=0

    for i in df_phish['type']:
        if i=='phishing':
            phishing+=1
        elif i=='defacement':
            defacement+=1
        elif i=='malware':
            malware+=1
    all_malicious=(phishing+defacement+malware)/len(df_phish['type'])
    #(phishing+defacement+malware)/len(df_phish['type']) Over a 3rd of all websites are malicious
    L=len(df_phish['type'])
    data={'All Websites':1,'All Malicious Websites':all_malicious,'phishing':phishing/L,'defacement':defacement/L,'malware':malware/L}
    return render_template('Dash.html',data=data)

@app.route('/Team')
def run_team():
    return render_template('Team.html')

@app.route('/Learn')
def run_learn():
    return render_template('Learn.html')


if __name__ == "__main__":
    app.run(debug=True)
