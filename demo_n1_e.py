def get_users_with_tags():
    users = User.objects.all()
    for user in users:
        tags = user.tags.all()  # N+1 쿼리
