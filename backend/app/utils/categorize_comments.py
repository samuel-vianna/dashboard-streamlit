from typing import Callable
from sqlmodel import Session

def categorize_comments(
    session: Session,
    repository,          
    categorize_fn: Callable[[list[str]], list[str]], 
    limit: int = 100,
    field: str = "sentiment"
):

    # 1️⃣ Pegar comentários não categorizados
    comments = repository.get_uncategorized_comments(session, limit)

    if not comments:
        return 0

    # 2️⃣ Pegar só os textos
    texts = [c.comment for c in comments]

    if not texts:
        return 0

    # 3️⃣ Mandar para IA categorizar
    sentiments = categorize_fn(texts).sentiments

    if not sentiments or len(sentiments) != len(comments):
        return 0

    # 4️⃣ Mapear de volta para {id: sentimento}
    updates = {c.id: sentiment for c, sentiment in zip(comments, sentiments)}

    # 5️⃣ Atualizar campo em massa
    repository.bulk_update_field(session, updates, field)

    return len(updates)