from jenkinsapi.jenkins import Jenkins
from work_space.backend.server import db, TestCase
import requests


def test_db_init():
    db.create_all()

def test_db():
    db.create_all()
    all = TestCase.query_all()
    print(all)
    testcase = TestCase(name="dengjun", steps="1,2,3")
    db.session.add(testcase)
    db.session.commit()
    all = TestCase.query_all()
    print(all)



def test_testcase_post():
    r = requests.post(
        'http://127.0.0.1:5000/testcase',
        json={'name': '4'}
    )
    assert r.status_code == 200


def test_task():
    r = requests.post(
        'http://127.0.0.1:5000/task',
        json={'testcase': [1, 2, 3]}
    )
    assert r.status_code == 200

    r = requests.get(
        'http://127.0.0.1:5000/task'
    )
    assert r.status_code == 200
    assert len(r.json()['body']) > 0


def test_jenkins():
    jenkins = Jenkins(
        'http://stuq.ceshiren.com:8020',
         username='seveniruby',
        # password得token从jenkins上获取
         password='12345qwer')
         # print(jenkins.version)
         # print(jenkins.keys())
         # jenkins['python15_task'].invoke(build_params={'task':'demo'})

