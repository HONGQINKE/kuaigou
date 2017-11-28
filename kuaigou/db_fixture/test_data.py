import sys
sys.path.append('/home/jane/p3_project/kuaigou/db_fixture')
from mysql_db import DB
from mysql_dbb import DBB

def init_data():
    db = DB()
    datas ={
        'kuaigou_sys_user_role_info':[
        {'role_id':'1','role_name':'superadmin','role_des':'remark','is_creat_role_list':'N','create_time':'1511342065','update_time':'1511342065'},
        {'role_id':'2','role_name':'salesman','role_des':'remark','is_creat_role_list':'N','create_time':'1511342065','update_time':'1511342065'},
        {'role_id':'3','role_name':'customer service','role_des':'remark','is_creat_role_list':'N','create_time':'1511342065','update_time':'1511342065'},


],
        'kuaigou_sys_user_info':[
        {'user_id':1,'user_name':'admin','user_pass':'09b11f110be6a46a2445e15ad3a68422184553a0','user_nick_name':'super admin','role_id':1,'effective_mark'
:1,'create_time':'1511342065','last_login':'1511342065','region_id':234},
        {'user_id':2,'user_name':'815653821@qq.com','user_pass':'09b11f110be6a46a2445e15ad3a68422184553a0','user_nick_name':'jack','role_id':2,'effective_mark':1,'create_time':'1511342065','last_login':'1511342065','region_id':234},
        {'user_id':3,'user_name':'815653822@qq.com','user_pass':'09b11f110be6a46a2445e15ad3a68422184553a0','user_nick_name':'rose','role_id':3,'effective_mark':1,'create_time':'1511342065','last_login':'1511342065','region_id':234},

],

        'kuaigou_city_list':[
        {'city_id':1,'region_id':234,'city_code':1,'city_create_time':'1494299098','city_updata_time':'1494299098','city_operation_user':'1','operation_user_name':'admin','city_name':'深圳市'},
        {'city_id':2,'region_id':2,'city_code':2,'city_create_time':'1494299098','city_updata_time':'1494299098','city_operation_user':'1','operation_user_name':'admin','city_name':'北京市'},
],

        'kuaigou_car_info':[
        {'car_id':1,'car_des':'小型面包车','car_status':1,'car_operation_user':1,'car_ext':'乘客|搬运|拆座','creat_time':'1511495941',
'car_operation_user_name':'admin','update_time':'1511495941','car_lenght':1,'car_weight':2,'car_width':3,'car_type':1,'car_size':1},
        {'car_id':2,'car_des':'小型货车','car_status':1,'car_operation_user':1,'car_ext':'乘客|搬运|拆座','creat_time':'1511495941',
'car_operation_user_name':'admin','update_time':'1511495941','car_lenght':1,'car_weight':2,'car_width':3,'car_type':2,'car_size':1},


],

        'kuaigou_car_price':[
        {'price_id':1,'car_id':1,'region_id':234,'car_start_price':10,'car_start_mileage':10,'car_beyond_mileage':1,'car_beyond_price':5,'create_time':'1494212554','price_operation_user':1,'status':1,'update_time':'1494212554','price_operation_user_name':'admin'},
        {'price_id':2,'car_id':1,'region_id':234,'car_start_price':15,'car_start_mileage':20,'car_beyond_mileage':1,'car_beyond_price':6,'create_time':'1494212554','price_operation_user':1,'status':1,'update_time':'1494212554','price_operation_user_name':'admin'},


]
}
    for table,data in datas.items():
        db.clear(table)
        for d in data:
            db.insert(table,d)
    db.close()


def init_datab():
    db = DBB()
    datas ={
        't_coupons_batch':[
        {'ID':1,'BATCH_NAME':'中秋节活动','COUPON_TYPE':1,'COUPON_VALUE':10,'EARN_WAY':1,'EARN_MODE':1,'MIN_ORDER_AMOUNT':50,'EARN_START_TIME':'2017-11-24 00:00:00','EARN_CLOSE_TIME':'2017-11-24 23:59:59','USE_START_TIME':'2017-11-24 00:00:00','USE_CLOSE_TIME':'2017-11-24 23:59:59','CITY_NAMES':'|深圳市|北京市|','CITY_CODES':'234|2|','MAX_NUM':10,'EARN_NUM':0,'ACTIVITY_STATE':2,'CREATE_TIME':'2017-11-24 00:00:00','CREATE_USER_ID':1,'UPDATE_TIME':'2017-11-24 00:00:00'},
        {'ID':2,'BATCH_NAME':'双11活动','COUPON_TYPE':2,'COUPON_VALUE':8,'MAX_DEDUCT_AMOUNT':20,'EARN_WAY':1,'EARN_MODE':1,'MIN_ORDER_AMOUNT':0,'EARN_START_TIME':'2017-11-24 00:00:00','EARN_CLOSE_TIME':'2017-11-24 23:59:59','USE_START_TIME':'2017-11-24 00:00:00','USE_CLOSE_TIME':'2017-11-24 23:59:59','CITY_NAMES':'|深圳市|北京市|','CITY_CODES':'234|2|','MAX_NUM':10,'EARN_NUM':0,'ACTIVITY_STATE':2,'CREATE_TIME':'2017-11-24 00:00:00','CREATE_USER_ID':1,'UPDATE_TIME':'2017-11-24 00:00:00'},
],
}

    for table,data in datas.items():
        db.clear(table)
        for d in data:
            db.insert(table,d)
    db.close()




if __name__ == '__main__':
    init_data()
    init_datab()
