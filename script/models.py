import json

from peewee import *
from enum import Enum
from peewee_enum_field import EnumField

database = SqliteDatabase('../db.sqlite')


class BaseModel(Model):
    class Meta:
        database = database


class InstagramStatus(Enum):
    active = 'active'
    suspended = 'suspended'
    challenging = 'challenging'


class UsageStatus(Enum):
    free = 'free'
    busy = 'busy'


class Accounts(BaseModel):
    username = CharField(unique=True)
    password = CharField()
    phone = CharField()
    session = TextField()
    instagram_status = EnumField(InstagramStatus)
    usage_status = EnumField(UsageStatus)
    log = TextField()
    created_at = CharField()
    updated_at = CharField()

    def make_challenging(self, log=''):
        self.instagram_status = InstagramStatus.challenging
        self.log = log
        self.save()

    def save_session(self, session):
        self.session = session
        self.save()

    def dict_session(self):
        # try:
        if self.session:
            return json.loads(self.session)

        #         except:
        #             print(f'Problem loading {self.username} session to dict ..')

        return self.session

    @staticmethod
    def get_first_free():
        return Accounts.get_or_none(
            Accounts.usage_status == UsageStatus.free,
            Accounts.instagram_status == InstagramStatus.active
        )

    @staticmethod
    def free_up_all_accounts():
        return (Accounts
                .update(usage_status=UsageStatus.free)
                .where(Accounts.usage_status == UsageStatus.busy)
                .execute())

    @staticmethod
    def pick_one():
        account = Accounts.get_first_free()

        if not account:
            Accounts.free_up_all_accounts()
            account = Accounts.get_first_free()

        account.usage_status = UsageStatus.busy
        account.save()

        return account
