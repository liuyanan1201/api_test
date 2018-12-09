import pymysql

from conf import config

def get_coon():
    coon = pymysql.connect(host=config.db_host,
                           port=config.db_port,
                           user=config.db_user,
                           password=config.db_password,
                           db=config.db,
                           charset='utf8')

    return coon

def db_query(sql):
    config.logging.debug(sql)
    # print(sql)
    c = get_coon()#调用上面的连接
    cur=c.cursor()#建立游标
    cur.execute(sql)
    r=cur.fetchall()
    config.logging.debug(r)
    # print(r)
    cur.close()
    c.close()
    return r
def db_change(sql):  #修改数据库时，如果sql出错了可以回滚 使用try
    # print(sql)
    try:
        c=get_coon()
        cur=c.cursor()
        cur.execute(sql)
        c.commit()#提交修改
    except Exception as e:
        config.logging.error(repr(e))   #打印错误信息
        e.rollback() # 回滚修改
    finally:
        cur.close()
        c.close()


#查询用户是否存在
def check_user(name):
    r = db_query("select * from user where name='%s'" % name)
    if r:
        return True
    return False

def del_user(name):
    db_change("delete from user where name='%s'" % name)

# if __name__=='__main__':  #用来判断是不是从当前模块执行
#     print(check_user("001"))  #调试信息

