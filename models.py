from app import app, db

class Project(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    project_name = db.Column(db.String(50), index = True, unique = False)
    phase = db.Column(db.String(20), index = True, unique = False)
    team = db.Column(db.String(50), index = True, unique = False)
    
    def __repr__(self):
        return "Project {self.project}_{self.phase}_{self.team}

class Tests(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50), index = True, unique = True)
    description = db.Column(db.String(400), index = True, unique = False)
    resource = db.Column(db.String(50), index = True, unique = False)
    category = db.Column(db.String(20), index = True, unique = False)
    pass_fail_req = db.Column(db.String(100), index = True, unique = False)
    owner = db.Column(db.String(30), index = True, unique = False)
    
    def __repr__(self):
        return "Test ID:{self.id}: {self.name}"

class TestList(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    items = db.Relationship('TestCase', backref='testlist', lazy='dynamic')
    
    def __repr__(self):
        return "Testlist #{self.id}"

class TestCase(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    testlist_id = db.Column(db.Integer, db.ForeignKey('testlist.id')
    test_id = db.Column(db.Integer, db.ForeignKey('test.id')
