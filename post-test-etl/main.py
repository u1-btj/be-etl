from etl.extract import get_from_sftp, get_from_api, put_into_server
from etl.transform import convert_into_dict, combine_all
from etl.load import make_dir, create_csv

# For API
url = "https://staging.nmssatellite.com/api/btj_academy"
method = "GET"

# For SFTP Connection
hostname = "eu-central-1.sftpcloud.io"
username = "40f46e344ed146d9a0e3f3d5d4a14f66"
pwd = "5b8d7FzHB34ShRz5OsARxdIskzEJonBf"
port = 22

# File name
file_alamat = "Learn Code Sample Data - Alamat peserta.csv"
file_smt1 = "Learn Code Sample Data - Skor Ujian Semester 1.csv"

# Directory to put the output files
path = "output_result"

# Variable to save all data from different source
all_data = {}

def extract():
    print("Extract Process")

    # Put files from sample directory into remote server
    put_into_server(hostname, username, pwd, port, f"sample/{file_alamat}")
    put_into_server(hostname, username, pwd, port, f"sample/{file_smt1}")
    print("Sample files successfully copied into remote server.")

    # Get response from API
    response = get_from_api(method, url)
    all_data['skor_smt_2'] = response['result']
    print("Get API responses success.")

    # Get and copy files from remote to local parent directory
    get_from_sftp(hostname, username, pwd, port, file_alamat)
    get_from_sftp(hostname, username, pwd, port, file_smt1)
    all_data['alamat'] = convert_into_dict(file_alamat)
    all_data['skor_smt_1'] = convert_into_dict(file_smt1)
    print("Files copied from server to local successfully.")

    # Display all data
    # print("Data Alamat (SFTP)")
    # print(all_data['alamat'])
    # print("Data Nilai Semester 1 (SFTP)")
    # print(all_data['skor_smt_1'])
    # print("Data Nilai Semester 2 (API)")
    # print(all_data['skor_smt_2'])
    print("Extract Done.")

def transform():
    print("Transform Process")
    res = combine_all(all_data) # Transform data into another form
    # Display transform result
    print("Transform Result")
    print(res)
    print("Transform Done.")
    return res

def load(data):
    print("Load Process")
    make_dir(path) # Make output directory
    create_csv(path, data) # Load all data into output directory
    print("Load Done.")

extract()
final_data = transform()
load(final_data)
