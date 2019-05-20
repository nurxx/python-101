class Column:
    constraints = ()
    def __init__(self, unique=False):
        self.unique = unique

    def get_constraints(self):
        #('PRIMARY KEY','AUTOINCREMENT') => 'PRIMARY KEY AUTOINCREMENT'
        return ''.join(self.constraints)

    def as_sql(self,name):
        # 'id INTEGER PRIMARY KEY AUTOINCREMENT'
        constraints_str=self.get_constraints()
        unique_str = self.unique and 'UNIQUE' or ''
        return f'{self.name} {self.column_type} {constraints_str} {unique_str}'

class PKColumn(Column):
    column_type = 'INTEGER'
    constraints = (
        'PRIMARY KEY',
        'AUTOINCREMENT',
        'UNIQUE'
        )

class TextColumn(Column):
    column_type = 'TEXT'

class BaseModelMetaClass(type):
    pass

class BaseModel(metaclass=BaseModelMetaClass)
    id = PKColumn()

    def get_columns(self):
        columns = {}
        for key,value in self.__class__.__dict__.items():
            if isinstance(value, Column):
                columns[key] = value
        return columns 

    def create_table(self):
        return f'''
        CREATE TABLE {self.__tablename__}(
        )
        '''

class User(BaseModel):
    __tablename__='users'
    full_name = TextColumn()
    def get_columns(self):
        super().get_columns()
