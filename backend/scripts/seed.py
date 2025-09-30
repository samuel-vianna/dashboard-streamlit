import sys
import pathlib

BACKEND_ROOT = pathlib.Path(__file__).resolve().parents[1]
if str(BACKEND_ROOT) not in sys.path:
    sys.path.insert(0, str(BACKEND_ROOT))

from sqlmodel import Session
from app.services.database.database import engine
from app.models.branch import Branch
from app.models.user import User


def seed():
    with Session(engine) as db:
        # Criar usuário admin se não existir
        existing = db.query(User).filter_by(username="admin").first()
        if not existing:
            db.add(User(username="admin", password="$2b$12$6plSiqZo6O3H57IT/mCTAOh3EfAA6w/B96pvFXCT7LN2NvVfAvkDS"))

        # Criar branches iniciais se não existirem
        for name in ("Filial A", "Filial B"):
            if not db.query(Branch).filter_by(name=name).first():
                db.add(Branch(name=name))

        db.commit()
    print("✅ Seed concluído!")


