from mongoengine import *
import datetime

#db = connect('newTest')
#db.drop_database('newTest')
class AnswerRec(EmbeddedDocument):
    correct_ans = StringField()
    user_ans = StringField()
    solve_time = DecimalField()

class LevelDataRec(EmbeddedDocument):
    start_timestamp = DateTimeField()
    answer  = ListField(EmbeddedDocumentField(AnswerRec))
    
    
class DynamicRecord(Document):
    username = StringField()
    subject = StringField()
    theme = StringField()
    score = IntField()
    level = IntField()
    data = ListField(EmbeddedDocumentField(LevelDataRec))


ac = AnswerRec(correct_ans='1', user_ans = '2', solve_time=4.5)


a = LevelDataRec(start_timestamp=datetime.datetime.utcnow(),answer=[ac])


#g = GroupRec(group_id = '',  start_group_date = datetime.date(1, 2, 3), leave_group_date= datetime.date(1, 2, 3), score= 4, next_level = '', answer_data = [a])



d = DynamicRecord()
d.username = 'adi'
d.subject = 'Counting'
d.theme = 'Shapes'
d.score = 20
d.level = 2
d.data = [a]

#.save()


############## group

class UserDataRec(EmbeddedDocument):
    user_id = StringField()
    user_name = StringField()
    join_timestamp = DateTimeField()
    leave_timestamp = DateTimeField()



class GroupDetail(Document):
    group_name = StringField()
    school_id = StringField()
    admin_id = StringField()
    created_by = StringField()
    user_data = ListField(EmbeddedDocumentField(UserDataRec))

    def __str__(self):
       return str("group name: " + self.group_name+"\n"+"created_by : " + str(self.created_by) +"\n")