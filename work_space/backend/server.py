import json

from flask import Flask, request
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)

username = 'python15'
password = 'ceshiren.com'
host = 'stuq.ceshiren.com:23306'
dbname = 'python15'
options = 'charset=utf8mb4'



app.config['db']=[]
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{username}:{password}@{host}/{dbname}?{options}'
db = SQLAlchemy(app)

class TestCase(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(120), unique=False, nullable=False)
    steps = db.Column(db.String(1024), nullable=True)

    def __repr__(self):
        return '<TestCase %r>' % self.name



class TestCaseService(Resource):
    def get(self):
        # return app.config['db']
        #查询数据库中全部数据
        # return TestCase.query_all()
        #查询单个数据
        testcase_id = request.args.get('id', None)
        if testcase_id:
            testcase = TestCase.query.filter_by(id=testcase_id).first()
            return {'errorcode':1,'body':str(testcase)}
        else:
            # return TestCase.query_all()
            return {'errorcode': 1, 'body': [str(testcase) for testcase in TestCase.query_all()]}

    def post(self):
        #测试用例新增
        # app.config['db'].append(request.json)

        print(**request.json)
        #json数据解开
        testcase = TestCase(**request.json)
        # 解开后的数据存入数据库
        db.session.add(testcase)
        #提交后可去get方法中查询数据
        db.session.commit()

        # return {"msg":"ok", "errcode": 0}

    def put(self):
        #测试用例更新
        pass

    def delete(self):
        #测试用例删除
        pass

#一个任务关联多个测试用例，多对多的关联关系
#一个任务 包含多个测试用例
#一个任务  一个测试用例  中间表
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=True)
    description = db.Column(db.String(120), unique=False, nullable=False)
    testcases = db.Column(db.String(1024), nullable=True)

    def __repr__(self):
        return '<Task %r>' % self.id

    def as_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'testcases': json.dupms(self.testcases)
        }


# 测试计划
class TaskService(Resource):
    def get(self):
        task_id = request.args.get('id', None)
        if task_id:
            task = TestCase.query.filter_by(id=task_id).first()
            return {'errorcode': 1, 'body': str(task)}
        else:
            # return TestCase.query_all()
            return {'errorcode': 1, 'body': [task.as_dict() for task in Task.query_all()]}

    def post(self):
        task = Task(**request.json)
        print(task)
        db.session.add(task)
        db.session.commit()
        return {"msg": "ok", "errcode": 0}

    def put(self):
        pass

    def delete(self):
        pass



api.add_resource(TestCase, '/testcase')
api.add_resource(Task, '/task')

if __name__ == '__main__':
    app.run(debug=True)
