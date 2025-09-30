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
                comment="comentário aleatório",
                timestamp=get_date(),
                origin=origem,
                branch_id=branch_id,
            )
        )

    # CSAT
    for _ in range(500):
        score = random.randint(1, 5)
        origem = random.choice(origens)

        csat_feedbacks.append(
            CSATFeedback(
                score=score,
                comment="comentário aleatório",
                timestamp=get_date(),
                origin=origem,
                branch_id=branch_id,
            )
        )

    return nps_feedbacks, csat_feedbacks


def seed_feedback():
    with Session(engine) as db:
        # Verificar se já existe feedback no banco
        if db.query(NPSFeedback).first() or db.query(CSATFeedback).first():
            print("⚠️ Banco já contém feedback. Seed não será executado.")
            return

        # Buscar branches criadas
        branches = db.query(Branch).all()

        if not branches:
            print("⚠️ Nenhuma branch encontrada. Seed não será executado.")
            return

        total_nps, total_csat = 0, 0

        # Criar feedbacks para cada branch
        for branch in branches:
            nps_list, csat_list = gerar_feedback(branch.id)
            db.add_all(nps_list + csat_list)
            total_nps += len(nps_list)
            total_csat += len(csat_list)

        db.commit()

    print(f"NPS gerados: {total_nps}")
    print(f"CSAT gerados: {total_csat}")
    print("✅ Seed concluído com NPS e CSAT!")
