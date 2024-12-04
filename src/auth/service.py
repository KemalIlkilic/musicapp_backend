#A session object is a way to manage database connections and transactions.
#It acts as an interface between your application code and the database.
from sqlmodel.ext.asyncio.session import AsyncSession
from src.db.models import User
from sqlmodel import select, desc
from .utils import generate_password_hash
from .schemas import UserCreateModel

class UserService:
    async def user_exists_by_email(self, email : str, session : AsyncSession):
        user = await self.get_user_by_email(email, session)
        return True if user else False
    
    async def get_all_users(self, session:AsyncSession):
        statement = select(User).order_by(desc(User.created_at))
        result = await session.exec(statement)
        return result.all()
    
    async def get_user_by_uid(self, user_uid : str ,session:AsyncSession):
        statement = select(User).where(User.uid == user_uid )
        result = await session.exec(statement)
        user = result.first()
        return user if user else None
    
    async def get_user_by_email(self, email : str, session : AsyncSession):
        statement = select(User).where(User.email == email)
        result = await session.exec(statement)
        user = result.first()
        return user

    async def create_user(self, user_data: UserCreateModel, session: AsyncSession):
        user_data_dict = user_data.model_dump()
        new_user = User(**user_data_dict)
        new_user.password_hash = generate_password_hash(user_data_dict['password'])
        session.add(new_user)
        await session.commit()
        return new_user