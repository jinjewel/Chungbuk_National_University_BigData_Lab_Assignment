import pandas as pd
import os

# CSV 파일이 저장된 디렉토리 경로를 지정합니다.
csv_files_path = r'C:/Users/User/Desktop/Dig_Data_lab/Project/2.공공데이터포털_OpenAPI_가져오기/'

# CSV 파일들을 읽어서 데이터프레임 리스트에 추가합니다.
dfs = []
for file_name in os.listdir(csv_files_path):
    if file_name.endswith('.csv'):
        file_path = os.path.join(csv_files_path, file_name)
        try:
            df = pd.read_csv(file_path)
            if not df.empty:
                dfs.append(df)
                print(f"{file_name} 파일을 성공적으로 읽었습니다.")
            else:
                print(f"{file_name} 파일은 비어 있습니다.")
        except Exception as e:
            print(f"{file_name} 파일을 읽는 중 오류가 발생했습니다: {e}")

# 데이터프레임들을 병합합니다.
if dfs:
    merged_data = pd.concat(dfs, ignore_index=True)
    print("모든 데이터프레임이 성공적으로 병합되었습니다.")
else:
    print("병합할 데이터프레임이 없습니다. CSV 파일들을 확인하세요.")

# 병합된 데이터프레임을 CSV 파일로 저장합니다.
output_path = 'C:/Users/User/Desktop/Dig_Data_lab/Project/2.공공데이터포털_OpenAPI_가져오기/merged_data.csv'  
try:
    merged_data.to_csv(output_path, index=False)
    print(f"병합된 데이터가 {output_path} 경로에 저장되었습니다.")
except Exception as e:
    print(f"병합된 데이터를 저장하는 중 오류가 발생했습니다: {e}")

