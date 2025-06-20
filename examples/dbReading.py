from model.DbSrv import DbSrv
db = DbSrv()

emos = db.conn().execute(db.query("select * from emo_thoughts")).fetchall()
print("Here are emo-thougths: ", emos)

