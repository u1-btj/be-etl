import pandas

def convert_into_dict(files):
    data = pandas.read_csv(files)
    return data.to_dict(orient='records')

def combine_all(all_data):
    temp = {}
    for i in all_data['alamat']:
        temp[f"{i['No']}-{i['Murid']}-{i['Gender']}-{i['Kota Asal']}"] = {}
    for i in all_data['skor_smt_1']:
        for j in temp.items():
            if i['Murid'] in j[0].split('-'):
                j[1]['Semester'] = [1]
                j[1]['Matematika'] = [i['Matematika']]
                j[1]['IPA'] = [i['IPA']]
                j[1]['IPS'] = [i['IPS']]
                j[1]['Bahasa'] = [i['Bahasa']]
                j[1]['Seni'] = [i['Seni']]
                j[1]['Olahraga'] = [i['Olahraga']]
    for i in all_data['skor_smt_2']:
        for j in temp.items():
            if i['Murid'] in j[0].split('-'):
                j[1]['Semester'].append(2)
                j[1]['Matematika'].append(i['Matematika'])
                j[1]['IPA'].append(i['IPA'])
                j[1]['IPS'].append(i['IPS'])
                j[1]['Bahasa'].append(i['Bahasa'])
                j[1]['Seni'].append(i['Seni'])
                j[1]['Olahraga'].append(i['Olahraga'])
    return(temp)
    




    
