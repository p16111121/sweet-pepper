#把url放入db
def inserturl(url,updatetime,time_sec):
    import mysql.connector #pip install mysql-connector-python
    #資料庫資料
    db_settings = {
        "host": "140.130.89.143",
        "database" : "sweetpepper",
        "user" : "bmeuserb",
        "password" : "BME7606B",
        "port" : "3306"}
    print("Inserting url,updatetime into image_url table")
    try:
        #對目標資料庫建立連線
        connection = mysql.connector.connect(**db_settings)
        #建立指標物件
        with connection.cursor() as cursor:
            #sql查詢語句
            sql_insert_query = """ INSERT INTO sweetpepper.imageurl 
                                    (url,updatetime,time_sec) VALUES (%s,%s,%s)"""
        
            #Convert data into tuple format
            insert_tuple = (url,updatetime,time_sec)
            result = cursor.execute(sql_insert_query, insert_tuple)
            connection.commit()
        print("Image inserted Successfully into MySQL",result)
    except mysql.connector.Error as error:
        print("Failed inserting image into MYSQL {}".format(error))
        
    finally:
        if connection.is_connected():
            #cursor.close()
            connection.close()
            print("MYSQL connection is closed")
            
if __name__ == '__main__':
    inserturl("test/url","2020-09-09 21:00:00",10082094)