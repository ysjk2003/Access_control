#사용법  
python3 main.py -m MODE ...  

#사용 가능한 모드  
crawler  
auth_check  

#auth_check 사용법  
python3 main.py -m auth_check -u http://192.168.1.1 -t target.txt -k keyword  
텍스트 파일 양식은 target.txt 참고  

#crawler 사용법  
python3 main.py -m crawler -u 192.168.1.1 -p 80  