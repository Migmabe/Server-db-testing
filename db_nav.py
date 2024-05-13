import database
import datetime


class Interface():
    def __init__(self, security=True):
        self.app = database.app
        self.db = database.db
        self.security = security



class CRUD(Interface):

    def create(self, **kwargs):

        """
        :param kwargs: USER(name, username, password, accountType) || SYSTEMLOGON(username)
        :return: Create entries in db
        """
        if "name" in kwargs:
            with self.app.app_context():
                self.db.session.add(database.Users(name=kwargs["name"], username=kwargs["username"],
                                                   password=kwargs["password"], accountType=kwargs["accountType"]))
                self.db.session.commit()
        elif "username" in kwargs:
            with self.app.app_context():
                self.db.session.add(database.SystemLogon(username=kwargs["username"], time=datetime.datetime.now()))
                self.db.session.commit()

    def read(self, db_selection, **kwargs):

        """
        :param db_selection: either "users" or "logon" to retrieve data from one db or the other
        :param kwargs: USER(name, username, accountType) || SYSTEMLOGON(username)
        :return: Read entries in db
        """
        if db_selection == "users":
            if "username" in kwargs:
                # Username is a unique attribute of every user, so cannot find more than one hence scalar.
                # Server does the handling
                with self.app.app_context():
                    entry = self.db.session.execute(self.db.select(database.Users).
                                                    where(database.Users.username == kwargs["username"])).scalar()
                    return entry
            elif "name" in kwargs:
                with self.app.app_context():
                    entry = self.db.session.execute(self.db.select(database.Users).
                                                    where(database.Users.name == kwargs["name"])).scalars()
                    return entry
            elif "accountType" in kwargs:
                with self.app.app_context():
                    entry = self.db.session.execute(self.db.select(database.Users).
                                                    where(database.Users.accountType == kwargs["accountType"])).scalars()
                    return entry

        if db_selection == "logon":
            with self.app.app_context():
                entry = self.db.session.execute(self.db.select(database.SystemLogon).
                                                where(database.SystemLogon.username == kwargs["username"])).scalars()
                return entry

    def read_all(self, database):
        """
        :param database: users|logon
        :return: all entries
        """
        if database == "users" and self.security:
            with self.app.app_context():
                self.db.session.execute(self.db.select(database.Users)).scalars()
        if database == "logon" and self.security:
            with self.app.app_context():
                self.db.session.execute(self.db.select(database.SystemLogon)).scalars()

    def update(self, username, **kwargs):

        """
        :param username: enter a username to update the user's data
        :param kwargs: USER(name, password, accountType) || SYSTEMLOGON(username, time)
        :return: Update entries in db
        """

        with self.app.app_context():
            entry = self.db.session.execute(self.db.select(database.Users).
                                            where(database.Users.username == username)).scalar()

            if kwargs["name"]:
                entry.name = kwargs["name"]
            # only for ADMINS
            if kwargs["accountType"] and self.security:
                entry.username = kwargs["accountType"]
            if kwargs["password"]:
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
