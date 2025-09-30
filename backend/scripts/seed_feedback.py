import sys
import pathlib
from datetime import datetime, timezone, timedelta
import random

BACKEND_ROOT = pathlib.Path(__file__).resolve().parents[1]
if str(BACKEND_ROOT) not in sys.path:
    sys.path.insert(0, str(BACKEND_ROOT))

from sqlmodel import Session
from app.services.database.database import engine
from app.models.branch import Branch
from app.models.user import User
from app.models.nps import NPSFeedback
from app.models.csat import CSATFeedback


def get_date():
    agora = datetime.now(timezone.utc)
    delta = timedelta(days=random.randint(0, 10),  # dias
                      seconds=random.randint(0, 86400))  # segundos adicionais no dia
    data_aleatoria = agora - delta
    return data_aleatoria.isoformat(timespec="milliseconds").replace("+00:00", "Z")

def gerar_feedback(branch_id: int):
    """Gera listas de feedback NPS e CSAT aleatórios para uma branch."""
    nps_feedbacks = []
    csat_feedbacks = []

    origens = ["site", "app", "telefone", "email", "chat", "presencial"]


    # NPS
    for _ in range(500):
        score = random.randint(0, 10)
        origem = random.choice(origens)

        nps_feedbacks.append(
            NPSFeedback(
                score=score,
                comment='comentário aleatório',
                timestamp=get_date(),
                origin=origem,
                branch_id=branch_id
            )
        )

    # CSAT
    for _ in range(500):
        score = random.randint(1, 5)
        origem = random.choice(origens)

        csat_feedbacks.append(
            CSATFeedback(
                score=score,
                comment='comentário aleatório',
                timestamp=get_date(),
                origin=origem,
                branch_id=branch_id,
            )
        )

    return nps_feedbacks, csat_feedbacks


def seed():
    with Session(engine) as db:
        # Criar usuário admin se não existir
        existing = db.query(User).filter_by(username="admin").first()
        if not existing:
            db.add(User(username="admin", password="admin"))

        # Criar branches iniciais se não existirem
        branch_names = ("Filial A", "Filial B")
        for name in branch_names:
            if not db.query(Branch).filter_by(name=name).first():
                db.add(Branch(name=name))
        db.commit()

        # Buscar branches criadas
        branches = db.query(Branch).all()

        # Criar feedbacks para cada branch
        for branch in branches:
            nps_list, csat_list = gerar_feedback(branch.id)
            db.add_all(nps_list + csat_list)
        

        db.commit()

    print(f"NPS gerados: {len(nps_list)}")
    print(f"CSAT gerados: {len(csat_list)}")
    print("✅ Seed concluído com NPS e CSAT!")
  


if __name__ == "__main__":
    seed()
