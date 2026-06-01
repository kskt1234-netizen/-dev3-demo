"""게시글 관련 기능 — 데모용 (의도적 결함 포함)."""


def get_posts(post_ids):
    """게시글 목록 조회. ⚠️ N+1 쿼리 + 테스트 없음."""
    posts = []
    for pid in post_ids:                                    # 루프
        post = db.query(f"SELECT * FROM posts WHERE id={pid}")  # 루프 안 DB 호출 → N+1
        posts.append(post)
    return posts


def calc_discount(price, rate):
    """할인가 계산 — 유일하게 테스트된 함수."""
    return price * (1 - rate)


def find_dups(items):
    """중복 찾기. ⚠️ O(n²) 이중 루프 + 테스트 없음."""
    result = []
    for i in items:                  # 바깥 루프
        for j in items:              # 안쪽 루프 → O(n²)
            if i == j:
                result.append(i)
    return result
