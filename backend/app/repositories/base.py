from typing import TypeVar, Generic, Type, List, Optional
from fastapi import HTTPException
from sqlmodel import SQLModel, Session, select, update, case

T = TypeVar("T", bound=SQLModel)


class BaseRepository(Generic[T]):
    def __init__(self, model: Type[T], name: str = 'Element'):
        self.model = model
        self.name = name

    def get_all(self, session: Session) -> List[T]:
        return session.exec(select(self.model)).all()

    def get_by_id(self, session: Session, id: int) -> Optional[T]:
        item = session.get(self.model, id)
        if item:
            return item
        else:
            raise HTTPException(status_code=404, detail=f"{self.name} not found")

    def create(self, session: Session, item: T) -> T:
        session.add(item)
        session.commit()
        session.refresh(item)
        return item
    
    def create_many(self, session: Session, items: List[T]) -> List[T]:
        session.add_all(items)
        session.commit()
        for item in items:
            session.refresh(item)
        return items


    def update(self, session: Session, item: T) -> T:
        session.add(item)
        session.commit()
        session.refresh(item)
        return item
    
    
    def bulk_update_field(
        self,
        session: Session,
        updates: dict[int, str],
        field_name: str
    ):
        field = getattr(self.model, field_name)

        stmt = (
            update(self.model)
            .where(self.model.id.in_(updates.keys()))
            .values(
                {
                    field_name: case(
                        *[(self.model.id == item_id, value) for item_id, value in updates.items()],
                        else_=field
                    )
                }
            )
        )

        session.exec(stmt)
        session.commit()


    def update_by_id(self, session: Session, id: int, data: T) -> Optional[T]:
        item = session.get(self.model, id)
        if not item:
            raise HTTPException(status_code=404, detail=f"{self.name} not found")
        item_data = data.model_dump(exclude_unset=True)
        item.sqlmodel_update(item_data)
        session.add(item)
        session.commit()
        session.refresh(item)
        return item

    def delete(self, session: Session, id: int) -> None:
        item = self.get_by_id(session, id)
        if not item:
            raise HTTPException(status_code=404, detail=f"{self.name} not found")
        session.delete(item)
        session.commit()
        return
        