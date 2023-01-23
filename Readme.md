# NTE System  
This is NTE System Project
## Instalation  
```bash
git clone https://github.com/m4ri01/NTE-Project.git
cd NTE-Project/
mkdir db_data
docker-compose up -d
docker-exec -ti backEndService /bin/bash
```  
inside the backEndService container type this
```bash
flask db migrate
flask db upgrade
```  

After that exit using CTRL+C