import hashlib
        pwd = str(hashlib.md5("123456".encode('utf-8').strip()).hexdigest())
        u = User(name='admin',  username='admin', password=pwd, user_role=UserRole.USER)
        db.session.add(u)
        db.session.commit()