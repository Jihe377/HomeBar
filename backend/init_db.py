from app.db.base import Base
from app.db.session import engine
from app.models import bar_item, recipe, cocktail_record, shopping, preference


def init_db():
    """
    初始化数据库，创建所有表。
    """
    Base.metadata.create_all(bind=engine)
    print("数据库表已创建")


def drop_db():
    """
    删除所有表（用于开发环境重置）。
    """
    Base.metadata.drop_all(bind=engine)
    print("数据库表已删除")


if __name__ == "__main__":
    init_db()