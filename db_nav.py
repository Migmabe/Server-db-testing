import database
import datetime


class Interface():
    def __init__(self, security=True):
        self.app = database.app
        self.db = database.db
        self.security = security


class CRUD(Interface):

    def create(self, args=None, **kwargs):

        """
        :param args: USER or SYSTEMLOGON. Table class creations defined in users.py
        :param kwargs: USER(name, username, password, accountType) || SYSTEMLOGON(username, time)
        :return: Create entries in db
        """

        if args[0].upper() == "USER" or args[1].upper() == "USER" or args[0].upper() == "U":
            with self.app.app_context():
                self.db.session.add(database.Users(name=kwargs["name"], username=kwargs["username"],
                                                   password=kwargs["password"], accountType=kwargs["accountType"]))
                self.db.session.commit()

        if args[0].upper() == "SYSTEMLOGON" or args[1].upper() == "SYSTEMLOGON" or args[0].upper() == "S":
            with self.app.app_context():
                self.db.session.add(database.SystemLogon(username=kwargs["username"], time=datetime.datetime.now()))
                self.db.session.commit()


    def read(self, args=None, **kwargs):

        """
        :param args: USERS or SYSTEMLOGON. Table class creations defined in users.py
        :param kwargs: USER(name, username, password, accountType) || SYSTEMLOGON(username)
        :return: Read entries in db
        """
        if args[0].upper() == "USERS" or args[1].upper() == "USERS":
            with self.app.app_context():
                entry = self.db.session.execute(self.db.select(database.Users).
                                                where(database.Users.username == kwargs["username"])).scalar()
                return entry

        if args[0].upper() == "SYSTEMLOGON" or args[1].upper() == "SYSTEMLOGON":
            with self.app.app_context():
                entry = self.db.session.execute(self.db.select(database.SystemLogon).
                                                where(database.SystemLogon.username == kwargs["username"])).scalar()
                return entry

    def read_all(self):
        with self.app.app_context():
            self.db.session.execute(self.db.select(database.Users)).scalars()

    def update(self, username, **kwargs):

        """
        :param username: enter a username to update the user's data
        :param kwargs: USER(name, username, password, accountType) || SYSTEMLOGON(username, time)
        :return: Update entries in db
        """

        with self.app.app_context():
            entry = self.db.session.execute(self.db.select(database.Users).
                                            where(database.Users.username == username)).scalar()

            if kwargs["name"] and self.security:
                entry.name = kwargs["name"]
            if kwargs["username"] and self.security:
                entry.username = kwargs["username"]
            if kwargs["password"] and self.security:
                entry.password = kwargs["password"]

    def deletion(self, username):

        """
        :param username: enter a username to delete it
        :return: Delete entries in db
        """

        with self.app.app_context():
            entry = self.db.session.execute(self.db.select(database.Users).
                                            where(database.Users.username == username)).scalar()
            if self.security:
                self.db.session.delete(entry)
                self.db.session.commit()

# -------------OPERATION BLOCK---------------#



