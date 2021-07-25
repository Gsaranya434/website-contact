from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from FskORM_model import DetailTable


class DetailQuery:
    def __init__(self):
        self.engine = create_engine('mysql+pymysql://root:@localhost/SQL')
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()
        self.Base = declarative_base()

    def insert(self, getdict):
        self.Base.metadata.create_all(self.engine)
        new_result = DetailTable(getdict)
        self.session.add(new_result)
        self.session.commit()

    def read(self, data):
        try:
            new_query = self.session.query(DetailTable).filter(DetailTable.id == data)
            for x in new_query:
                return x.name, x.phone_number, x.location, x.gmail

        except Exception as err:
            return err

    def all_data(self):
        to_read_list = []
        query = self.session.query(DetailTable)
        for x in query:
            to_read_list.append(x.id)
        # get_data = input('which Id you like to point out : ')
        return to_read_list

    def update(self, get):
        try:
            new_query = self.session.query(DetailTable).filter(DetailTable.id == int(get['integer_u']))
        except Exception as err:
            return err
        else:
            for x in new_query:
                new = get
                x.name = new['name']
                x.phone_number = new['phone_number']
                x.location = new['location']
                x.gmail = new['gmail']
            self.session.commit()
        return True

    def delete(self, data):
        try:
            new_query = self.session.query(DetailTable).filter(DetailTable.id == data)
        except Exception as err:
            return err
        finally:
            for x in new_query:
                self.session.delete(x)
            self.session.commit()


